import csv
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton, QLCDNumber, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtMultimedia import QSound
import datetime
import sys
import os
import pyaudio
import wave
MAIN_PATH = 'D:/Python/Liam/'
CHUNK = 1024


class StudyClock(QWidget):
    def __init__(self):
        super().__init__()
        """
        self.time_start = datetime.datetime.now()
        self.time_end = datetime.datetime.now()
        self.time_show = datetime.datetime.strptime("00:00:00", "%H:%M:%S")
        self.model = 1# 判断计增还是计减
        self.file_now = ""
        self.initInfo()
        self.initUI()
        self.flag = 1# 判断是否停止
        self.flag_off = 1#判断是否非法退出"""
        self.initAll()

    def initAll(self):
        self.time_start = datetime.datetime.now()
        self.time_end = datetime.datetime.now()
        self.time_show = datetime.datetime.strptime("00:00:00", "%H:%M:%S")
        self.model = 1  # 判断计增还是计减
        self.file_now = ""
        self.initInfo()
        self.initUI()
        self.flag = 1  # 判断是否停止
        self.flag_off = 1  # 判断是否非法退出
        self.music_on = 2 # 判断是否播放音乐

    def initInfo(self):
        if input("please choose the model(1: timer, 2: countdown): ") == '1':
            self.Timer()
        else:
            self.count_down()

    def Timer(self):
        self.get_task()
        task_tar = "8"#input("please enter the num of task: ")  # 选择目标任务
        self.task_name = "test_timer"#input("please enter the name of this task")  # 任务名称
        file_name = self.get_task(task_num=int(task_tar)).split(',')[2]  # 获取目标任务对应文件
        self.file_path = '/ConfigFile/TimeControl/' + file_name + '.csv'
        self.file_now = file_name
        self.time_start = datetime.datetime.now()
        #self.time_st = datetime.datetime.strptime("00:00:00", "%H:%M:%S")
        #self.model = 1


    def count_down(self):
        self.get_task()
        task_tar = "8"#input("please enter the num of task: ")  # 选择目标任务
        time_count = "00"#input("please enter the time to count down: ")  # 倒计时时间 输入分钟
        task_name = "test_countdown"#input("please enter the name of this task")  # 任务名称
        file_name = self.get_task(task_num=int(task_tar)).split(',')[2]  # 获取目标任务对应文件
        file_path = '/ConfigFile/TimeControl/' + file_name + '.csv'
        self.file_now = file_name
        time_start = datetime.datetime.now()
        time_end = time_start + datetime.timedelta(seconds=float(time_count) * 60)# TODO:将10改回60
        #input_str = task_name + "," + time_start.strftime("%Y%m%d%H%M%S") + "," + time_end.strftime("%Y%m%d%H%M%S")
        self.time_show = datetime.datetime.strptime("00:"+time_count+":10", "%H:%M:%S")
        self.model = 2
        input_list = []
        input_list.append(task_name)
        input_list.append(time_start.strftime("%Y%m%d%H%M%S"))
        input_list.append(time_end.strftime("%Y%m%d%H%M%S"))
        for str in input_list:
            print("test1", str)
        #input_list.append(input_str)
        if os.path.exists(MAIN_PATH + file_path):
            self.add_task(input_list, file_path)
        else:
            file = open(MAIN_PATH + file_path, 'w')
            file.close()
            self.add_task(input_list, file_path)

    def initUI(self):

        # 窗口信息
        self.setGeometry(800, 300, 250, 200)
        self.setWindowTitle('Study Clock')
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.show()

        # 显示时间的元件
        self.lcd = QLCDNumber(self)
        # 设置为显示八个字符
        self.lcd.setDigitCount(8)

        # 其他按钮
        self.qbtn = QPushButton('Start', self)
        self.qbtn.clicked.connect(self.qbtnReset)
        # 暂停按钮
        self.pbtn = QPushButton('Pause', self)
        self.pbtn.clicked.connect(self.pbtnClicked)
        # 放成一列
        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(self.pbtn)
        vbox.addWidget(self.qbtn)
        if self.model == 2:
            self.pbtn.hide()
        self.qbtn.hide()
        self.setLayout(vbox)

        # 利用计时器每一秒打印时间
        self.timer = QTimer(self)
        if self.model == 1:
            self.timer.timeout.connect(self.showTime_add)
        elif self.model == 2:
            self.timer.timeout.connect(self.showTime_sub)
        self.timer.start(1000)

        #self.time_start = datetime.datetime.strptime("00:00:07", "%H:%M:%S")

    def showTime_add(self):
        text = self.time_show.strftime("%H:%M:%S")
        print("test2", text)
        if int(text[-1]) % 2 != 0:
            text = text[0:2] + ' ' + text[3:5] + ' ' + text[6:]
        self.lcd.display(text)
        if self.flag == 1:
            self.time_show = self.time_show + datetime.timedelta(seconds=float('1'))

    def showTime_sub(self):
        text = self.time_show.strftime("%H:%M:%S")
        print("test3", text)
        if(text == '00:00:00'):
            self.ring_on()
            sys.exit(9)
        if(text == '00:00:00'):
            self.flag_off = 2
            self.lcd.display('00:00:00')
            return
        if int(text[-1]) % 2 != 0:
            text = text[0:2] + ' ' + text[3:5] + ' ' + text[6:]
        self.lcd.display(text)
        self.time_show = self.time_show - datetime.timedelta(seconds=float('1'))

    def get_task(self, task_num=0, end_path='/ConfigFile/TimeControl/schedule.csv'):
        schedule_file = open(MAIN_PATH + end_path, 'r', newline='')
        schedule_list = schedule_file.readlines()
        i = 1
        if task_num > 0:
            return schedule_list[task_num-1]
        for s in schedule_list:
            print(i, s)
            i = i + 1
        schedule_file.close()

    def add_task(self, add_list, end_path='/ConfigFile/TimeControl/schedule.csv'):
        for add in add_list:
            print("testt", add)
        schedule_file = open(MAIN_PATH + end_path, 'r', newline='')
        reader = csv.reader(schedule_file)
        reader_list = list(reader)
        schedule_file.close()
        reader_list.append(add_list)
        schedule_file = open(MAIN_PATH + end_path, 'w', newline='')
        writer = csv.writer(schedule_file)
        writer.writerows(reader_list)
        schedule_file.close()
        """
        schedule_writer = csv.writer(schedule_file)
        if len(add_list) != 0:
            schedule_writer.writerow(add_list)
        else:
            print("TimeControl ERROR! the input row is none!")"""
        schedule_file.close()

    def change_task(self, change_row, change_list, del_mode=False, end_path='/ConfigFile/TimeControl/schedule.csv'):# 需删除则change_list传入''
        schedule_file = open(MAIN_PATH + end_path, 'r', newline='')
        reader = csv.reader(schedule_file)
        reader_list = list(reader)
        schedule_file.close()
        if del_mode:
            if len(reader_list) > 0:
                del reader_list[change_row]
        else:
            reader_list[change_row] = change_list
        schedule_file = open(MAIN_PATH + end_path, 'w', newline='')
        writer = csv.writer(schedule_file)
        writer.writerows(reader_list)
        schedule_file.close()

    def qbtnReset(self):
        self.flag = 1
        self.time_start = datetime.datetime.now()
        self.pbtn.show()
        self.qbtn.hide()

    def pbtnClicked(self):
        self.time_end = datetime.datetime.now()
        print(self.time_end.strftime("%H:%M:%S"))
        self.flag = 2
        input_list = []
        input_list.append(self.task_name)
        input_list.append(self.time_start.strftime("%Y%m%d%H%M%S"))
        input_list.append(self.time_end.strftime("%Y%m%d%H%M%S"))
        if os.path.exists(MAIN_PATH + self.file_path):
            self.add_task(input_list, self.file_path)
        else:
            file = open(MAIN_PATH + self.file_path, 'w')
            file.close()
            self.add_task(input_list, self.file_path)
        #self.pbtn.setText("Start")
        self.time_show = datetime.datetime.strptime("00:00:00", "%H:%M:%S")
        self.pbtn.hide()
        self.qbtn.show()

    def closeEvent(self, QCloseEvent):
        def closeEvent(self, event):
            event.accept()
        try:
            if self.model == 1:
                sys.exit(5)
            elif self.model == 2:
                if self.flag_off == 1:# 非法
                    self.change_task(-1,"",True,end_path="/ConfigFile/TimeControl/"+self.file_now+".csv")
                    #os._exit
                    sys.exit(6)
                else:# 合法
                    #os._exit(7)
                    sys.exit(7)
            else:
                #os._exit(888)
                sys.exit(888)

        except Exception as e:
            print(e)

    def ring_on(self):
        f = wave.open(r"D:\\Python\\Liam\\ConfigFile\\ring.wav", "rb")
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        data = f.readframes(CHUNK)
        while data != '':
            stream.write(data)
            data = f.readframes(CHUNK)
        stream.stop_stream()
        stream.close()
        p.terminate()
        sys.exit()


def run():
    app = QApplication(sys.argv)
    ex = StudyClock()
    #sys.exit(app.exec_())
    #exit_code = app.exec_()
    exit_code = app.exec_()
    print(exit_code)
    if exit_code == 888:
        run()
    else:
        sys.exit(111)


if __name__ == '__main__':
    #app = QApplication(sys.argv)
    #ex = StudyClock()
    #sys.exit(app.exec_())
    run()
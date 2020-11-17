from random import randint
from PyQt5.QtGui import QIntValidator
from Ui_Form import *
from PyQt5 import QtWidgets
from sys import argv, exit

from process_scheduling import ProcessScheduling, PCB


class Demo(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)
        self.ui_init()

    def ui_init(self):
        self.pushButton.clicked.connect(self.run_process)
        self.pushButton_2.clicked.connect(self.run_process_random)
        self.lineEdit_3.setPlaceholderText("1")
        self.lineEdit.setPlaceholderText("0,4;1,6;4,2;3,3;2,5")
        self.lineEdit_2.setPlaceholderText("5")

        validator = QIntValidator(1, 999)
        self.lineEdit_2.setValidator(validator)
        validator_1 = QIntValidator(1, 999)
        self.lineEdit_3.setValidator(validator_1)

        # 测试
        #self.lineEdit.setText("0,4;1,6;4,2;3,3;2,5")
        #self.lineEdit_2.setText("5")
        #self.lineEdit_3.setText("1")

    def run_process(self):
        ps1 = ProcessScheduling()
        ps2 = ProcessScheduling(target=2)
        ps3 = ProcessScheduling(target=3)
        ps4 = ProcessScheduling(target=4)

        input_text_1 = self.lineEdit.text()
        input_text_3 = self.lineEdit_3.text()
        if not input_text_1:
            return -1
        input_list = input_text_1.split(";")
        if not input_list:
            return -2
        for i, input_num in enumerate(input_list):
            sub_list = input_num.split(",")
            print(sub_list)
            if not sub_list:
                return -3
            try:
                ps1.process_list.append(PCB(str(i), int(sub_list[0]), int(sub_list[1]), 0, 1.0, "Wait"))
                ps2.process_list.append(PCB(str(i), int(sub_list[0]), int(sub_list[1]), 0, 1.0, "Wait"))
                ps3.process_list.append(PCB(str(i), int(sub_list[0]), int(sub_list[1]), 0, 1.0, "Wait"))
                ps4.process_list.append(PCB(str(i), int(sub_list[0]), int(sub_list[1]), 0, 1.0, "Wait"))
            except:
                print("ERROR")
                return -4

        ps1.first_come_first_served()
        ps2.short_job_first()
        if input_text_3:
            ps3.RR(int(input_text_3))
        else:
            ps3.RR()
        ps4.highest_response_ratio_next()

        print("ps1.return_text", ps1.return_text)
        self.textBrowser.setPlainText(ps1.return_text)
        self.textBrowser_2.setPlainText(ps2.return_text)
        self.textBrowser_3.setPlainText(ps3.return_text)
        self.textBrowser_4.setPlainText(ps4.return_text)

        self.cursor_1.movePosition(QTextCursor.End)
        self.textBrowser.setTextCursor(self.cursor_1)
        self.cursor_2.movePosition(QTextCursor.End)
        self.textBrowser_2.setTextCursor(self.cursor_2)
        self.cursor_3.movePosition(QTextCursor.End)
        self.textBrowser_3.setTextCursor(self.cursor_3)
        self.cursor_4.movePosition(QTextCursor.End)
        self.textBrowser_4.setTextCursor(self.cursor_4)

    def run_process_random(self):
        ps1 = ProcessScheduling()
        ps2 = ProcessScheduling(target=2)
        ps3 = ProcessScheduling(target=3)
        ps4 = ProcessScheduling(target=4)

        input_text_2 = self.lineEdit_2.text()
        input_text_3 = self.lineEdit_3.text()
        num = 5
        if input_text_2:
            num = int(input_text_2)
        j = -1
        k = 1
        for i in range(num+1):
            p = randint(j+1, j+k)
            q = randint(1, 20)
            ps1.process_list.append(PCB(str(i), p, q, 0, 1.0, "Wait"))
            ps2.process_list.append(PCB(str(i), p, q, 0, 1.0, "Wait"))
            ps3.process_list.append(PCB(str(i), p, q, 0, 1.0, "Wait"))
            ps4.process_list.append(PCB(str(i), p, q, 0, 1.0, "Wait"))
            j = p
            k = randint(1, 10)

        ps1.first_come_first_served()
        ps2.short_job_first()
        if input_text_3:
            ps3.RR(int(input_text_3))
        else:
            ps3.RR()
        ps4.highest_response_ratio_next()

        self.textBrowser.setPlainText(ps1.return_text)
        self.textBrowser_2.setPlainText(ps2.return_text)
        self.textBrowser_3.setPlainText(ps3.return_text)
        self.textBrowser_4.setPlainText(ps4.return_text)

        self.cursor_1.movePosition(QTextCursor.End)
        self.textBrowser.setTextCursor(self.cursor_1)
        self.cursor_2.movePosition(QTextCursor.End)
        self.textBrowser_2.setTextCursor(self.cursor_2)
        self.cursor_3.movePosition(QTextCursor.End)
        self.textBrowser_3.setTextCursor(self.cursor_3)
        self.cursor_4.movePosition(QTextCursor.End)
        self.textBrowser_4.setTextCursor(self.cursor_4)


if __name__ == '__main__':
    app = QtWidgets.QApplication(argv)
    demo = Demo()
    demo.show()
    exit(app.exec_())
from random import randint
from csv import reader


class PCB:
    def __init__(self, id, sub_time, need_time, used_time, state):
        self.id =id
        self.sub_time = sub_time
        self.need_time = need_time
        self.used_time = used_time
        self.state = state

    def running(self):
        print("****当前运行的进程****")
        self.need_time -= 1
        self.used_time += 1
        self.state = "Run"
        self.print_process()

    def to_wait(self):
        self.state = "Wait"

    def to_finish(self):
        self.state = "Finish"

    def print_process(self):
        print("进程号：", str(self.id), " 状态：", self.state, " 提交时间：", self.sub_time, " 已运行时间：",
              self.used_time, " 需要时间：", self.need_time)


class ProcessScheduling:
    def __init__(self):
        self.file = ".//process.csv"
        self.process_list = []
        self.time = 0
        self.ready_queue = []
        self.statistics_list = []
        self.num = 0

    def enter_mode(self, mode=True, num=5):
        self.num = num
        j = randint(1, 5)
        if mode:
            for i in range(num):
                k = j + randint(1, 3)
                self.process_list.append(PCB(str(i), randint(j, k),randint(1, 10),
                                             0, "Wait"))
                j = k
            # 测试用
            #self.process_list.append(PCB("0", 0, 4, 0, "Wait"))
            #self.process_list.append(PCB("1", 1, 6, 0, "Wait"))
            #self.process_list.append(PCB("2", 2, 5, 0, "Wait"))
            #self.process_list.append(PCB("3", 3, 3, 0, "Wait"))
            #self.process_list.append(PCB("4", 4, 2, 0, "Wait"))
        else:
            try:
                file = open(self.file, 'r')
            except:
                print("process.csv 不存在!")
                return -1
            file_reader = reader(file)
            final_list = list(file_reader)
            try:
                for process in final_list:
                    self.process_list.append(PCB(process[0], int(process[1]), int(process[2]), int(process[3]),
                                             process[4]))
            except:
                print("输入格式错误!")
                return -1

    def short_job_first(self):
        while True:
            print("Time: ", self.time, "-", self.time+1)
            copy_list = []
            if self.process_list:
                for process in self.process_list:
                    if process.sub_time != self.time:
                        copy_list.append(process)
                    else:
                        self.ready_queue.append(process)
                self.process_list = copy_list
            if len(self.ready_queue) > 1:
                self.ready_queue.sort(key=lambda x: x.need_time)
            ready_queue_len = len(self.ready_queue)
            if ready_queue_len > 0:
                self.ready_queue[0].running()
                if ready_queue_len > 1:
                    print("****就绪队列中的其他进程****")
                    for i in range(1, ready_queue_len):
                        self.ready_queue[i].print_process()
                if self.ready_queue[0].need_time == 0:
                    self.ready_queue[0].to_finish()
                    print("****进程完成, 完成时间: ", self.time+1, "周转时间: ", self.time+1-self.ready_queue[0].sub_time, "****")
                    list1 = []
                    list1.append(self.ready_queue[0])
                    list1.append(self.time+1)
                    list1.append(self.time+1-self.ready_queue[0].sub_time)
                    self.statistics_list.append(list1)
                    self.ready_queue.remove(self.ready_queue[0])
                else:
                    self.ready_queue[0].to_wait()
            if len(self.ready_queue)==0 and len(self.process_list)==0:
                print("\n****调度结束****")
                break
            else:
                self.time += 1
            print("")
        total_cycling_time = 0
        total_with_right_cycling_time = 0
        for process in self.statistics_list:
            print("进程号: ", process[0].id, "到达时间: ", process[0].sub_time, "服务时间: ", process[0].used_time,
                  "完成时间: ", process[1], "周转时间: ", process[2], "带权周转时间: ", process[2]/process[0].used_time)
            total_cycling_time += process[2]
            total_with_right_cycling_time += process[2]/process[0].used_time
        print("\n平均周转时间: ", total_cycling_time/self.num, "平均带权周转时间: ", total_with_right_cycling_time/self.num)

    def output_list(self):
        for process in self.process_list:
            process.print_process()



if __name__ == '__main__':
    demo = ProcessScheduling()
    if input("输入1随机生成, 输入2文件输入(根目录下的process.csv): ") == "1":
        number = int(input("输入生成的进程数量: "))
        if number > 0:
            demo.enter_mode(mode=True, num=number)
        else:
            exit(0)
    else:
        demo.enter_mode(mode=False)
    for process in demo.process_list:
        process.print_process()
    print("")
    demo.short_job_first()
    input("\n按任意键结束")
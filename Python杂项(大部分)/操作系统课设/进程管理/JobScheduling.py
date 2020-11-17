from random import randint
from csv import reader


class JCB:
    def __init__(self, id, sub_time, need_time, used_time, Rp, state):
        self.id = id
        self.sub_time = sub_time
        self.need_time = need_time
        self.used_time = used_time
        self.Rp = Rp
        self.state = state

    def running(self):
        print("****当前运行的进程****")
        self.need_time -= 1
        self.used_time += 1
        self.state = "Run"
        self.print_job()

    def to_wait(self):
        self.state = "Wait"

    def to_finish(self):
        self.state = "Finish"

    def print_job(self):
        print("作业号: ", str(self.id), " 状态: ", self.state, " 提交时间: ", self.sub_time, " 已运行时间: ",
              self.used_time, " 需要时间: ", self.need_time, " 响应比: ", self.Rp)


class  JobScheduling:
    def __init__(self):
        self.job_list = []
        self.ready_queue = []# 就绪队列
        self.file = "job.csv"
        self.time = 0
        self.statistics_list = []
        self.num = 0

    def select_mode(self, mode=True, num=5):
        self.num = num
        j = randint(1, 5)
        if mode:
            for i in range(num):
                k = j + randint(1, 3)
                self.job_list.append(JCB(str(i), randint(j, k), randint(1, 10), 0, 1.0, "Wait"))
                j = k
            # 测试
            #self.job_list.append(JCB("0", 0, 4, 0, 1.0, "Wait"))
            #self.job_list.append(JCB("1", 1, 6, 0, 1.0, "Wait"))
            #self.job_list.append(JCB("2", 2, 5, 0, 1.0, "Wait"))
            #self.job_list.append(JCB("3", 3, 3, 0, 1.0, "Wait"))
            #self.job_list.append(JCB("4", 4, 2, 0, 1.0, "Wait"))
        else:
            try:
                file = open(self.file, 'r')
            except:
                print("job.csv 不存在!")
                return -1
            file_reader = reader(file)
            final_list = list(file_reader)
            try:
                for job in final_list:
                    self.job_list.append(JCB(job[0], int(job[1]), int(job[2]), int(job[3]), float(job[4]), job[5]))
            except:
                print("输入格式错误!")
                return -1

    def first_come_first_served(self):
        self.job_list.sort(key=(lambda x:x.sub_time))
        while True:
            print("Time: ", self.time, "-", self.time+1)
            copy_list = []
            if self.job_list:
                for job in self.job_list:
                    if job.sub_time == self.time:
                        self.ready_queue.append(job)
                    else:
                        copy_list.append(job)
                self.job_list = copy_list
            ready_queue_len = len(self.ready_queue)
            if ready_queue_len > 0:
                self.ready_queue[0].running()
                if ready_queue_len > 1:
                    print("****就绪队列中的其他作业****")
                    for i in range(1, ready_queue_len):
                        self.ready_queue[i].print_job()
                if self.ready_queue[0].need_time == 0:
                    self.ready_queue[0].to_finish()
                    print("****作业完成, 完成时间: ", self.time + 1, "周转时间: ", self.time + 1 - self.ready_queue[0].sub_time,
                          "****")
                    list1 = []
                    list1.append(self.ready_queue[0])
                    list1.append(self.time+1)
                    list1.append(self.time+1-self.ready_queue[0].sub_time)
                    self.statistics_list.append(list1)
                    self.ready_queue.remove(self.ready_queue[0])
            if len(self.ready_queue)==0 and len(self.job_list)==0:
                print("\n****调度结束****")
                break
            else:
                self.time += 1
            print("")

        total_cycling_time = 0
        total_with_right_cycling_time = 0
        for process in self.statistics_list:
            print("作业号: ", process[0].id, "到达时间: ", process[0].sub_time, "服务时间: ", process[0].used_time,
                  "完成时间: ", process[1], "周转时间: ", process[2], "带权周转时间: ", process[2] / process[0].used_time)
            total_cycling_time += process[2]
            total_with_right_cycling_time += process[2] / process[0].used_time
        print("\n平均周转时间: ", total_cycling_time / self.num, "平均带权周转时间: ", total_with_right_cycling_time / self.num)
        return("\nFCFS:\n平均周转时间: ", total_cycling_time / self.num, "平均带权周转时间: ", total_with_right_cycling_time / self.num)

    def highest_response_ratio_next(self):
        # 优先权等于 等待时间+要求服务时间 / 要求服务时间
        while True:
            print("Time: ", self.time, "-", self.time+1)
            copy_list = []
            if self.job_list:
                for job in self.job_list:
                    if job.sub_time == self.time:
                        self.ready_queue.append(job)
                    else:
                        copy_list.append(job)
                self.job_list = copy_list
            #    self.ready_queue.sort(key=lambda x: x.Rp, reverse=True)
            ready_queue_len = len(self.ready_queue)
            if ready_queue_len > 0:
                self.ready_queue[0].running()
                if ready_queue_len > 1:
                    print("****就绪队列中的其他作业****")
                    for i in range(1, ready_queue_len):
                        self.ready_queue[i].print_job()
                if self.ready_queue[0].need_time == 0:
                    self.ready_queue[0].to_finish()
                    print("****作业完成, 完成时间: ", self.time + 1, "周转时间: ", self.time + 1 - self.ready_queue[0].sub_time,
                          "****")
                    list1 = []
                    list1.append(self.ready_queue[0])
                    list1.append(self.time + 1)
                    list1.append(self.time + 1 - self.ready_queue[0].sub_time)
                    self.statistics_list.append(list1)
                    self.ready_queue.remove(self.ready_queue[0])
                    for ready_job in self.ready_queue:
                        wait_time = self.time - ready_job.sub_time - ready_job.used_time + 1
                        #print(ready_job.id, "test ready_queue, wait_time:", wait_time)
                        ready_job.Rp = (wait_time + ready_job.need_time) / ready_job.need_time
                        #print(ready_job.id, "test ready_queue, Rp: ", ready_job.Rp)

                    if self.ready_queue:
                        self.ready_queue.sort(key=lambda x: x.Rp, reverse=True)

                    #if len(self.ready_queue) > 1:
                    #    self.ready_queue.sort(key=lambda x: x.Rp, reverse=True)
                else:
                    self.ready_queue[0].to_wait()
                    for ready_job in self.ready_queue:
                        wait_time = self.time - ready_job.sub_time - ready_job.used_time + 1
                        #print(ready_job.id, "test ready_queue, wait_time:", wait_time)
                        ready_job.Rp = (wait_time + ready_job.need_time) / ready_job.need_time
            if not self.ready_queue and not self.job_list:
                print("\n****调度结束****")
                break
            else:
                self.time += 1
            print("")

        total_cycling_time = 0
        total_with_right_cycling_time = 0
        for process in self.statistics_list:
            print("作业号: ", process[0].id, "到达时间: ", process[0].sub_time, "服务时间: ", process[0].used_time,
                  "完成时间: ", process[1], "周转时间: ", process[2], "带权周转时间: ", process[2] / process[0].used_time)
            total_cycling_time += process[2]
            total_with_right_cycling_time += process[2] / process[0].used_time
        print("\n平均周转时间: ", total_cycling_time / self.num, "平均带权周转时间: ", total_with_right_cycling_time / self.num)
        return("\nHRRN:\n平均周转时间: ", total_cycling_time / self.num, "平均带权周转时间: ", total_with_right_cycling_time / self.num)


if __name__ == '__main__':
    demo = JobScheduling()
    demo_1 = JobScheduling()
    if input("输入1随机生成, 输入2文件输入(根目录下的job.csv): ") == "1":
        number = int(input("输入生成的进程数量: "))
        if number > 0:
            demo.select_mode(mode=True, num=number)
            demo_1.select_mode(mode=True, num=number)
        else:
            exit(0)
    else:
        demo.select_mode(mode=False)
        demo_1.select_mode(mode=False)

    for job in demo.job_list:
        job.print_job()

    print("FCFS\n")
    demo.first_come_first_served()

    print("\nHRRN\n")
    demo_1.highest_response_ratio_next()
    input("\n按回车结束")
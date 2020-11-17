class PCB:
    def __init__(self, id, sub_time, need_time, used_time, Rp, state):
        self.id =id
        self.sub_time = sub_time
        self.need_time = need_time
        self.used_time = used_time
        self.Rp = Rp
        self.state = state

    def running(self):
        #print("****当前运行的进程****")
        self.need_time -= 1
        self.used_time += 1
        self.state = "Run"
        return "****当前运行的进程****\n" + self.print_process()

    def to_wait(self):
        self.state = "Wait"

    def to_finish(self):
        self.state = "Finish"

    def print_process(self, flag=True):
        if flag:
            return "进程号：" + self.id + " 状态：" + self.state + " 提交时间：" + str(self.sub_time) + " 已运行时间：" + \
                   str(self.used_time) + " 需要时间：" + str(self.need_time) +  "\n"
        else:
            return "进程号：" + self.id + " 状态：" + self.state + " 提交时间：" + str(self.sub_time) + " 已运行时间：" + \
                   str(self.used_time) + " 需要时间：" + str(self.need_time) + " 响应比: " + str(self.Rp) + "\n"


class ProcessScheduling:
    def __init__(self, target=1, ):
        self.process_list = []
        self.time = 0
        self.ready_queue = []
        self.statistics_list = []
        self.num = 0

        self.target = self.first_come_first_served
        if target == 2:
            self.target = self.short_job_first
        elif target == 3:
            self.target = self.RR
        elif target == 4:
            self.target = self.highest_response_ratio_next
        self.return_text = ""

    def first_come_first_served(self):
        for process in self.process_list:
            self.return_text += "进程号: " + process.id + " 提交时间: " + str(process.sub_time) + " 已运行时间: " + \
                                str(process.used_time) + " 需要时间: " + str(process.need_time) + "\n"
        self.num = len(self.process_list)
        self.process_list.sort(key=(lambda x:x.sub_time))
        while True:
            self.return_text += "\nTime: " + str(self.time) + " - " + str(self.time+1) + "\n"
            copy_list = []
            if self.process_list:
                for process in self.process_list:
                    if process.sub_time == self.time:
                        self.ready_queue.append(process)
                    else:
                        copy_list.append(process)
                self.process_list = copy_list
            ready_queue_len = len(self.ready_queue)
            if ready_queue_len > 0:
                self.return_text += self.ready_queue[0].running()
                if ready_queue_len > 1:
                    self.return_text += "****就绪队列中的其他进程****\n"
                    for i in range(1, ready_queue_len):
                        self.return_text += self.ready_queue[i].print_process()
                if self.ready_queue[0].need_time == 0:
                    self.ready_queue[0].to_finish()
                    self.return_text += "****进程 " + self.ready_queue[0].id + " 完成****\n" + "完成时间: " + str(self.time + 1) + \
                                        " 周转时间: " + str(self.time + 1 - self.ready_queue[0].sub_time) + "\n"
                    list1 = []
                    list1.append(self.ready_queue[0])
                    list1.append(self.time + 1)
                    list1.append(self.time + 1 - self.ready_queue[0].sub_time)
                    self.statistics_list.append(list1)
                    self.ready_queue.remove(self.ready_queue[0])
            if len(self.ready_queue)==0 and len(self.process_list)==0:
                self.return_text += "\n****调度结束****\n"
                break
            else:
                self.time += 1
        total_cycling_time = 0
        total_with_right_cycling_time = 0
        self.statistics_list.sort(key=(lambda x:x[0].sub_time))
        for process in self.statistics_list:
            self.return_text += "作业号: " + str(process[0].id) + " 到达时间: " + str(process[0].sub_time) + " 服务时间: " + \
                                str(process[0].used_time) + " 完成时间: " + str(process[1]) + " 周转时间: " + \
                                str(process[2]) + " 带权周转时间: " + str(process[2] / process[0].used_time) + "\n"
            total_cycling_time += process[2]
            total_with_right_cycling_time += process[2] / process[0].used_time
        self.return_text += "FCFS:\n平均周转时间: " + str(total_cycling_time / self.num) + " 平均带权周转时间: " + \
                            str(total_with_right_cycling_time / self.num) + "\n"


    def short_job_first(self):
        for process in self.process_list:
            self.return_text += "进程号: " + process.id + " 提交时间: " + str(process.sub_time) + " 已运行时间: " + \
                                str(process.used_time) + " 需要时间: " + str(process.need_time) + "\n"
        self.num = len(self.process_list)
        while True:
            self.return_text += "\nTime: " + str(self.time) + " - " + str(self.time + 1) + "\n"
            copy_list = []
            if self.process_list:
                for process in self.process_list:
                    if process.sub_time == self.time:
                        self.ready_queue.append(process)
                    else:
                        copy_list.append(process)
                self.process_list = copy_list
            if len(self.ready_queue) > 1:
                self.ready_queue.sort(key=lambda x: x.need_time)
            ready_queue_len = len(self.ready_queue)
            if ready_queue_len > 0:
                self.return_text += self.ready_queue[0].running()
                if ready_queue_len > 1:
                    self.return_text += "****就绪队列中的其他进程****\n"
                    for i in range(1, ready_queue_len):
                        self.return_text += self.ready_queue[i].print_process()
                if self.ready_queue[0].need_time == 0:
                    self.ready_queue[0].to_finish()
                    self.return_text += "****进程 " + self.ready_queue[0].id + " 完成****\n" + "完成时间: " + str(
                        self.time + 1) + " 周转时间: " + str(self.time + 1 - self.ready_queue[0].sub_time) + "\n"
                    list1 = []
                    list1.append(self.ready_queue[0])
                    list1.append(self.time + 1)
                    list1.append(self.time + 1 - self.ready_queue[0].sub_time)
                    self.statistics_list.append(list1)
                    self.ready_queue.remove(self.ready_queue[0])
                #else:
                #    self.ready_queue[0].to_wait()
            if len(self.ready_queue) == 0 and len(self.process_list) == 0:
                self.return_text += "\n****调度结束****\n"
                break
            else:
                self.time += 1
        total_cycling_time = 0
        total_with_right_cycling_time = 0
        self.statistics_list.sort(key=(lambda x:x[0].sub_time))
        for process in self.statistics_list:
            self.return_text += "作业号: " + str(process[0].id) + " 到达时间: " + str(process[0].sub_time) + " 服务时间: " + \
                                str(process[0].used_time) + " 完成时间: " + str(process[1]) + " 周转时间: " + \
                                str(process[2]) + " 带权周转时间: " + str(process[2] / process[0].used_time) + "\n"
            total_cycling_time += process[2]
            total_with_right_cycling_time += process[2] / process[0].used_time
        self.return_text += "SJF:\n平均周转时间: " + str(total_cycling_time / self.num) + " 平均带权周转时间: " + \
                            str(total_with_right_cycling_time / self.num) + "\n"

    def RR(self, q=1):
        pop_process = None
        run_time = 0
        self.num = len(self.process_list)
        for process in self.process_list:
            self.return_text += "进程号: " + process.id + " 提交时间: " + str(process.sub_time) + " 已运行时间: " + \
                                str(process.used_time) + " 需要时间: " + str(process.need_time) + " 响应比: " + str(
                process.Rp) + " 时间片长度: " + str(q) + "\n"
        while True:
            self.return_text += "\nTime: " + str(self.time) + " - " + str(self.time + 1) + "\n"
            copy_list = []
            if self.process_list:
                for process in self.process_list:
                    # 先将提交的进程插入队列, 再将弹出的进程插入后面
                    if process.sub_time == self.time:
                        self.ready_queue.append(process)
                    else:
                        copy_list.append(process)
                self.process_list = copy_list
            if pop_process:
                self.ready_queue.append(pop_process)
            ready_queue_len = len(self.ready_queue)
            if ready_queue_len > 0:
                self.return_text += self.ready_queue[0].running()
                run_time += 1
                if ready_queue_len > 1:
                    self.return_text += "****就绪队列中的其他进程****\n"
                    for i in range(1, ready_queue_len):
                        self.return_text += self.ready_queue[i].print_process()
                if self.ready_queue[0].need_time == 0:
                    self.ready_queue[0].to_finish()
                    self.return_text += "****进程 " + self.ready_queue[0].id + " 完成****\n"+ "完成时间: " + str(self.time + 1) + \
                                        " 周转时间: " + str(self.time + 1 - self.ready_queue[0].sub_time) + "\n"
                    list1 = []
                    list1.append(self.ready_queue[0])
                    list1.append(self.time + 1)
                    list1.append(self.time + 1 - self.ready_queue[0].sub_time)
                    self.statistics_list.append(list1)
                    self.ready_queue.pop(0)
                    pop_process = None
                    run_time = 0
                else:
                    # 判断时间片有没有用完
                    if run_time < q:# 没用完
                        pop_process = None
                    else:# 用完
                        pop_process = self.ready_queue.pop(0)
                        run_time = 0
            if not self.ready_queue and not self.process_list:
                if not pop_process:
                    self.return_text += "\n****调度结束****\n"
                    break
                else:
                    self.time += 1
            else:
                self.time += 1
        total_cycling_time = 0
        total_with_right_cycling_time = 0
        self.statistics_list.sort(key=(lambda x:x[0].sub_time))
        for process in self.statistics_list:
            self.return_text += "作业号: " + str(process[0].id) + " 到达时间: " + str(process[0].sub_time) + " 服务时间: " + \
                                str(process[0].used_time) + " 完成时间: " + str(process[1]) + " 周转时间: " + \
                                str(process[2]) + " 带权周转时间: " + str(process[2] / process[0].used_time) + "\n"
            total_cycling_time += process[2]
            total_with_right_cycling_time += process[2] / process[0].used_time
        self.return_text += "RR:\n平均周转时间: " + str(total_cycling_time / self.num) + " 平均带权周转时间: " + \
                            str(total_with_right_cycling_time / self.num) + "\n"



    def highest_response_ratio_next(self):
        self.num = len(self.process_list)
        for process in self.process_list:
            self.return_text += "进程号: " + process.id + " 提交时间: " + str(process.sub_time) + " 已运行时间: " + \
                                str(process.used_time) + " 需要时间: " + str(process.need_time) + " 响应比: " + str(process.Rp) + "\n"
        while True:
            self.return_text += "\nTime: " + str(self.time) + " - " + str(self.time + 1) + "\n"
            copy_list = []
            if self.process_list:
                for process in self.process_list:
                    if process.sub_time == self.time:
                        self.ready_queue.append(process)
                    else:
                        copy_list.append(process)
                self.process_list = copy_list
            ready_queue_len = len(self.ready_queue)
            if ready_queue_len > 0:
                self.return_text += self.ready_queue[0].running()
                if ready_queue_len > 1:
                    self.return_text += "****就绪队列中的其他进程****\n"
                    for i in range(1, ready_queue_len):
                        self.return_text += self.ready_queue[i].print_process(False)
                if self.ready_queue[0].need_time == 0:
                    self.ready_queue[0].to_finish()
                    self.return_text += "****进程 " + self.ready_queue[0].id + " 完成****\n" + " 完成时间: " + str(
                        self.time + 1) + " 周转时间: " + str(self.time + 1 - self.ready_queue[0].sub_time) + "\n"
                    list1 = []
                    list1.append(self.ready_queue[0])
                    list1.append(self.time + 1)
                    list1.append(self.time + 1 - self.ready_queue[0].sub_time)
                    self.statistics_list.append(list1)
                    self.ready_queue.remove(self.ready_queue[0])
                    for ready_process in self.ready_queue:
                        wait_time = self.time - ready_process.sub_time - ready_process.used_time + 1
                        ready_process.Rp = (wait_time + ready_process.need_time) / ready_process.need_time
                    if self.ready_queue:
                        self.ready_queue.sort(key=lambda x: x.Rp, reverse=True)
                else:
                    for ready_job in self.ready_queue:
                        wait_time = self.time - ready_job.sub_time - ready_job.used_time + 1
                        ready_job.Rp = (wait_time + ready_job.need_time) / ready_job.need_time
            if len(self.ready_queue) == 0 and len(self.process_list) == 0:
                self.return_text += "\n****调度结束****\n"
                break
            else:
                self.time += 1
        total_cycling_time = 0
        total_with_right_cycling_time = 0
        self.statistics_list.sort(key=(lambda x:x[0].sub_time))
        for process in self.statistics_list:
            self.return_text += "作业号: " + str(process[0].id) + " 到达时间: " + str(process[0].sub_time) + " 服务时间: " + \
                                str(process[0].used_time) + " 完成时间: " + str(process[1]) + " 周转时间: " + \
                                str(process[2]) + " 带权周转时间: " + str(process[2] / process[0].used_time) + "\n"
            total_cycling_time += process[2]
            total_with_right_cycling_time += process[2] / process[0].used_time
        self.return_text += "HRRN:\n平均周转时间: " + str(total_cycling_time / self.num) + " 平均带权周转时间: " + \
                            str(total_with_right_cycling_time / self.num) + "\n"

"""#测试
if __name__ == '__main__':
    ps = ProcessScheduling()
    ps.process_list.append(PCB("0", 0, 4, 0, 1.0, "Wait"))
    ps.process_list.append(PCB("1", 1, 6, 0, 1.0, "Wait"))
    ps.process_list.append(PCB("2", 2, 5, 0, 1.0, "Wait"))
    ps.process_list.append(PCB("3", 3, 3, 0, 1.0, "Wait"))
    ps.process_list.append(PCB("4", 4, 2, 0, 1.0, "Wait"))
    #ps.first_come_first_served()
    #ps.highest_response_ratio_next()
    ps.RR(4)
    print(ps.return_text)
"""
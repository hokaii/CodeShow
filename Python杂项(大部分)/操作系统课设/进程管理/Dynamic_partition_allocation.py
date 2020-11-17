# 首次适应算法和最佳适应算法的动态分区分配过程和回收过程
class Partition:
    def __init__(self, size, start_address, state):
        self.size = size# 空间大小
        self.start_address = start_address# 起始地址
        self.state = state# 状态
        self.work_id = 0# 作业ID

    def print_partition(self):
        if self.state:
            return("分区始址: " + str(self.start_address) + " 分区大小: "+ str(self.size)+ " 状态: "+ " 空闲\n")
        else:
            return ("分区始址: "+ str(self.start_address)+ " 分区大小: "+ str(self.size)+ " 状态: "+ " 已分配"+ " 作业号: "+ str(self.work_id) + "\n")


class DistributedSimulate:
    def __init__(self, target=1):
        self.total_size = 640
        self.partition_list = []
        self.request_list = []
        self.mini_size = 10
        self.target = self.first_fit
        if target == 2:
            self.target = self.best_fit
        elif target == 3:
            self.target = self.worst_fit
        self.sign_pointer = 0
        self.return_text = ""
        self.log_dict = {'success':0, 'failure': 0, 'compact': 0, 'num': 0, 'debris': 0}
        self.log_list = []
        self.partition_list.append(Partition(self.total_size, 0, True))

    def first_fit(self, size, job_id, num=1):
        # 碎片统计
        for partition in self.partition_list:
            if partition.size <= 10 and partition.state and [partition.start_address, partition.size] not in self.log_list:
                self.log_dict['debris'] += 1
                self.log_list.append([partition.start_address, partition.size])

        self.log_dict['num'] += 1
        self.return_text += "作业号: " + str(job_id) + " 申请: " + str(size) + "\n"
        self.partition_list.sort(key=(lambda x: x.start_address))
        flag = False
        for partition in self.partition_list:
            if partition.work_id == job_id:
                self.return_text += "不允许重复申请\n"
                self.return_text += "------------------------\n"
                return 0
        for partition in self.partition_list:
            if partition.state:
                if size <= partition.size:
                    #切割
                    if partition.size - size >= self.mini_size:
                        divide_partition = Partition(partition.size-size, partition.start_address+size, True)
                        partition.size = size
                        partition.state = False
                        partition.work_id = job_id
                        self.partition_list.append(divide_partition)
                        flag = True
                        break
                    # 不用切割
                    else:
                        partition.state = False
                        partition.work_id = job_id
                        flag = True
                        break
                else:
                    continue
        free_size = 0
        for partition in self.partition_list:
            if partition.state:
                free_size += partition.size
        # 测试
        self.return_text += "剩余内存: " + str(free_size) + "\n"
        if flag:
            self.partition_list.sort(key=(lambda x: x.start_address))
            self.return_text += "分配成功! \n"
            for partition in self.partition_list:
                self.return_text += partition.print_partition()
            self.return_text += "------------------------\n"
            self.log_dict['success'] += 1
            return True
        elif num==1 and free_size >= size:
            self.compact()
            self.log_dict['compact'] += 1
            self.first_fit(size, job_id, num=2)
        else:
            self.log_dict['failure'] += 1
            self.return_text += "内存不足, 分配失败\n"
            self.return_text += "------------------------\n"
            return False

    def best_fit(self, size, job_id, num=1):
        for partition in self.partition_list:
            if partition.size <= 10 and partition.state and [partition.start_address, partition.size] not in self.log_list:
                self.log_dict['debris'] += 1
                self.log_list.append([partition.start_address, partition.size])

        self.log_dict['num'] += 1
        self.return_text += "作业号: " + str(job_id) + " 申请: " + str(size) + "\n"
        self.partition_list.sort(key=(lambda x:x.size))
        flag = False
        for partition in self.partition_list:
            if partition.work_id == job_id:
                self.return_text += "不允许重复申请\n"
                self.return_text += "------------------------\n"
                return 0
        for partition in self.partition_list:
            if partition.state:
                if size <= partition.size:
                    if partition.size - size >= self.mini_size:
                        divide_partition = Partition(partition.size - size, partition.start_address + size, True)
                        partition.size = size
                        partition.state = False
                        partition.work_id = job_id
                        self.partition_list.append(divide_partition)
                        flag = True
                        break
                    else:
                        partition.state = False
                        partition.work_id = job_id
                        flag = True
                        break
                else:
                    continue
        free_size = 0
        for partition in self.partition_list:
            if partition.state:
                free_size += partition.size
        self.return_text += "剩余内存: " + str(free_size) + "\n"
        if flag:
            self.partition_list.sort(key=(lambda x: x.start_address))
            self.return_text += "分配成功! \n"
            for partition in self.partition_list:
                self.return_text += partition.print_partition()
            self.return_text += "------------------------\n"
            self.log_dict['success'] += 1
        elif num==1 and free_size >= size:
            self.compact()
            self.log_dict['compact'] += 1
            self.best_fit(size, job_id, num=2)
        else:
            self.return_text += "内存不足, 分配失败\n"
            self.log_dict['failure'] += 1
            self.return_text += "------------------------\n"

    def worst_fit(self, size, job_id, num=1):
        for partition in self.partition_list:
            if partition.size <= 10 and partition.state and [partition.start_address, partition.size] not in self.log_list:
                self.log_dict['debris'] += 1
                self.log_list.append([partition.start_address, partition.size])

        self.log_dict['num'] += 1
        self.return_text += "作业号: " + str(job_id) + " 申请: " + str(size) + "\n"
        self.partition_list.sort(key=(lambda x: x.size), reverse=True)
        flag = False
        for partition in self.partition_list:
            if partition.work_id == job_id:
                self.return_text += "不允许重复申请\n"
                self.return_text += "------------------------\n"
                return 0
        for partition in self.partition_list:
            if partition.state:
                if size <= partition.size:
                    if partition.size - size >= self.mini_size:
                        divide_partition = Partition(partition.size - size, partition.start_address + size, True)
                        partition.size = size
                        partition.state = False
                        partition.work_id = job_id
                        self.partition_list.append(divide_partition)
                        flag = True
                        break
                    else:
                        partition.state = False
                        partition.work_id = job_id
                        flag = True
                        break
                else:
                    continue
        free_size = 0
        for partition in self.partition_list:
            if partition.state:
                free_size += partition.size
        self.return_text += "剩余内存: " + str(free_size) + "\n"
        if flag:
            self.partition_list.sort(key=(lambda x: x.start_address))
            self.return_text += "分配成功!\n"
            for partition in self.partition_list:
                self.return_text += partition.print_partition()
            self.return_text += "------------------------\n"
            self.log_dict['success'] += 1
        elif num == 1 and free_size >= size:
            self.compact()
            self.log_dict['compact'] += 1
            self.worst_fit(size, job_id, num=2)
        else:
            self.log_dict['failure'] += 1
            self.return_text += "内存不足, 分配失败\n"
            self.return_text += "------------------------\n"

    def free(self, job_id, free_size=100000):
        # 不输入free_size默认释放整个作业
        self.return_text += "回收作业号: " + str(job_id) + "回收大小: " + str(free_size) + "\n"
        flag = False
        flag1 = False
        for i in range(len(self.partition_list)):
            if self.partition_list[i].work_id == job_id:
                if free_size >= self.partition_list[i].size:
                    # 后面也是空闲
                    if i < len(self.partition_list) - 1 and self.partition_list[i + 1].state:
                        self.partition_list[i].size += self.partition_list[i + 1].size
                        self.partition_list[i].state = True
                        self.partition_list.remove(self.partition_list[i + 1])
                        flag = True
                    # 前面是空闲
                    if i > 0 and self.partition_list[i - 1].state:
                        self.partition_list[i - 1].size += self.partition_list[i].size
                        self.partition_list.remove(self.partition_list[i])
                        flag = True
                    if flag == False:
                        self.partition_list[i].state = True
                    flag1 = True
                    break
                else:
                    self.partition_list[i].size -= free_size
                    if i < len(self.partition_list) - 1 and self.partition_list[i + 1].state:
                        self.partition_list[i+1].start_address -= free_size
                        self.partition_list[i+1].size += free_size
                    else:
                        partition = Partition(free_size,self.partition_list[i].start_address+self.partition_list[i].size,True)
                        self.partition_list.append(partition)
                        #print("free size!!!!")
                        self.partition_list.sort(key=lambda x: x.start_address)
                    flag1 = True
                    break
        if flag1:
            self.return_text += "回收成功!\n"
            self.partition_list.sort(key=(lambda x:x.start_address))
            for partition in self.partition_list:
                self.return_text += partition.print_partition()
        else:
            self.return_text += "在内存空间中找不到该作业号!\n"
        self.return_text += "------------------------\n"


    def compact(self):
        self.return_text += "进行紧凑处理\n"
        self.partition_list.sort(key=(lambda x:x.start_address))
        i = 0
        length = len(self.partition_list)
        while i < length:
            if self.partition_list[i].state:
                if i < len(self.partition_list) - 1:
                    if not self.partition_list[i + 1].state:
                        self.partition_list[i + 1].start_address = self.partition_list[i].start_address
                        self.partition_list[i].start_address += self.partition_list[i + 1].size
                        self.partition_list.sort(key=(lambda x: x.start_address))
                    else:
                        self.partition_list[i].size += self.partition_list[i + 1].size
                        del self.partition_list[i + 1]
                        self.partition_list.sort(key=(lambda x: x.start_address))
                        i -= 1
                else:
                    break
            i += 1
        for partition in self.partition_list:
            self.return_text += partition.print_partition()
        self.return_text += "紧凑完成!"

    def main(self):
        demo = DistributedSimulate()


"""
if __name__ == '__main__':
    demo = DistributedSimulate()

    demo_1 = DistributedSimulate()
    demo_1.target = demo_1.best_fit

    demo_2 = DistributedSimulate()
    demo_2.target = demo_2.worst_fit
"""
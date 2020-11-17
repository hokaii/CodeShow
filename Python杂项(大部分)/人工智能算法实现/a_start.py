
class node:
    def __init__(self):
        self.tag = None
        self.f = None
        self.g = None
        self.h = None
        self.order = None
        self.name = None
        self.nextNode = None

class a_star:
    def __init__(self):
        self.open = []
        self.close = []

    # 寻找E节点函数，如果找到E，返回true，否则返回false
    def findE(self):
        if self.close:
            if self.close[-1].name == 'E':
                return True
            else:
                return False
        else:
            return False


    # 打印Close表中的所有节点，输出到控制台，同时显示到达每个节点的耗散值
    def print_close(self):
        if not self.close:
            print("find no nodes error!")
            return
        for close_node in self.close:
            print(close_node.name, close_node.h)

    # 将寻找到的符合条件的节点加入到Open表中
    def openAdd(self, node_p):
        self.open.append(node_p)

    # 在Open表中所有节点中找到耗散值与启发值之和最小的节点，同时将该节点从Open表中删除，并返回列表
    def find_min(self):
        del_list = []
        """
        if not self.open:
            print("test5")
            return False"""
        del_num = 0
        min = self.open[0].f + self.open[0].h
        #min_node = self.open[0]
        for i in range(len(self.open)):
            if min > self.open[i].f + self.open[i].h:
                min = self.open[i].f + self.open[i].h
                #min_node = self.open[i]
                del_num = i
        #self.open.remove(min_node)
        print(del_num, len(self.open))
        del_list = self.open[del_num:len(self.open)]
        for i in range(del_num, len(self.open)):
            print("test6")
            self.open = self.open[0:del_num-1]
        print("test4 len(del_list)", len(del_list))
        #return del_list
        for i in range(len(del_list)):
            self.close.append(del_list[i])

    # 将从find_min函数中返回的节点加入到Close表的结尾
    def closeAdd(self, add_list):
        for i in range(len(add_list)):
            self.close.append(add_list[i])

if __name__ == '__main__':
    graph = [[-1, -1, -1, -1, -1, -1, -1, -1, -1],[-1, -1, -1, -1, -1, -1, -1, -1, -1],[-1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1],[-1, -1, -1, -1, -1, -1, -1, -1, -1],[-1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1],[-1, -1, -1, -1, -1, -1, -1, -1, -1],[-1, -1, -1, -1, -1, -1, -1, -1, -1]]
    graph[0][1] = 0
    graph[1][2] = 3
    graph[2][1] = 3
    graph[2][3] = 4
    graph[3][2] = 4
    graph[3][4] = 8
    graph[4][3] = 8
    graph[4][5] = 2
    graph[5][4] = 2
    graph[1][8] = 4
    graph[8][1] = 4
    graph[2][8] = 5
    graph[8][2] = 5
    graph[7][8] = 2
    graph[8][7] = 2
    graph[3][7] = 3
    graph[7][3] = 3
    graph[4][7] = 8
    graph[7][4] = 8
    graph[6][7] = 4
    graph[7][6] = 4
    graph[4][6] = 3
    graph[6][4] = 3
    star = a_star()
    node_list = []
    for i in range(9):
        node_add = node()
        node_list.append(node_add)
    node_list[0].h = 100
    node_list[1].h = 15
    node_list[1].name = 'A'
    node_list[2].h = 14
    node_list[2].name = 'B'
    node_list[3].h = 10
    node_list[3].name = 'C'
    node_list[4].h = 2
    node_list[4].name = 'D'
    node_list[5].h = 0
    node_list[5].name = 'E'
    node_list[6].h = 5
    node_list[6].name = 'F'
    node_list[7].h = 9
    node_list[7].name = 'G'
    node_list[8].h = 3
    node_list[8].name = 'H'
    for i in range(9):
        node_list[i].order = i
        node_list[i].f = 0
        node_list[i].tag = 0

    #star.open.append(node_list[0])
    for node_1 in node_list:
        star.open.append(node_1)
    #min_node = star.open[0]
    min_node = node_list[0]

    print("test2", star.findE())
    min_list = []
    while not star.findE():
        print("test1")
        for i in range(9):
            if (graph[min_node.order][node_list[i].order] == -1) or (node_list[i].tag == 1):
                continue
            else:
                graph[min_node.order][node_list[i].order] = -1
                node_list[i].f = min_node.f + graph[min_node.order][node_list[i].order]
                star.openAdd(node_list[i])
        print("for end find_min begin")
        min_list = star.find_min()
        print(type(min_list))
        print("find_min end close_add begin")
        #star.closeAdd(min_list)
    star.print_close()
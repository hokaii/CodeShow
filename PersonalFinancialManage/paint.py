#-*- coding:utf-8 -*-
import datetime

from pyecharts import Pie


# 绘图类
class paint:
    def __init__(self):
        self.path_1 = './01.png'
        self.path_2 = './02.png'

    def main(self, num, list):
        arrt1 = []
        value1 = []
        arrt2 = []
        value2 = []
        for i in range(num):
            arrt1.append(list[i]["income_type"])
            value1.append(list[i]["income_num"])
        for j in range(num, len(list)):
            arrt2.append(list[j]["pay_type"])
            value2.append(list[j]["pay_num"])
        pie_1 = Pie("收入")
        pie_2 = Pie("支出")

        pie_1.add("收入", arrt1, value1, is_label_show=True,
                   label_pos="inside", label_text_color="#fff")
        pie_2.add("支出", arrt2, value2, is_label_show=True,
                  label_pos="inside", label_text_color="#fff")
        pie_1.render(path=self.path_1)
        pie_2.render(path=self.path_2)
        return self.path_1, self.path_2


# 测试
if __name__ == '__main__':
    show_list = [{'income_id': 2, 'user_id': '1', 'income_time': datetime.datetime(2020, 1, 5, 16, 13, 43), 'income_type': '理财', 'income_name': '工资到账', 'income_num': 5001, 'income_remark': None}, {'pay_id': 1, 'user_id': '1', 'pay_time': datetime.datetime(2020, 1, 5, 14, 2, 11), 'pay_type': '购物', 'pay_name': '小超市购物', 'pay_num': 20, 'pay_remark': ''}, {'pay_id': 2, 'user_id': '1', 'pay_time': datetime.datetime(2020, 1, 6, 0, 0), 'pay_type': '缴费', 'pay_name': '水电缴费', 'pay_num': 90, 'pay_remark': '下个月记得交'}, {'pay_id': 3, 'user_id': '1', 'pay_time': datetime.datetime(2020, 1, 3, 0, 0), 'pay_type': '线下', 'pay_name': '购买水果', 'pay_num': 45, 'pay_remark': ''}]
    num = 1
    p = paint()
    print(p.main(num, show_list))

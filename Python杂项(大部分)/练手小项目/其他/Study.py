import csv
import random
import requests
import urllib3
import os
from PIL import Image
from bs4 import BeautifulSoup


class ReciteWord:
    def __init__(self):
        self.info = {}
        self.word_list = []
        self.recite_list = []
        self.__initialize()

    def run(self, number=30, recite=True, min_num=0):
        if number < 5:
            print("[recite_word-INFO]: The number of recitations must grater than 10")
            return
        reviewed_num = 0
        for i in range(10):
            if i < min_num:
                continue
            if reviewed_num == number:
                break
            for row in self.word_list:
                if reviewed_num == number:
                    break
                if row[4] == str(i):
                    to_check = row[2].split(".")
                    k = 0
                    while k < len(to_check):
                        if row[3]:
                            input1 = input(str(reviewed_num+1) + "、" + "*" + row[1] + " " + to_check[k] + " :")
                        else:
                            input1 = input(str(reviewed_num+1) + "、" + row[1] + " " + to_check[k] + " :")
                        if input1 == 'skip':
                            if row[4] != '0':
                                row[4] = str(int(row[4]) - 1)
                            continue
                        if input1 == 'cue':
                            if row[3]:
                                cue_list = row[3].split(";")
                                print(cue_list[0])
                            else:
                                print("No cue!")
                            input1 = input(str(reviewed_num+1) + "、" + "*" + row[1] + " " + to_check[k] + " :")
                        if input1 in to_check[k+1]:
                            print('√ ' + row[1] + " : " + to_check[k] + ". " + to_check[k+1])
                            row[4] = str(int(row[4]) + 1)
                        else:
                            print('× ' + row[1] + " : " + to_check[k] + ". " + to_check[k+1])
                            if row[4] != '0':
                                row[4] = str(int(row[4]) - 1)
                            row[5] = str(int(row[5]) + 1)
                            self.recite_list.append(row)
                        k = k + 2
                    reviewed_num = reviewed_num + 1
        file = open('D:\\Python\\Liam\\ConfigFile\\Wordlist.csv', 'w', newline='')
        writer = csv.writer(file)
        writer.writerows(self.word_list)
        file.close()
        if recite:
            print('***********************************')
            for row_a in self.recite_list:
                print(row_a[1], row_a[2], row_a[3])
            print('***********************************')
            while self.recite_list:
                for row in self.recite_list:
                    flag = 0
                    to_check = row[2].split(".")
                    k = 0
                    while k < len(to_check):
                        input2 = input(row[1] + " " + to_check[k] + " :")
                        if input2 in to_check[k+1]:
                            flag = flag + 2
                        else:
                            print(row[1] + " : " + to_check[k] + ". " + to_check[k+1])
                        if flag == len(to_check):
                            self.recite_list.remove(row)
                        k = k + 2
        print("[recite_word-INFO]: Recite word completed!")

    def __initialize(self, ):
        try:
            file = open("D:\\Python\\Liam\\ConfigFile\\Wordlist.csv")
        except FileNotFoundError:
            print("[recite_word-INFO]: Configuration file error!")
            return
        reader = csv.reader(file)
        self.word_list = list(reader)
        file.close()


class FindAnswer:
    urllib3.disable_warnings()  # 这句和上面一句是为了忽略 https 安全验证警告，参考：https://www.cnblogs.com/ljfight/p/9577783.html

    def get_verifynum(session):  # 网址的验证码逻辑是先去这个网址获取验证码图片，提交计算结果到另外一个网址进行验证。
        r = session.get("https://www.shangxueba.com/ask/VerifyCode2.aspx",
                        verify=False)  # HTTPS 请求进行 SSL 验证或忽略 SSL 验证才能请求成功，忽略方式为 verify=False。参考：https://www.cnblogs.com/ljfight/p/9577783.html
        with open('temp.png', 'wb+') as f:
            f.write(r.content)
        image = Image.open('temp.png')
        image.show()  # 调用系统的图片查看软件打开验证码图片，如果不能打开，可以自己找到 temp.png 打开。
        verifynum = input("\n请输入验证码图片中的计算结果：")
        image.close()
        os.remove("temp.png")
        return verifynum

    def get_question(session):
        r = session.get(link)
        soup = BeautifulSoup(r.content, "html.parser")
        description = soup.find(attrs={"name": "description"})['content']  # 抓取题干内容
        return description

    def get_answer(session, verifynum, dataid):
        data1 = {
            "Verify": verifynum,
            "action": "CheckVerify",
        }
        session.post("https://www.shangxueba.com/ask/ajax/GetZuiJia.aspx", data=data1)  # 核查验证码正确性
        data2 = {
            "phone": "",
            "dataid": dataid,
            "action": "submitVerify",
            "siteid": "1001",
            "Verify": verifynum,
        }
        r = session.post("https://www.shangxueba.com/ask/ajax/GetZuiJia.aspx", data=data2)
        soup = BeautifulSoup(r.content, "html.parser")
        ans = soup.find('h6')
        print("\n" + '-' * 45)
        if (ans):  # 只有验证码核查通过才会显示答案
            print("\n题目：" + get_question(session))
            print(ans.text)
        else:
            print('\n没有找到答案！请检查验证码或网址是否输入有误！\n')
        print('-' * 45)

    def run(session):
        s = requests.session()
        while True:
            s.headers.update({"X-Forwarded-For": "%d.%d.%d.%d" % (
            random.randint(120, 125), random.randint(1, 200), random.randint(1, 200),
            random.randint(1, 200))})  # 这一句是整个程序的关键，通过修改 X-Forwarded-For 信息来欺骗 ASP 站点对于 IP 的验证。
            link = input("\n请输入上学吧网站上某道题目的网址，例如：https://www.shangxueba.com/ask/8952241.html\n\n请输入：").strip()  # 过滤首尾的空格
            if (link[0:31] != "https://www.shangxueba.com/ask/" or link[-4:] != "html"):
                print("\n网址输入有误！请重新输入！\n")
                continue
            dataid = link.split("/")[-1].replace(r".html", "")  # 提取网址最后的数字部分
            if (dataid.isdigit()):  # 根据格式，dataid 应该全部为数字，判断字符串是否全部为数字，返回 True 或者 False
                verifynum = get_verifynum(s)
                get_answer(s, verifynum, dataid)
            else:
                print("\n网址输入有误！请重新输入！\n")
                continue


def recite_words(num=30):
    instance = ReciteWord()
    instance.run(num)


def find_answer():
    instance = FindAnswer()
    instance.run()


if __name__ == '__main__':
    word = ReciteWord()
    word.run(45, True, 2)
    #answer = FindAnswer()
    #answer.run()

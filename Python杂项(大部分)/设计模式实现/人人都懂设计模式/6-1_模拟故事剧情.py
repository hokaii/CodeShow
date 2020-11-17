from copy import copy, deepcopy

class Person:
    """人"""

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def showMyself(self):
        print("我是" + self.__name + ", 年龄" + str(self.__age) + "。")

    def coding(self):
        print("我是码农, 我用程序改变世界, Coding....")

    def reading(self):
        print("阅读使我快乐...")

    def fallInLove(self):
        print("花前月下好相约...")

    def clone(self):
        return copy(self)

if __name__ == '__main__':
    tony = Person("Tony", 27)
    tony.showMyself()
    tony.coding()

    tony1 = tony.clone()
    tony1.showMyself()
    tony1.reading()

    tony2 = tony.clone()
    tony2.showMyself()
    tony2.fallInLove()
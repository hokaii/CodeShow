def singletonDecorator(cls, *args, **kwargs):
    """定义一个单例装饰器"""
    instance = {}

    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapperSingleton

@singletonDecorator
class Singleton3:
    """使用单例装饰器修饰一个类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

@singletonDecorator
class MyBeautifulGril(object):
    def __init__(self, name):
        self.__name = name
        if self.__name == name:
            print("遇见" + name + ", 我一见钟情! ")
        else:
            print("遇见" + name + ", 我置若罔闻! ")

    def showMyHeart(self):
        print(self.__name + "就是我心中的唯一!")

if __name__ == '__main__':
    jenny = MyBeautifulGril("Jenny")
    jenny.showMyHeart()
    kimi = MyBeautifulGril("Kimi")
    kimi.showMyHeart()
    print("id(jenny):", id(jenny), " id(kimi):", id(kimi))
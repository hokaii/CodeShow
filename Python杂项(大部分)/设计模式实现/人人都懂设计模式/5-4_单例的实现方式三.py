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


if __name__ == '__main__':
    tony = Singleton3("Tony")
    karry = Singleton3("Karry")
    print(tony.getName(), karry.getName())
    print("id(tony):", id(tony), "id(karry):", id(karry))
    print("tony == karry:", tony == karry)
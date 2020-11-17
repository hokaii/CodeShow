class Singleton2(type):
    """单例实现方式二"""

    def __init__(cls, what, bases=None, dict=None):
        super().__init__(what, bases, dict)
        cls._instance = None # 初始化全局变量cls._instance为None

    def __call__(cls, *args, **kwargs):
        # 控制对象的创建过程, 如果cls._instance为None, 则创建, 否则直接返回
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class CustomClass(metaclass=Singleton2):
    """用户自定义的类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


if __name__ == '__main__':
    tony = CustomClass("Tony")
    karry = CustomClass("Karry")
    print(tony.getName(), karry.getName())
    print("id(tony):", id(tony), "id(karry):", id(karry))
    print("tony == karry:", tony == karry)
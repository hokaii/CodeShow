"""装饰器可以是一个函数, 也可以是一个类(必须要实现__call__方法, 使其是callable的).
同时装饰器不仅可以修改一个函数, 还可以修饰一个类."""
class ClassDecorator:
    """类装饰器, 记录一个类被实例化的次数"""

    def __init__(self, func):
        self.__numOfCall = 0
        self.__func = func

    def __call__(self, *args, **kwargs):
        self.__numOfCall += 1
        obj = self.__func(*args, **kwargs)
        print("创建%s的第%d个实例: %s" % (self.__func.__name__, self.__numOfCall, id(obj)))
        return obj

@ClassDecorator
class MyClass:

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

if __name__ == '__main__':
    tony = MyClass("Tony")
    karry = MyClass("Karry")
    print(id(tony))
    print(id(karry))
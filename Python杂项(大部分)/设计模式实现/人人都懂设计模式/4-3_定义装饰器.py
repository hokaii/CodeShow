"""每一个函数在被调用之前和被调用之后, 记录一条日志"""
import logging
logging.basicConfig(level=logging.INFO)

def loggingDecorator(func):
    """记录日志的装饰器"""
    def wrapperLogging(*args, **kwargs):
        logging.info("开始执行 %s() ..." % func.__name__)
        func(*args, **kwargs)
        logging.info("%s() 执行完成! " % func.__name__)
    return wrapperLogging

def showInfo(*args, **kwargs):
    print("这是一个测试函数, 参数: ", args, kwargs)



decoratedShowInfo = loggingDecorator(showInfo)
decoratedShowInfo('arg1', 'arg2', kwarg1 = 1, kwarg2 = 2)

"""称loggingDecorator为装饰器, 定义之后, 可以将其应用于所有希望记录日志的函数"""
def showMin(a, b):
    print("%d、%d 中的最小值是: %d" % (a, b, a if a < b else b))

decoratedShowMin = loggingDecorator(showMin)
decoratedShowMin(2, 3)

"""每次调用一个函数都要写两行代码非常繁琐, 可以通过@decorator语法使代码更加简洁"""
"""@loggingDecorator表示用loggingDecorator装饰器来修饰showMax函数"""
@loggingDecorator
def showMax(a, b):
    print("%d、%d 中的最大值是: %d" % (a, b, a if a > b else b))

showMax(2, 3)
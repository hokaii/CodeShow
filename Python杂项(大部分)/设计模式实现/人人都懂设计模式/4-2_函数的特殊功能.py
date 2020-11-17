def func(num):
    """定义内部函数并返回"""

    def firstInnerFunc():
        return "这是第一个内部函数"

    def secondInnerFunc():
        return "这是第二个内部函数"

    if num == 1:
        return firstInnerFunc
    else:
        return secondInnerFunc


if __name__ == '__main__':
    print(func(1))
    print(func(2))
    print(func(1)())
    print(func(2)())
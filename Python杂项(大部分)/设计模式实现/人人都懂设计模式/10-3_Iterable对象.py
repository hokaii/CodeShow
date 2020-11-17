# 方法一: 使用()定义生成器
gen = (x * x for x in range(10))

# 方法二: 使用yield定义generator函数
def fibonacci(maxNum):
    """裴波那契数列的生成器"""

    a = b = 1
    for i in range(maxNum):
        yield a
        a, b = b, a+b

if __name__ == '__main__':
    print("方法一, 0-9的平方数: ")
    for e in gen:
        print(e, end="\t")
    print()

    print("方法二, 裴波那契数列: ")
    fib = fibonacci(10)
    for n in fib:
        print(n, end="\t")
    print()

    print("内置容器的for循环: ")
    arr = [x * x for x in range(10)]
    for e in arr:
        print(e, end="\t")
    print()

    print(type(gen))
    print(type(fib))
    print(type(arr))
from array import array                             #引入array类型
from random import random
floats=array('d',(random() for i in range(10**7)))  #利用一个可迭代对象来建立一个双精度浮点数组（类型码是‘d'），这里我们用的可迭代对象是一个生成器表达式
print(floats[-1])                                   #查看数组的最后一个元素
fp=open('floats.bin','wb')
floats.tofile(fp)                                   #把数组存入一个二进制文件里
fp.close()
floats2=array('d')                                  #新建一个双精度浮点空数组
fp=open('floats.bin','rb')
floats2.fromfile(fp,10**7)                          #把1000万个浮点数从二进制文件里读取出来
fp.close()
print(floats2[-1])                                  #查看数组的最后一个元素
print(floats2==floats)                              #检查两个数组的内容是否完全一样
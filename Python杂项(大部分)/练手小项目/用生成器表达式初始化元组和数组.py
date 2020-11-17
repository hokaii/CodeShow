#coding=utf-8
symbols='$!@#%^*'
print(tuple(ord(symbol) for symbol in symbols))
import array
print(array.array('I',(ord(symbol) for symbol in symbols)))

#使用生成器表达式计算笛卡尔积：
colors=['black','white']
sizes=['S','M','L']
for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):       #生成器表达式逐个生成产出元素，不会一次性产出一个含有6个T恤样式的列表
	print(tshirt)
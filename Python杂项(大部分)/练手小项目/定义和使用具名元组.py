#coding=UTF-8
#定义和使用具名元组
from collections import namedtuple
City = namedtuple('City','name country population coordinates')
tokoy=City('Tokoy','JP',36.933,(35.689722,139.637433))
print(tokoy)
print(tokoy.population)
print(tokoy.coordinates)
print(tokoy[1])
#具名元组的属性和方法
print(City._fields)
LatLong=namedtuple('LatLong','lat long')
delhi_data=('Delhi NCR','IN',21.935,LatLong(28.623523,23.232234))
delhi=City._make(delhi_data)
print(delhi._asdict())
for key ,value in delhi._asdict().items():
	print(key + ':',value)
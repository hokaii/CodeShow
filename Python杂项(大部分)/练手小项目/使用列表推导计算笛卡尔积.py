#coding=utf-8
colors=['black','white']
sizes=['S','M','L']
Tshirts=[(color,size) for color in colors for size in sizes]
print(Tshirts)



#相当于：
for color in colors:
	for size in sizes:
		print((color,size))
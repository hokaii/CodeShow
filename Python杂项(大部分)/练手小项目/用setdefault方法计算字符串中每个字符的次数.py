#coding=UTF-8
import pprint                 #pprint函数和pformat函数
message='It was a bright cold day in April, and the clocks were struking thirteen.'
count={}
for character in message:
	count.setdefault(character,0)
	count[character]=count[character]+1
	
print(pprint.pformat(count))  #漂亮打印
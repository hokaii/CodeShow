#! python3
#项目：下载斗破苍穹漫画

import requests,os,bs4
num=input('你想下载第几话？请输入:')
os.makedirs(('斗破苍穹第%s话'%str(num)),exist_ok=True)
for i in range(8):
    url='https://mhpic.jumanhua.com/comic/D%2F%E6%96%97%E7%A0%B4%E8%8B%8D%E7%A9%B9%E6%8B%86%E5%88%86%E7%89%88%2F'+str(num)+'%E8%AF%9D%2F'+str(i+1)+'.jpg-mht.middle.webp'
    res=requests.get(url)
    res.raise_for_status()
    print('正在下载第%s页...'%str(i+1))
    imageFile=open(os.path.join(('斗破苍穹第%s话'%str(num)),('第%s页.jpg'%str(i+1))),'wb')
    for chunk in res.iter_content(1000000):
            imageFile.write(chunk)
    imageFile.close()
print('\a')
print('下载完毕')
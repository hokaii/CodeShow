#! python3
#项目：下载所有XKCD漫画
import requests,os,bs4
url='https://xkcd.com'
os.makedirs('xkcd',exist_ok=True)#保存漫画到 ./xkcd
while not url.endswith('#'):
    print('Downloading page %s...'%url)
    res=requests.get(url)#下载url
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,"html.parser")#创建一个BeautifulSoup对象
    comicElem=soup.select('#comic img')#因为<img>元素在<div id="comic">元素之内
    if comicElem==[]:
        print('Could not find comic image.')
    else:
        comicUrl='https:'+comicElem[0].get('src')#src属性的值是图像文件的URL
        print('Downloading image %s...'% (comicUrl))
        res=requests.get(comicUrl)
        res.raise_for_status()
        imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    prevLink=soup.select('a[rel="prev"]')[0]#因为Prev按钮有一个rel HTML属性，值是prev
    url='http://xkcd.com'+prevLink.get('href')
print('Done')
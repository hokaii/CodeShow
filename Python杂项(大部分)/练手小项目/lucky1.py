#！ python3
#项目：一次打开几个bing查找结果
import requests,webbrowser,bs4
print('Binging....')
res=requests.get('https://cn.bing.com/search?q=慕课&go=提交&qs=n&form=QBLH&sp=-1&pq=慕课&sc=8-2&sk=&cvid=4947D8A920A14E53B9B77AC4AC0D4474')
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")
linkElems=soup.select('.r a')
numOpen=min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://cn.bing.com'+linkElems[i]+get('href'))
    print('Done')

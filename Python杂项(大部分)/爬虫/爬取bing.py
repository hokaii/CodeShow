import re,urllib.parse,urllib.request,urllib.error
from bs4 import BeautifulSoup as BS

baseUrl = 'http://cn.bing.com/search?'
word = '鹿晗 吴亦凡 张艺兴'
print(word)
word = word.encode(encoding='utf-8', errors='strict')#将Word用utf-8标准转码
#print(word)

data = {'q':word}
data = urllib.parse.urlencode(data)#转换为URL后面部分
#print(data)
url = baseUrl+data
print(url)

try:
    html = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print(e.code)
except urllib.error.URLError as e:
    print(e.reason)

soup = BS(html,"html.parser")
td = soup.findAll("h2")#介绍和链接
count = soup.findAll(class_="sb_count")#数量
for c in count:
    print(c.get_text())

for t in td:
    print(t.get_text())#输出介绍
    pattern = re.compile(r'href="([^"]*)"')
    h = re.search(pattern,str(t))#寻找网址
    if h:
        for x in h.groups():
            print(x)#输出网址

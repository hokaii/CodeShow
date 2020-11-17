import requests
import json
url = 'http://c.m.163.com/nc/article/headline/T1348647853363/0-100.html'
header = {
    'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
    'Connection': 'keep - alive'
}
wbdata = requests.get(url, headers=header).text
data = json.loads(wbdata)
news = data['T1348647853363']
for item in news:
    digest = item['digest']
    mtime = item['mtime']
    title = item['title']
    source = item['source']
    try:
        url = item['url']
    except:
        url = ''
    newes_data = {
        'title': title,
        'digest': digest,
        'source': source,
    }
    print(newes_data)
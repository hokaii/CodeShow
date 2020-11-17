import requests
from bs4 import BeautifulSoup as bs

url = "https://www.baidu.com/s?wd=%E8%8B%8F%E8%BD%BC&rsv_spt=1&rsv_iqid=0xc1d581080003895f&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=11&rsv_sug1=8&rsv_sug7=100&rsv_t=1a8feVkcrzYbmmVsR68UsfJlI%2BGUcEpvUkO%2FAwDwPPcUs%2F%2BqH%2FsUlHcOgbxe461bcYL0"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url, headers=headers).text
soup = bs(html, 'lxml')
for h3 in soup.find(id='content_left').select('h3'):
    print(h3.get_text())
	
for i in range(9):
	for div in soup.find(id='content_left').find(id=str(i+1)).select('div'):
		print(div.get_text())
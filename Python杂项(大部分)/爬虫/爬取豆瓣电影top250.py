import requests
import re
import json
import time
from requests.exceptions import RequestException
import codecs

def get_one_page(url):
	try:
		headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safiri/537.36'
		}
		response = requests.get(url, headers = headers)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def parse_one_page(html):
	pattern = re.compile(
		'<li>.*?<em class="">(.*?)</em>.*?src="(.*?)".*?<span.*?class="title">(.*?)</span>.*?<p.*?class="">\n\s{28}(.*?)&nbsp;&nbsp;&nbsp;(.*?)...<br>.*?</li>', re.S)
	items = re.findall(pattern, html)
	for item in items:
		print(item)
		print('\n')
	"""for item in items:
		yield{
			'index': item[0],
			'image': item[1],
			'title': item[2].strip(),
			'actor': item[3].strip()[3:],
			#'time': item[4].strip()[5:],
			#'score': item[5] + item[6]
		}
	"""

def main():
	for i in range(10):
		num = 25 * i
		url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
		html = get_one_page(url)
		parse_one_page(html)
		time.sleep(2)

main()
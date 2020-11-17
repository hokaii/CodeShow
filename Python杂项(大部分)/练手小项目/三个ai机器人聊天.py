from time import sleep
import requests
import urllib.request
import re

s = input('话题：')
while True:
    resp = requests.post('http://www.tuling123.com/openapi/api', data={'key': 'f1b6d7cb959c419a87fdd5c68be55bba', 'info': s,})
    resp = resp.json()
    sleep(1)
    print('图灵: ', resp['text'])

    s = resp['text']
    resp = requests.get('http://api.qingyunke.com/api.php?', {'key': 'free', 'appid': 0, 'msg': s})
    resp.encoding = 'utf-8'
    resp = resp.json()
    sleep(1)
    print('青云：', resp['content'])

    t = urllib.parse.quote(s)
    link = urllib.request.urlopen("http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%22ff725c236e5245a3ac825b2dd88a7501%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%227cd29df3450745fbbdcf1a462e6c58e6%22%2C%22body%22%3A%7B%22content%22%3A%22" + t + "%22%7D%2C%22type%22%3A%22txt%22%7D")
    html_doc = link.read().decode()
    reply_list = re.findall(r'\"content\":\"(.+?)\\r\\n\"', html_doc)
    print('小i: '+reply_list[-1])
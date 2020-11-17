import requests
from urllib.parse import urlencode
import os
from hashlib import md5
# from multiprocessing.pool import Pool

def get_page():
    params = {
        'category': '组图',
        'utm_source': 'toutiao',
        'max_behot_time': '0',
        'as': 'A1156CD7EC0D485',
        'cp': '5C7C0D64E8F55E1',
        '_signature': 'HGOwkAAAQCO2TPAQ8svE1BxjsI',
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
    url = 'https://www.toutiao.com/api/pc/feed/?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_images(json):
    if json:
        items = json.get('data')
        for item in items:
            title = item.get('title')
            images = item.get('image_list')
            if images:
                for image in images:
                    yield {
                        'images': image.get('url'),
                        'title': title
                    }

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        if(item.get('images')):
            response = requests.get("https:" + item.get('images'))
            if response.status_code == 200:
                file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                else:
                    print('Aleady Download', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


"""
GROUP_START = 1
GROUP_END = 20


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)
"""

if __name__ == '__main__':
    """
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
    """
    json = get_page()
    for item in get_images(json):
        save_image(item)
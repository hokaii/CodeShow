"""
2019/6/9/10/47 MusicDownload v0.1
Author:hoka
TODO:
1. Kugou模块因为付费歌曲无法在网页播放无法下载, 下一步抓取客户端的数据来下载
2. 图形界面
3. 爬取图片及其他信息
4. 歌曲列表数量
"""
from os import path, mkdir, urandom
from re import findall
from requests import get, Session
from sys import stdout, exit
from random import randrange
from random import random
from json import dumps
from Crypto.Cipher import AES
from contextlib import closing
from base64 import b64encode
from codecs import encode
from time import sleep



class Kugou:
    def __init__(self):
        self.info = {}
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
        self.search_url = 'https://songsearch.kugou.com/song_search_v2?keyword={}&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1552897007078'
        # self.search_url = 'http://songsearch.kugou.com/song_search_v2?keyword={}&page=1&pagesize=30'
        self.hash_url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash={}'
        self.search_results = {}
    """外部调用"""
    def get(self, mode='search', **kwargs):
        if mode == 'search':
            song_name = kwargs.get('song_name')
            self.search_results = self.__search(song_name)
            return self.search_results
        elif mode == 'download':
            need_down_list = kwargs.get('need_down_list')
            downed_list = []
            save_path = kwargs.get('save_path') if kwargs.get('save_path') is not None else '.\Download'
            if need_down_list is not None:
                try:  # 这里报错的原因是酷狗网页版无法播放付费歌曲
                    for download_name in need_down_list:
                        file_hash = self.search_results.get(download_name)
                        res = get(self.hash_url.format(file_hash))
                        play_url = findall('"play_url":"(.*?)"', res.text)[0]
                        download_url = play_url.replace("\\", "")
                        if not download_url:
                            continue
                        res = self.__download(download_name, download_url, save_path)
                        if res:
                            downed_list.append(download_name)
                except:
                    print("这首歌在酷狗平台无法下载，请更换平台重新下载 0.0")
            return downed_list
        else:
            raise ValueError('mode in kugou().get must be <search> or <download>...')
    """下载"""
    def __download(self, download_name, download_url, save_path):
        if not path.exists(save_path):
            mkdir(save_path)
        download_name = download_name.replace('<', '').replace('>', '').replace('\\', '').replace('/', '') \
                                     .replace('?', '').replace(':', '').replace('"', '').replace('：', '') \
                                     .replace('|', '').replace('？', '').replace('*', '')
        save_name = 'kugou_{}'.format(download_name)
        save_name = save_name.replace('em', '')
        if path.exists(path.join(save_path, save_name+'.mp3')):
            print('The music file "' + save_name + '" already exists!')
            return True
        count = 0
        while path.isfile(path.join(save_path, save_name+'.mp3')):
            count += 1
            save_name = 'kugou_{}_{}'.format(download_name, count)
        save_name += '.mp3'
        try:
            print('[kugou-INFO]: 正在下载 --> %s' % save_name.split('.')[0])
            with closing(get(download_url, headers=self.headers, stream=True, verify=False)) as res:
                total_size = int(res.headers['content-length'])
                temp_size = 0
                if res.status_code == 200:
                    with open(path.join(save_path, save_name), "wb") as f:
                        for chunk in res.iter_content(chunk_size=1024):
                            if chunk:
                                temp_size += len(chunk)
                                f.write(chunk)
                                f.flush()
                                done = int(50 * temp_size / total_size)
                                stdout.write("\r[%s%s] %d%%" % ('▉' * done, '  ' * (50 - done), 100 * temp_size / total_size))
                                stdout.flush()
                        print("\r")
                    """
                    label = '[FileSize]:%0.2f MB' % (total_size/(1024*1024))
                    with click.progressbar(length=total_size, label=label) as progressbar:
                        with open(path.join(save_path, save_name), 'wb') as f:
                            for chunk in res.iter_content(chunk_size=1024):
                                if chunk:
                                    f.write(chunk)
                                    progressbar.update(1024)
                    """
                else:
                    raise RuntimeError('Connect error...')
            return True
        except:
            return False
    """根据歌名搜索"""
    def __search(self, song_name):
        res = get(self.search_url.format(song_name), headers=self.headers)
        results = {}
        for song in res.json()['data']['lists']:
            file_hash = song.get('FileHash')
            singers = song.get('SingerName')
            album = song.get('AlbumName')
            singers = singers.replace('<em>', '').replace('</em>', '')
            download_name = '%s--%s--%s' % (song.get('SongName').replace('<em>', '').replace('</em>', ''), singers, album)
            count = 0
            while download_name in results:
                count += 1
                download_name = '%s(%d)--%s--%s' % (song.get('SongName').replace('<em>', '').replace('</em>', ''), count, singers, album)
            results[download_name] = file_hash
        return results


class Kuwo:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.search_url = 'http://sou.kuwo.cn/ws/NSearch?key={}&type=music&pn={}'
        # self.search_url = 'http://sou.kuwo.cn/ws/NSearch?type=all&catalog=yueku2016&key={}'
        self.player_url = 'http://player.kuwo.cn/webmusic/st/getNewMuiseByRid?rid=MUSIC_{}'
        self.search_results = {}
    """外部调用"""
    def get(self, mode='search', **kwargs):
        if mode == 'search':
            song_name = kwargs.get('song_name')
            self.search_results = self.__search(song_name)
            return self.search_results
        elif mode == 'download':
            need_down_list = kwargs.get('need_down_list')
            downed_list = []
            save_path = kwargs.get('save_path') if kwargs.get('save_path') is not None else '.\Download'
            if need_down_list is not None:
                for download_name in need_down_list:
                    song_id = self.search_results.get(download_name)
                    res = get(self.player_url.format(song_id), headers=self.headers)
                    mp3dl = findall(r'<mp3dl>(.*?)</mp3dl', res.text)[0]
                    mp3path = findall(r'<mp3path>(.*?)</mp3path>', res.text)[0]
                    download_url = 'http://' + mp3dl + '/resource/' + mp3path
                    res = self.__download(download_name, download_url, save_path)
                    if res:
                        downed_list.append(download_name)
            return downed_list
        elif mode == 'download_singer':
            need_down_singer = kwargs.get('need_down_singer')
            for j in range(25):
                j = j + 1
                try:
                    search_results = self.__search(need_down_singer, num=j)
                except:
                    break
                s_downed_list = []
                s_savapath = kwargs.get('savepath') if kwargs.get('savepath') is not None else './Download/music/{}'.format(need_down_singer)
                if search_results is not None:
                    for s_download_name in search_results:
                        if s_download_name.split('--')[1] != need_down_singer:
                            continue
                        else:
                            s_songid = search_results.get(s_download_name)
                            s_res = get(self.player_url.format(s_songid), headers=self.headers)
                            s_mp3dl = findall(r'<mp3dl>(.*?)</mp3dl>', s_res.text)[0]
                            s_mp3path = findall(r'<mp3path>(.*?)</mp3path>', s_res.text)[0]
                            download_url = 'http://' + s_mp3dl + '/resource/' + s_mp3path
                            s_res = self.__download(s_download_name, download_url, s_savapath)
                            if s_res:
                                s_downed_list.append(s_download_name)
        else:
            raise ValueError('mode in kuwo().get must be <search> or <download>...')
    """下载"""
    def __download(self, download_name, download_url, save_path):
        if not path.exists(save_path):
            mkdir(save_path)
        download_name = download_name.replace('<', '').replace('>', '').replace('\\', '').replace('/', '') \
                                     .replace('?', '').replace(':', '').replace('"', '').replace('：', '') \
                                     .replace('|', '').replace('？', '').replace('*', '')
        save_name = 'kuwo_{}'.format(download_name)
        save_name = save_name.replace('&nbsp', '')
        if path.exists(path.join(save_path, save_name+'.mp3')):
            print('The music file "' + save_name + '" already exists!')
            return True
        count = 0
        while path.isfile(path.join(save_path, save_name+'.mp3')):
            count += 1
            save_name = 'kuwo_{}_{}'.format(download_name, count)
        save_name += '.mp3'
        try:
            print('[kuwo-INFO]: 正在下载 --> %s' % save_name.split('.')[0])
            with closing(get(download_url, headers=self.headers, stream=True, verify=False)) as res:
                total_size = int(res.headers['content-length'])
                temp_size = 0
                if res.status_code == 200:
                    with open(path.join(save_path, save_name), "wb") as f:
                        for chunk in res.iter_content(chunk_size=1024):
                            if chunk:
                                temp_size += len(chunk)
                                f.write(chunk)
                                f.flush()
                                done = int(50 * temp_size / total_size)
                                stdout.write("\r[%s%s] %d%%" % ('▉' * done, '  ' * (50 - done), 100 * temp_size / total_size))
                                stdout.flush()
                        print("\r")
                else:
                    raise RuntimeError('Connect error...')
            return True
        except:
            return False
    """搜索"""
    def __search(self, song_name, num=1):
        res = get(self.search_url.format(song_name, num), headers=self.headers)
        infos = findall(r'<a href="http://www\.kuwo\.cn/yinyue/(.*?)/" title="(.*?)" target="_blank">', res.text)
        albums = findall(r'\<p class="a_name"\>(.*?)\</p\>', res.text)
        all_singers = findall(r'\<p class="s_name"\>(.*?)\</p\>', res.text)
        results = {}
        for i in range(len(infos)):
            song_id = infos[i][0]
            singers = findall(r'title="(.*?)"', all_singers[i])
            singers = ','.join(singers)
            try:
                album = findall(r'title="(.*?)"', albums[i])[0]
            except:
                album = '无专辑'
            download_name = '%s--%s--%s' % (infos[i][1], singers, album)
            download_name = download_name.replace('&nbsp;', '')
            count = 0
            while download_name in results:
                count += 1
                download_name = '%s(%d)--%s--%s' % (infos[i][1], count, singers, album)
                download_name = download_name.replace('&nbsp;', '')
            results[download_name] = song_id
        return results


class Qianqian:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'referer': 'http://music.baidu.com/'
        }
        self.search_url = 'http://musicapi.qianqian.com/v1/restserver/ting'
        self.player_url = 'http://music.baidu.com/data/music/links'
        self.search_results = {}
    """外部调用"""
    def get(self, mode='search', **kwargs):
        if mode == 'search':
            song_name = kwargs.get('song_name')
            self.search_results = self.__search(song_name)
            return self.search_results
        elif mode == 'download':
            need_down_list = kwargs.get('need_down_list')
            downed_list = []
            save_path = kwargs.get('sava_path') if kwargs.get('save_path') is not None else '.\Download'
            if need_down_list is not None:
                for download_name in need_down_list:
                    song_id = self.search_results.get(download_name)
                    params = {"songIds": song_id}
                    res = get(self.player_url, params=params, headers=self.headers)
                    if not res.json().get('data').get('songList'):
                        continue
                    download_url = res.json().get('data').get('songList')[0].get('songLink')
                    if not download_url:
                        continue
                    res = self.__download(download_name, download_url, save_path)
                    if res:
                        downed_list.append(download_name)
            return downed_list
        else:
            raise ValueError('mode in qianqian().get must be <search> or <download>...')
    """下载"""
    def __download(self, download_name, download_url, save_path):
        if not path.exists(save_path):
            mkdir(save_path)
        download_name = download_name.replace('<', '').replace('>', '').replace('\\', '').replace('/', '') \
                                     .replace('?', '').replace(':', '').replace('"', '').replace('：', '') \
                                     .replace('|', '').replace('？', '').replace('*', '')
        save_name = 'qianqian_{}'.format(download_name)
        if path.exists(path.join(save_path, save_name+'.mp3')):
            print('The music file "' + save_name + '" already exists!')
            return True
        count = 0
        while path.isfile(path.join(save_path, save_name+'.mp3')):
            count += 1
            save_name = 'qianqian_{}_{}'.format(download_name, count)
        save_name += '.mp3'
        try:
            print('[qianqian-INFO]: 正在下载 --> %s' % save_name.split('.')[0])
            with closing(get(download_url, headers=self.headers, stream=True, verify=False)) as res:
                total_size = int(res.headers['content-length'])
                temp_size = 0
                if res.status_code == 200:
                    with open(path.join(save_path, save_name), "wb") as f:
                        for chunk in res.iter_content(chunk_size=1024):
                            if chunk:
                                temp_size += len(chunk)
                                f.write(chunk)
                                f.flush()
                                done = int(50 * temp_size / total_size)
                                stdout.write("\r[%s%s] %d%%" % ('▉' * done, '  ' * (50 - done), 100 * temp_size / total_size))
                                stdout.flush()
                        print("\r")
                    """
                    label = '[FileSize]:%0.2f MB' % (total_size/(1024*1024))
                    with click.progressbar(length=total_size, label=label) as progressbar:
                        with open(path.join(save_path, save_name), 'wb') as f:
                            for chunk in res.iter_content(chunk_size=1024):
                                if chunk:
                                    f.write(chunk)
                                    progressbar.update(1024)
                    """
                else:
                    raise RuntimeError('Connect error...')
            return True
        except:
            return False
    """搜索"""
    def __search(self, song_name):
        params = {
            "query": song_name,
            "method": "baidu.ting.search.common",
            "format": "json",
            "page_no": 1,
            "page_size": 15
        }
        res = get(self.search_url, params=params, headers=self.headers)
        results = {}
        for song in res.json()['song_list']:
            song_id = song.get('song_id')
            singers = song.get('author').replace("<em>", "").replace("</em>", "")
            album = song.get('album_title').replace("<em>", "").replace("</em>", "")
            download_name = '%s--%s--%s' % (song.get('title').replace("<em>", "").replace("</em>", ""), singers, album)
            count = 0
            while download_name in results:
                count += 1
                download_name = '%s(%d)--%s--%s' % (song.get('title'), count, singers, album)
            results[download_name] = song_id
        return results


class QqMusic:
    def __init__(self):
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
                "referer": "http://y.qq.com"
        }
        self.ios_headers = {
                'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46",
                "referer": "http://y.qq.com"
        }
        self.search_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
        self.fcg_url = 'http://base.music.qq.com/fcgi-bin/fcg_musicexpress.fcg'
        self.download_format_url = "http://dl.stream.qqmusic.qq.com/{}{}.mp3?vkey={}&guid={}&fromtag=1"
        self.search_results = {}
    '''外部调用'''
    def get(self, mode='search', **kwargs):
        if mode == 'search':
            song_name = kwargs.get('song_name')
            self.search_results = self.__search(song_name)
            return self.search_results
        elif mode == 'download':
            need_down_list = kwargs.get('need_down_list')
            downed_list = []
            save_path = kwargs.get('save_path') if kwargs.get('save_path') is not None else '.\Download'
            if need_down_list is not None:
                for download_name in need_down_list:
                    songmid, media_mid = self.search_results.get(download_name)
                    guid = str(randrange(1000000000, 10000000000))
                    params = {
                        "guid": guid,
                        "format": "json",
                        "json": 3
                    }
                    fcg_res = get(self.fcg_url, params=params, headers=self.ios_headers)
                    vkey = fcg_res.json()['key']
                    for quality in ["M800", "M500", "C400"]:
                        download_url = self.download_format_url.format(quality, songmid, vkey, guid)
                        res = self.__download(download_name, download_url, save_path)
                        if res:
                            break
                        print('[qq-INFO]: %s-%s下载失败, 将尝试降低歌曲音质重新下载...' % (download_name, quality))
                    if res:
                        downed_list.append(download_name)
            return downed_list
        else:
            raise ValueError('mode in qq().get must be <search> or <download>...')
    '''下载'''
    def __download(self, download_name, download_url, save_path):
        if not path.exists(save_path):
            mkdir(save_path)
        download_name = download_name.replace('<', '').replace('>', '').replace('\\', '').replace('/', '') \
                                     .replace('?', '').replace(':', '').replace('"', '').replace('：', '') \
                                     .replace('|', '').replace('？', '').replace('*', '')
        save_name = 'qq_{}'.format(download_name)
        if path.exists(path.join(save_path, save_name+'.mp3')):
            print('The music file "' + save_name + '" already exists!')
            return True
        count = 0
        while path.isfile(path.join(save_path, save_name+'.mp3')):
            count += 1
            save_name = 'qq_{}_{}'.format(download_name, count)
        save_name += '.mp3'
        try:
            print('[qq-INFO]: 正在下载 --> %s' % save_name.split('.')[0])
            with closing(get(download_url, headers=self.headers, stream=True, verify=False)) as res:
                total_size = int(res.headers['content-length'])
                temp_size = 0
                if res.status_code == 200:
                    with open(path.join(save_path, save_name), "wb") as f:
                        for chunk in res.iter_content(chunk_size=1024):
                            if chunk:
                                temp_size += len(chunk)
                                f.write(chunk)
                                f.flush()
                                done = int(50 * temp_size / total_size)
                                stdout.write("\r[%s%s] %d%%" % ('▉' * done, '  ' * (50 - done), 100 * temp_size / total_size))
                                stdout.flush()
                        print("\r")
                    """
                    label = '[FileSize]:%0.2f MB' % (total_size/(1024*1024))
                    with click.progressbar(length=total_size, label=label) as progressbar:
                        with open(path.join(save_path, save_name), "wb") as f:
                            for chunk in res.iter_content(chunk_size=1024):
                                if chunk:
                                    f.write(chunk)
                                    progressbar.update(1024)
                    """
                else:
                    raise RuntimeError('Connect error...')
            return True
        except:
            return False
    '''根据歌名搜索'''
    def __search(self, song_name):
        params = {
            'w': song_name,
            'format': 'json',
            'p': 1,
            'n': 15
        }
        res = get(self.search_url, params=params, headers=self.headers)
        results = {}
        for song in res.json()['data']['song']['list']:
            media_mid = song.get('media_mid')
            songmid = song.get('songmid')
            singers = [s.get('name') for s in song.get('singer')]
            singers = ','.join(singers)
            album = song.get('albumname')
            download_name = '%s--%s--%s' % (song.get('songname'), singers, album)
            count = 0
            while download_name in results:
                count += 1
                download_name = '%s(%d)--%s--%s' % (song.get('songname'), count, singers, album)
            results[download_name] = [songmid, media_mid]
        return results


"""
Function:
    用于算post的两个参数, 具体原理详见知乎： 
    https://www.zhihu.com/question/36081767
"""


class Cracker:
    def __init__(self):
        self.modules = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'
        self.pubKey = '010001'

    def get(self, text):
        text = dumps(text)
        sec_key = self._createsecretkey(16)
        enc_text = self._aesencrypt(self._aesencrypt(text, self.nonce), sec_key)
        enc_sec_key = self._rsaencrypt(sec_key, self.pubKey, self.modules)
        post_data = {
            'params': enc_text,
            'encSecKey': enc_sec_key
        }
        return post_data

    def _aesencrypt(self, text, sec_key):
        pad = 16 - len(text) % 16
        if isinstance(text, bytes):
            text = text.decode('utf-8')
        text = text + str(pad * chr(pad))
        sec_key = sec_key.encode('utf-8')
        encryptor = AES.new(sec_key, 2, b'0102030405060708')
        text = text.encode('utf-8')
        ciphertext = encryptor.encrypt(text)
        ciphertext = b64encode(ciphertext)
        return ciphertext

    def _rsaencrypt(self, text, pubkey, modulus):
        text = text[::-1]
        rs = int(encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubkey, 16) % int(modulus, 16)
        return format(rs, 'x').zfill(256)

    def _createsecretkey(self, size):
        return (''.join(map(lambda xx: (hex(ord(xx))[2:]), str(urandom(size)))))[0:16]


class WangyiYun:
    def __init__(self):
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'cookie': '_iuqxldmzr_=32; _ntes_nnid=0e6e1606eb78758c48c3fc823c6c57dd,1527314455632; '
            '_ntes_nuid=0e6e1606eb78758c48c3fc823c6c57dd; __utmc=94650624; __utmz=94650624.1527314456.1.1.'
            'utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_TID=blBrSVohtue8%2B6VgDkxOkJ2G0VyAgyOY;'
            ' JSESSIONID-WYYY=Du06y%5Csx0ddxxx8n6G6Dwk97Dhy2vuMzYDhQY8D%2BmW3vlbshKsMRxS%2BJYEnvCCh%5CKY'
            'x2hJ5xhmAy8W%5CT%2BKqwjWnTDaOzhlQj19AuJwMttOIh5T%5C05uByqO%2FWM%2F1ZS9sqjslE2AC8YD7h7Tt0Shufi'
            '2d077U9tlBepCx048eEImRkXDkr%3A1527321477141; __utma=94650624.1687343966.1527314456.1527314456'
            '.1527319890.2; __utmb=94650624.3.10.1527319890',
            'Origin': 'https://music.163.com',
            'Referer': 'https://music.163.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36'
            }
        self.search_url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='
        self.player_url = 'http://music.163.com/weapi/song/enhance/player/url?csrf_token='
        self.cracker = Cracker()
        self.session = Session()
        self.session.headers.update(self.headers)
        self.search_results = {}
    '''外部调用'''
    def get(self, mode='search', bit_rate=320000, csrf='', timeout=600, **kwargs):
        if mode == 'search':
            song_name = kwargs.get('song_name')
            self.search_results = self.__search(song_name)
            return self.search_results
        elif mode == 'download':
            need_down_list = kwargs.get('need_down_list')
            downed_list = []
            save_path = kwargs.get('save_path') if kwargs.get('save_path') is not None else '.\Download'
            if need_down_list is not None:
                for download_name in need_down_list:
                    song_id = self.search_results.get(download_name)
                    params2 = {
                        'ids': [song_id],
                        'br': bit_rate,
                        'csrf_token': csrf
                    }
                    res = self.__postrequests(self.player_url, params2, timeout)
                    try:
                        download_url = res['data'][0]['url']
                    except:
                        download_url = self.song_url.format(song_id)
                    res = self.__download(download_name, download_url, save_path)
                    if res:
                        downed_list.append(download_name)
                        sleep(random())
            return downed_list
        else:
            raise ValueError('mode in wangyiyun().get must be <search> or <download>...')
    '''下载'''
    def __download(self, download_name, download_url, save_path):
        if not path.exists(save_path):
            mkdir(save_path)
        download_name = download_name.replace('<', '').replace('>', '').replace('\\', '').replace('/', '') \
                                     .replace('?', '').replace(':', '').replace('"', '').replace('：', '') \
                                     .replace('|', '').replace('？', '').replace('*', '')
        save_name = 'wangyiyun_{}'.format(download_name)
        if path.exists(path.join(save_path, save_name+'.mp3')):
            print('The music file "' + save_name + '" already exists!')
            return True
        count = 0
        while path.isfile(path.join(save_path, save_name+'.mp3')):
            count += 1
            save_name = 'wangyiyun_{}_{}'.format(download_name, count)
        save_name += '.mp3'
        try:
            print('[wangyiyun-INFO]: 正在下载 --> %s' % save_name.split('.')[0])
            with closing(get(download_url, stream=True, verify=False)) as res:
                total_size = int(res.headers['content-length'])
                temp_size = 0
                if res.status_code == 200:
                    with open(path.join(save_path, save_name), "wb") as f:
                        for chunk in res.iter_content(chunk_size=1024):
                            if chunk:
                                temp_size += len(chunk)
                                f.write(chunk)
                                f.flush()
                                done = int(50 * temp_size / total_size)
                                stdout.write("\r[%s%s] %d%%" % ('▉' * done, '  ' * (50 - done), 100 * temp_size / total_size))
                                stdout.flush()
                        print("\r")
                    """
                    label = '[FileSize]:%0.2f MB' % (total_size/(1024*1024))
                    with click.progressbar(length=total_size, label=label) as progressbar:
                        with open(path.join(save_path, save_name), "wb") as f:
                            for chunk in res.iter_content(chunk_size=1024):
                                if chunk:
                                    f.write(chunk)
                                    progressbar.update(1024)
                    """
                else:
                    raise RuntimeError('Connect error...')
            return True
        except:
            return False
    '''根据歌名搜索'''
    def __search(self, song_name, search_type=1, limit=9, timeout=600):
        params1 = {
            's': song_name,
            'type': search_type,
            'offset': 0,
            'sub': 'false',
            'limit': limit
        }
        res = self.__postrequests(self.search_url, params1, timeout)
        results = {}
        if res is not None:
            if res['result']['songCount'] >= 1:
                songs = res['result']['songs']
                for song in songs:
                    song_id = song.get('id')
                    singers = [each.get('name') for each in song.get('ar')]
                    singers = ','.join(singers)
                    album = song.get('al').get('name')
                    download_name = '%s--%s--%s' % (song.get('name'), singers, album)
                    count = 0
                    while download_name in results:
                        count += 1
                        download_name = '%s(%d)--%s--%s' % (song.get('name'), count, singers, album)
                    results[download_name] = song_id
        return results
    '''post请求函数'''
    def __postrequests(self, url, params, timeout):
        post_data = self.cracker.get(params)
        res = self.session.post(url, data=post_data, timeout=timeout, headers=self.headers)
        if res.json()['code'] != 200:
            return None
        else:
            return res.json()


class MusicDownload:
    def __init__(self, **kwargs):  # D:\\Python\\Liam\\Download\\music
        self.save_path = kwargs.get('save_path')if kwargs.get('save_path') is not None else None
        self.legal = True
        self.INFO = []
        self.resources = ['网易云音乐', 'QQ音乐', '酷狗音乐', '酷我音乐', '千千音乐']
        self.platform_now = WangyiYun()
        self.platform_now_name = '网易云音乐'
        self.is_select_platform = True
    """外部调用"""
    def run(self):
        """
        //打开下载所有相关歌手歌曲
        fc = input('Enter the name of the artist or song for the full list to download: ')
        if fc == 'download all':
            kw = Kuwo()
            kw.get('download_singer', need_down_singer=fc)
        """
        while True:
            try:
                self.__search()
            except ConnectionError:
                r = input("未检查到网络，请检查网络设置")
                break
    """选择平台"""
    def __select_platform(self):
        while True:
            print('支持平台: ')
            for idx, resource in enumerate(self.resources):
                print('--%d. %s' % ((idx+1), resource))
            platform_idx = self.__input('选择平台号(1-%d):' % len(self.resources))
            if platform_idx == '1':
                return WangyiYun(), '网易云音乐'
            elif platform_idx == '2':
                return QqMusic(), 'qq音乐'
            elif platform_idx == '3':
                return Kugou(), '酷狗音乐'
            elif platform_idx == '4':
                return Kuwo(), '酷我音乐'
            elif platform_idx == '5':
                return Qianqian(), '千千静听'
            else:
                print('<ERROR>--平台输入有误, 请重新输入--<ERROR>')

    """搜索操作"""
    def __search(self):
        try:
            r = get('https://www.baidu.com')
            re = True
        except:
            re = False
        if re == False:
            raise ConnectionError
        song_name = self.__input('[%s-INFO]: 输入歌曲名 --> ' % self.platform_now_name)
        if song_name is None:
            return
        results = self.platform_now.get(mode='search', song_name=song_name)
        while True:
            print('[%s-INFO]: 搜索结果如下 -->' % self.platform_now_name)
            for idx, result in enumerate(sorted(results.keys())):
                self.INFO.append(result)
                print('[%d]. %s' % (idx+1, result))
            need_down_numbers = self.__input('[%s-INFO]: 输入需要下载的歌曲编号(1-%d) -->' % (self.platform_now_name, len(results.keys()))).split(',')
            if need_down_numbers is None:
                return
            numbers_legal = [str(i) for i in range(1, len(results.keys())+1)]
            error_flag = False
            for number in need_down_numbers:
                if number not in numbers_legal:
                    print('<ERROR>--歌曲号输入有误, 请重新输入--<ERROR>')
                    error_flag = True
                    break
            if error_flag:
                continue
            need_down_list = []
            for number in need_down_numbers:
                need_down_list.append(sorted(results.keys())[int(number)-1])
            break
        return self.__download(need_down_list)
    """下载选择的歌曲"""
    def __download(self, need_down_list):
        return self.platform_now.get(mode='download', need_down_list=need_down_list, save_path=self.save_path)
    """处理输入"""
    def __input(self, tip=None):
        if tip is None:
            user_input = input()
        else:
            user_input = input(tip)
        if user_input.lower() == 'quit' or user_input.lower() == 'exit':
            print('Client exited!')
            exit(-1)
        elif user_input.lower() == 'change':
            self.is_select_platform = False
            self.platform_now, self.platform_now_name = self.__select_platform()
            return None
        elif user_input.lower() == 'help':
            print("MusicDownload v0.1 author:höka 欢迎使用!\n默认平台为网易云音乐，输入歌曲名后输入单个数字下载歌曲，输入多个用逗号分隔的数字可下载多首歌曲\n输入'change'更换平台，输入'exit'或者'quit'关闭程序。\r")
        else:
            return user_input


if __name__ == '__main__':
    """
    ku_gou = Kugou()
    res = ku_gou.get(mode='search', song_name='一路向北')
    ku_gou.get(mode='download', need_down_list=list(res.keys())[:2])
    kw = Kuwo()
    res_kw = kw.get(mode='search', song_name='背影')
    kw.get(mode='download', need_down_list=list(res_kw.keys())[:2])
    qianian = Qianqian()
    res = qianian.get(mode='search', song_name='生僻字')
    qianian.get(mode='download', need_down_list=list(res.keys())[:2])
    qq = QqMusic()
    res = qq.get(mode='search', song_name='最佳歌手')
    qq.get(mode='download', need_down_list=list(res.keys())[:2])
    wy = WangyiYun()
    res = wy.get(mode='search', song_name='年少有为')
    wy.get(mode='download', need_down_list=list(res.keys())[:2])
    """
    music = MusicDownload(save_path="D:\\Python\\Liam\\Download\\music")# save_path="D:\\Python\\Liam\\Download"
    music.run()
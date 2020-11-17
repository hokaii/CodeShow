import sys
import requests
import os

#屏蔽warning信息, 因为下面verify=False会报警告信息
requests.packages.urllib3.disable_warnings()

def download(url, file_path):
    # verify=False, 这一句话是为了有点网站证书问题, 为True会报错
    r = requests.get(url, stream=True, verify=False)

    # 既然要实现下载进度, 那就要知道文件大小, 下面这句就是得到总大小
    total_size = int(r.headers['Content-Length'])
    # r.headers 为{'Date': 'Sun, 02 Jun 2019 12:50:23 GMT',
    # 'Server': 'Apache', 'Content-Length': '141287457',
    # 'Content-MD5': '39e87ab50535a6b8101650aeaa82be1b',
    # 'Accept-Ranges': 'bytes',
    # 'Content-Disposition': 'attachment; filename=jhu-usc.edu_COAD.HumanMethylation450.13.lvl-3.TCGA-QG-A5Z1-01A-11D-A28O-05.gdc_hg38.txt',
    # 'Access-Control-Allow-Origin': '*',
    # 'Access-Control-Allow-Headers': 'Content-Type, X-CSRFToken, X-Requested-With',
    # 'Access-Control-Expose-Headers': 'Content-Disposition', 'Keep-Alive': 'timeout=5, max=100',
    # 'Connection': 'Keep-Alive', 'Content-Type': 'application/octet-stream',
    # 'X-Frame-Options': 'SAMEORIGIN', 'Strict-Transport-Security': 'max-age=63072001; includeSubdomains; preload'}
    temp_size = 0

    with open(file_path, 'wb') as f:
        # iter_content()函数就是得到文件的内容,
        # 有些人下载文件很大怎么办, 内存都装不下怎么办
        # 那就要指定chunk_size= 1024, 大小自己设置
        # 意思是下载一点写一点到磁盘
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                temp_size += len(chunk)
                f.write(chunk)
                f.flush()
                # 下载进度部分
                done = int(50 * temp_size / total_size)
                # 调用标准输出刷新命令行, 看到\r回车符了吧
                # 相当于把每一行重新刷新一遍
                sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                sys.stdout.flush()
    print() # 避免上面\r回车符, 执行完后需要换行

if __name__ == '__main__':
    link = r'http://antiserver.kuwo.cn/anti.s?useless=/resource/&format=mp3&rid=MUSIC_57649473&response=res&type=convert_url&'
    UUID = r'2a4a3044-0b1a-4722-83ed-43ba5d6d25b0'
    path = r'./test.mp3'
    url = os.path.join(link, UUID)
    download(url, path)
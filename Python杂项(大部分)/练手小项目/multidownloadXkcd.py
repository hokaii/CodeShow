#! python3
#项目：多线程XCDK下载漫画
import requests,os,bs4,threading
os.makedirs('xk_cd',exist_ok=True)
def downloadXkcd(startComic,endComic):
    for urlNumber in range(startComic,endComic):
        print('Downloading page http://xkcd.com/%s...'%(urlNumber))
        res=requests.get('https://xkcd.com/%s'%(urlNumber))
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text,"html.parser")
        comicElem=soup.select('#comic img')
        if comicElem==[]:
            print('Could not find comic image.')
        else:
            comicUrl='https:'+comicElem[0].get('src')
            print('Downloading image %s...'%(comicUrl))
            res=requests.get(comicUrl)
            res.raise_for_status()
            imageFile=open(os.path.join('xk_cd',os.path.basename(comicUrl)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

downloadThreads=[]
for i in range(0,400,100):
    downloadThread=threading.Thread(target=downloadXkcd,args=(i,i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')

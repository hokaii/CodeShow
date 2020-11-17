#引入库
import pyaudio
import wave
#定义数据流块
CHUNK=1024
#只读方式打开WAV文件
wf=wave.open(r'H:\Python\Python3.6.6\MyPythonScripts\WelcomeHomeSir.WAV','rb')
p=pyaudio.PyAudio()
#打开数据流
stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
#读取数据
data=wf.readframes(CHUNK)
#播放
while data!='':
	stream.write(data)
	data=wf.readframes(CHUNK)
#停止数据流
stream.stop_stream()
stream.close()
#关闭PyAudio
p.terminate()
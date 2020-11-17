#coding:utf-8
import sys,importlib
import pyttsx3

importlib.reload(sys)

engine=pyttsx3.init()
volume=engine.getProperty('volume')#音量控制
engine.setProperty('volume',volume-0.25)
rate=engine.getProperty('rate')#语速控制
engine.setProperty('rate',rate+50)
#voice=engine.getProperty('voice')#更换发音人声音
#engine.setProperty('voice',voice.id)
#voice=engine.getProperty('voice')
#engine.setProperty('voice',gender)
engine.say('hello world')
engine.say('你好,我是')
engine.runAndWait()
#朗读一次
engine.endLoop()
#coding=utf-8
from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):   #从Frame派生一个Application类
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()   #pack方法把Widget加入到父容器中，并实现布局
        self.createWidgets()
    
    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.quitButton=Button(self,text='Hello',command=self.hello)
        self.quitButton.pack()
    
    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello, %s'%name)

app=Application()
app.master.title("Hello world")
app.mainloop()   #示例化application
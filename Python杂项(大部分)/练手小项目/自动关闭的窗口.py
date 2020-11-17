import time
import tkinter
import threading

#创建应用程序窗口,设置标题和大小
root=tkinter.Tk()
root.title('倒计时自动关闭的窗口')
root['width']=400
root['height']=300
#不允许改变窗口大小
root.resizable(False,False)

#创建Text组件,放置一些文字
richText=tkinter.Text(root,width=380)
richText.place(x=10,y=10,width=380,height=230)
richText.insert('0.0','假设阅读这些文字需要10秒钟时间')

#显示倒计时的Label
lbTime=tkinter.Label(root,fg='red',anchor='w')
lbTime.place(x=10,y=250,width=150)

def autoClose():
	for i in range(10):
		lbTime['text']='距离窗口关闭还有{}秒',format(10-i)
		time.sleep(1)
	root.destroy()

#创建并启动线程
t=threading.Thread(target=autoClose)
t.start()
root.mainloop()
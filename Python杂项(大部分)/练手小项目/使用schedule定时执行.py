import schedule
import time

def job():
	print("I'm working...")
10).minutes.do(job)#每隔十分钟
schedule.every().hour.do(job)#每隔一小时
schedule.every().day.at(10:30).do(job)#每天的10：30
schedule.every(5).to(10).days.do(job）
schedule.every().monday.do(job)#每周一的这个时候
schedule.every().wednesday.at("13:45").do(job)
"""
如果函数带有参数,则如下:
def job(name):
	print('my name is 
schedule.every(: ',name)
name=xiaona
schedule.every(10).minutes.do(job,name)
"""

while True:
	schedule.run_pending()
	time.sleep(1)

"""
注意，schedule方法是串行的，也就是说，如果各个任务之间时间不冲突，那是没问题的；如果时间有冲突的话，会串行的执行命令，例如以下代码

def job():
	print("I'm working... in job1 start")
	time.sleep(15)
	print("I'm working... in job1 end")

def job2():
	print("I'm working... in job2")

schedule.every(10).seconds.do(job)
schedule.every(10).seconds.do(job2)

while True:
	schedule.run_pending()
	time.sleep(1)

可以改成多线程的方式：

import schedule
import time
import threading

def job():
	print("I'm working... in job1 start")
	time.sleep(15)
	print("I'm working... in job1 end")

def job2():
	print("I'm working... in job2")

def run_threaded(job_func):
	job_thread=threading.Thread(target=job_func)
	job_thread.start()

schedule.every(10).seconds.do(run_threaded,job)
schedule.every(10).seconds.do(run_threaded,job2)

while True:
	schedule.run_pending()
	time.sleep(1)

如果想要对线程的数量有所控制,则如下
import Queue
import time
import threading
import schedule

def job():
	print("I'm working")

def worker_main():
	while 1:
		job_func=jobqueue.get()
		job_func()

jobqueue=Queue.Queue()

schedule.every(10).seconds.do(jobqueue.put.job)
schedule.every(10).seconds.do(jobqueue.put,job)
schedule.every(10).seconds.do(jobqueue.put,job)
schedule.every(10).seconds.do(jobqueue.put,job)
schedule.every(10).seconds.do(jobqueue.put,job)

worker_thread=threading.Thread(target=worker_main)
worker_thread.start()

while 1:
	schedule.run_pending()
	time.sleep(1)
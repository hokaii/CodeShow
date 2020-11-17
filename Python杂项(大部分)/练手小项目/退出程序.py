import os,sys

#sys.exit()
#sys.exit()的退出会引发SystemExit异常,可以捕获此异常
try:
	sys.exit(0)
except:
	print('die')
finally:
	print('cleanup')

#os._exit()
#os._exit()直接将Python解释器退出,余下的语句不会执行
try:
	os._exit(0)
except:
	print('die')
print('os.exit')

"""
一般来说os._exit()用于在线程中退出
sys.exit()用于在主线程中退出

exit(0)和exit(1)
exit(0):无错误退出
exit(1):有错误退出
退出代码是告诉解释器的(或操作系统)
"""
#! python3
#项目：简单的倒计时程序
import time,subprocess
timeLeft=60
while timeLeft>0:
    print(timeLeft,end='')
    time.sleep(1)
    timeLeft=timeLeft-1
subprocess.Popen(['start','Welcome Home Sir.wav'],shell=True)
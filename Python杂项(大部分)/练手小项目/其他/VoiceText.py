import requests
import time
import hashlib
import base64
import win32com.client
# https://www.cnblogs.com/warcraft/p/10112486.html
# https://ai.baidu.com/docs#/ASR-Online-Python-SDK/b3e9a8da
# https://console.xfyun.cn/app/myapp?currPage=1&keyword=


class VoiceText:
    def __init__(self):
        self.url = "http://api.xfyun.cn/v1/service/v1/iat"
        self.app_id = "5c921fd5"
        self.api_key = "23ff11a03aa43eed379ecd4e43db16b5"

    def speaker(self, s):
        speak = win32com.client.Dispatch("SAPI.SpVoice")



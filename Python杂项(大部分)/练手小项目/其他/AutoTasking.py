from pyautogui import screenshot
from datetime import datetime
from win32api import RegOpenKeyEx
from win32api import RegSetValueEx
from win32gui import SystemParametersInfo
from win32con import HKEY_CURRENT_USER
from win32con import REG_SZ
from win32con import SPI_SETDESKWALLPAPER
from win32con import KEY_SET_VALUE
from win32con import SPIF_SENDWININICHANGE
from os import path
from PIL.Image import open


class AutoTasking:
    def __init__(self):
        self.addr = './file/screen_shot/'

    def screenshot(self):  # 返回截图图片保存的地址
        shot = datetime.now().strftime('%Y%b%d_%H%M')
        im = screenshot()
        # im.show()
        address = self.addr + shot + '.png'
        im.save(address)
        return address

    def change_my_wall(self, addr='E:\\MySripts\\default.jpg'):
        self.__set_wallpaper(addr)
        print("change wall successfully!")
        return None

    def __set_wallpaper_from_bmp(self, bmp_path):
        reg_key = RegOpenKeyEx(HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, KEY_SET_VALUE)
        RegSetValueEx(reg_key, "WallpaperStyle", 0, REG_SZ, "2")
        RegSetValueEx(reg_key, "TillWallpaper", 0, REG_SZ, "0")
        SystemParametersInfo(SPI_SETDESKWALLPAPER, bmp_path, SPIF_SENDWININICHANGE)

    def __set_wallpaper(self, img_path):
        img_dir = path.dirname(img_path)
        bmpImage = open(img_path)
        new_bmp_path = path.join(img_dir, 'wallpaper.bmp')
        bmpImage.save(new_bmp_path, "BMP")
        self.__set_wallpaper_from_bmp(new_bmp_path)


if __name__ == '__main__':
    atuo = AutoTasking()
    print(atuo.screenshot())

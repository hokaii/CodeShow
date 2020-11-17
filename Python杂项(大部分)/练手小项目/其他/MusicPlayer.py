"""
2019/6/9
"""
from os import path
from PyQt5.QtWidgets import *


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.__initialize()
    """初始化"""
    def __initialize(self):
        self.setWindowTitle("音乐播放器 v0.1")
        #self.setWindowIcon(QIcon('icon.ico'))
        self.songs_list = []
        self.song_formats = ['mp3', 'm4a', 'flac', 'wav', 'ogg']
        self.setting_filename = 'setting.ini'
        self.player = QMediaPlayer()
        self.cur_path = path.abspath(path.dirname(__file__))
        self.cur_playing_song = ''
        self.is_switching = False
        self.is_pause = True
        """界面元素"""
        """--播放时间"""
        self.label1 = QLabel('00:00')
        self.label1.setStyle(QStyleFactory.create('Fusion'))
        self.label2 = QLabel('00:00')
        self.label2.setStyle(QStyleFactory.create('Fusion'))
        """滑动条"""
        self.slider = QSlider(Qt.Horizontal, self)
        self.play_button = QPushButton('播放', self)
        self.play_button.clicked.connect(self.playMusic)
        self.play_button.setStyle(QStyleFactory.create('Fusion'))
        """--播放按钮"""
        self.play_

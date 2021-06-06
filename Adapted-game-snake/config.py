import pygame
import os
from math import *

# pygame初始化
pygame.init()

# 常用环境变量，分别是鼠标角度，x位置，y位置，以及是否按下
env = {"mouse_direction": 0, "mouse_x": 0, "mouse_y": 0, "mouse_down": False}

# 屏幕长宽，初始化屏幕
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))

# 聊天框字体
chat_font_size = 20
chat_font = pygame.font.Font("sanji.ttf", chat_font_size)

# 等级显示字体，同时也是纯文本场景字体
level_font = pygame.font.Font("sanji.ttf", 40)

# 计时器
clock = pygame.time.Clock()

# 设置显示title
pygame.display.set_caption('SnakeQuest')


# helper函数，获取两点间的距离
def get_distance(p1, p2):
    d1, d2 = p1[0] - p2[0], p1[1] - p2[1]
    return sqrt(d1*d1 + d2*d2)


# helper函数，获取角度
def get_angle(x, y):
    return atan2(y, x)


# 获取材质文件夹下的所有材质名
textures = os.listdir("texture")


# helper函数，读取一个材质
def load(n):
    return pygame.image.load(os.path.join("texture", n + ".png")).convert_alpha()


# 将所有材质名解为的png去掉，为统一格式
texture_names = [name[:-4] for name in textures]

# 空字典用于存储所有材质
texture_lib = {}

# 读取所有材质
for name in texture_names:
    texture_lib[name] = load(name)


class AudioPlayer:
    """
    音乐音效播放器，一共有三个频道，分别是背景音乐(background music)，音效(sound effect)，以及蛇(snake)，
    音频文件必须是ogg格式，id_in为文件名，type_in为频道，volume可调音量
    """
    def __init__(self, id_in, type_in, volume=0.2):
        self.id = id_in
        self.music = pygame.mixer.Sound(os.path.join('audio', id_in + '.ogg'))
        self.music.set_volume(volume)
        if type_in == "bg":
            self.channel = pygame.mixer.Channel(1)
        if type_in == "se":
            self.channel = pygame.mixer.Channel(2)
        if type_in == "sn":
            self.channel = pygame.mixer.Channel(3)

    # 无限循环播放
    def play_non_stop(self):
        self.channel.play(self.music, -1)

    # 播放一次
    def play_once(self):
        self.channel.play(self.music, 0)

    # 停止当前频道
    def stop(self):
        self.channel.stop()


# 初始化所有背景音乐
bgs = (AudioPlayer("menubg", "bg"),
       AudioPlayer("gamebg", "bg"),
       AudioPlayer("gamebg2", "bg"),
       AudioPlayer("chat", "bg"),
       AudioPlayer("map", "bg", volume=0.06))

# 初始化所有音效
ses = (AudioPlayer("sebigcannon", "se"),
       AudioPlayer("sebutton", "se"),
       AudioPlayer("seeat", "sn"),
       AudioPlayer("sehit", "sn"),
       AudioPlayer("selevelup", "sn"),
       AudioPlayer("sesmallcannon", "se"),
       AudioPlayer("sebeam", "se"),
       AudioPlayer("sechat", "se"))

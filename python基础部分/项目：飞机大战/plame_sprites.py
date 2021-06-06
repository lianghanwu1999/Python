# -*- coding: utf-8 -*-

"""
@project: 飞机大战
@author: 梁汉武
@file: plane_main.py
@ide: PyCharm
"""
"""
导入模块顺序
1.官方标准模块
2.第三方模块
3.应用程序模块导入
"""

import random
import pygame
#TODO 常量设置（全部大写）
#设置屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
#定义刷新的帧率的常量
FRAME_PER_SEC = 60
#TODO （定时器设置，第一步：设置常量）
#创建敌机的定时器常量  (定时器：USEREVENT这个是用户事件名)
CREATE_ENEMY_EVENT = pygame.USEREVENT
#英雄发射子弹事件
HERO_FIRE_EVENT =pygame.USEREVENT + 1      #用户事件名已经被使用，为了区分，可以在后面 +1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏的精灵"""
    def __init__(self,image_name,speed=1):

        #调用父类的初始化方法：子类的父类不是object的基类
        #在初始化方法中主动调用父类的初始化方法
        # 不然就没法享受父类封装好的方法
        super().__init__()

        #定义对象属性
        self.image = pygame.image.load(image_name)  #加载图像
        self.rect = self.image.get_rect()  #绘制对象图像位置
        self.speed =speed     #控制对象速度

    def update(self): #提供update方法，根据游戏需求，更新位置rect
        #在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):   # 继承父类GemeSprite
    """游戏背景精灵"""
    def __init__(self,is_alt = False):   #is_alt = False 表示创建的为第一张图像，叠加在屏幕上方
                                         #is_alt  = True  表示另一张的图片
        #1.调用父类方法实现精灵的创建（images/rect/speed）
        super().__init__("./images/background.png")

        #2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:     #is_alt 交替图像，这里判断是否是交替图像， 这里is_alt =False ，不是交替图像，则执行不修改图像位置。
            self.rect.y = -self.rect.height                 #若输入为True  时，则判断为交替图像，则执行循环，交替图像位置。


    def update(self):   #定义了一个update的方法：对对象进行更新
    #1.调用父类的方法实现
        super().update()  #重新父类方法，在子类方中重新父类，既可以调用父类所具有的方法：super().子类方法名  重新父类

    #2.判断是否移出屏幕，如果移出屏幕，将图像设置在屏幕正上方

        if self.rect.y  >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height



class Enemy(GameSprite): #继承gamesprite 的父类方法
    """敌机精灵"""
    def __init__(self):
        #1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")
        #2.指定敌机的初始随机速度
        self.speed = random.randint (1,3)  #randint() 方法接受区间的随机数
        #指定敌机的初始随机位置
        self.rect.bottom = 0

        #x轴最大值  = 屏幕宽度 -当前图像（飞机自身）的宽度
        max_x =SCREEN_RECT.width - self.rect.width
        # 定义敌机的随机水平位置
        self.rect.x =random.randint(0,max_x)

    def update(self):
        #1.调用父类方法，保持垂直方向的飞行
        super().update()
        #2.判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组删除。。。")

            #kill方法可以将精灵从所有精灵组中移除精灵会自动销毁
            self.kill()      #kill()可以销毁对象，同时让对象在内存中删除

    #__del__内置方法会在对象被销毁前调用，在开发中，可以用于判断对象是否被销毁（可以返回字符串可以可以输出print（））
    def __del__(self):
        # print("敌机挂了 %s " % self.rect)   #输出敌机挂了的情况并且输出敌机销毁的位置
        pass

class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        #调用父类方法，继承父类的方法，同时增添自己的方法，images$speed速度
        super().__init__("./images/me1.png",0)
        #2.设置英雄的初始位置:centerx 函数为中心位置
        self.rect.centerx = SCREEN_RECT.centerx        #英雄的中心位置= 屏幕的中心位置
        self.rect.bottom = SCREEN_RECT.bottom - 120    #bootom：与窗口上边界的距离 + 图像本身的高度(height)，这里是英雄图像 距边界的距离为120

        #3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):  #重新update方法 ，因继承的父类update方法，只有上下垂直移动，不满足需求。

        #英雄在水平方法移动：  将水平移动与速度进行叠加。
        # 当speed为负数时 ，叠加结果越来越小，则x轴 减少，向左移动
        # 当speed为负数时 ，叠加结果越来越大，则x轴 增大，向右移动
        # 当speed为0时 ，叠加结果不变，则x轴 不变，不移动
        self.rect.x += self.speed
        #添加上下移动操作
        self.rect.y += self.speed

        #TODO 控制英雄不能离开屏幕
        if self.rect.x < 0 :   #判断飞机位置是否超越 x = 0,跳出边界
            self.rect.x = 0  #调整飞机位置，回正

        elif self.rect.right > SCREEN_RECT.right:    #判断飞机位置右侧是否超越 屏幕的右侧
            self.rect.right = SCREEN_RECT.right      #回正到屏幕的右侧



    def fire(self):        # 发射子弹方法
        print("发射子弹。。。")
        for i in(0,1,2):
            #1.创建子弹精灵
            bullet = Bullet()
            #2.设置精灵的位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx

            #3.将精灵添加到精灵组
            self.bullets.add(bullet)

class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        #调用父类方法，设置子弹图片,设置初始速度。
        super().__init__("./images/Bullet1.png", -2)  #将子弹速度设置成负值，子弹就会向上发射。

    def update(self):   #重写update方法，增加所需要的功能
        #调用父类方法，让子弹沿着垂直方向飞行
        super().update()

        #判断子弹是否飞出屏幕
        if self.rect.bottom <0 :
            self.kill()      #飞出屏幕的子弹进行销毁
    def __del__(self):
        """添加坠毁效果"""
        print("子弹被销毁。。。。")




#补充：
"""
调用 .rect 方法 本身具有的属性：
x,y, 
方向大小：lef,top,bottom,right   其中：right = x + width
center ,centerx ,cetery 
size,width,height 

"""
"""
设置定时器的三个步骤：
1.在表头有大写字母设置定时器常量
2.在初始化方法中，调用set_timer 方法，设置定时器事件
3.在游戏循环中监听定时器。
"""



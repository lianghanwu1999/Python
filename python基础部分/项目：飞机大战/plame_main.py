# -*- coding: utf-8 -*-


"""
@project: 飞机大战
@author: 梁汉武
@file: plane_main.py
@ide: PyCharm
"""

import pygame
from plame_sprites import *    #调用plame_sprites模块内的所有工具。

class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        #1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size) #"""调用设置屏幕的元组数据""" # 定义常量：用大写字母

        #2.创建游戏的时钟
        self.clock = pygame.time.Clock()

        #3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        #设置定时器事件
        # -创建敌机 出现间隔时间，每秒出现一次 定时器单位为1毫秒  1s = 1000 ms
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        #英雄发射子弹时间
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

     #TODO （）定义一个私有方法，创建精灵与精灵组
    def __create_sprites(self):

        #TODO 创建背景精灵和精灵组

        #TODO 创建背景精灵
        bg1 = Background()       #调用plame_sprites 所创建的背景类background,背景类默认为is_alt = Flase 叠加在屏幕上方
        bg2 = Background(True)   #这里为True 为 is_alt = True  在palme_sprite 判断为另一张图片。
                                 # 是交替背景，则if 执行变换位置

        #TODO 创建背景精灵组：调用某个方法时，精灵也随之改变
        self.back_group = pygame.sprite.Group(bg1,bg2)

        #TODO 创建敌机的精灵组
        self.enemy_group =pygame.sprite.Group()

        #TODO 创建英雄精灵和精灵组
        self.hero = Hero()    #：由于英雄要调用到其他地方，所以将英雄定义为属性
        self.hero_group = pygame.sprite.Group(self.hero)    #创建精灵组






#TODO （游戏循环，游戏主体）
    def start_game(self):
        print("游戏开始。。。")

        while True:      #为什么游戏屏幕会一闪而过，因为没有设置while循环使得游戏屏幕一直循环刷新下去
                         #设置循环以下方法，让在游戏内可以调用。
            #1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            #2.事件监听
            self.__event_handler()
            #3.碰撞检测
            self.__check_collide()
            #4.更新/绘制精灵组
            self.__update_sprites()
            #5.更新显示
            pygame.display.update()

    #TODO 定义事件监听的方法:即是记录玩家的操作记录
    def __event_handler(self):
        #记录事件列表，用for循环遍历打印，获取事件记录
        for event in pygame.event.get():
            #判断是否退出游戏
            if event.type == pygame.QUIT:
                #如果是就可以调用退出游戏的静态方法
                PlaneGame.__game_over()   #调用静态方法，类名加方法名，或用 self.静态方法名
                #方法2：self.__game_over()

            #设置监听事件
            elif event.type == CREATE_ENEMY_EVENT:
                #print("敌机出场 ")
                #创建敌机精灵
                enemy =Enemy()

                #将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            # 设置监听事件：监听发射子弹时间
            elif event.type ==HERO_FIRE_EVENT:
                #创建子弹精灵
                self.hero.fire()

            #方法1.键盘按键捕获： 事件捕获方法，缺点，按下抬起为一次，灵活性差
            # elif event.type ==pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动。。。")

        #TODO (按键获取) 方法2：使用键盘模块提供的方法捕获键盘按键  通过返回的一个元组，捕获用户操作信息
        kes_passed = pygame.key.get_pressed()
        #判断元组中对应的按键索引值  TODO [灵敏度设置] 数值越大，灵敏度越高。
        if kes_passed[pygame.K_RIGHT]:
            self.hero.speed = 4

        elif kes_passed[pygame.K_LEFT]:
            self.hero.speed = -4

        else:
            self.hero.speed = 0


    #定义碰撞检测方法
    def __check_collide(self):
        # pygame.sprite.groupcollide(group1,group2,dokill1,dokill2,collided = None )方法
        #将dokill1 设置为True，则第几个group 发生碰撞会被自动移除，设置false 则是不会。
        # 两个精灵组中所有精灵的碰撞检测：
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        #2.敌机列表撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group,True)
        #精灵组和精灵碰撞（self.hero（精灵组） , self.enemy_group （精灵）, True（确认发生碰撞后移除））
        #判断列表是否有内容
        if len(enemies) > 0:
            #英雄牺牲
            self.hero.kill()
            #结束游戏
            PlaneGame.__game_over()



    #TODO 更新精灵组方法
    def __update_sprites(self):

        self.back_group.update()            #更新背景精灵组
        self.back_group.draw(self.screen)  #draw() 方法就是让更新的东西绘制在屏幕上

        self.enemy_group.update()           #更新敌机精灵组
        self.enemy_group.draw(self.screen)  #绘制敌机在屏幕上（draw() 绘制方法，把敌机绘制到哪里）

        self.hero_group.update()            #更新英雄精灵组
        self.hero_group.draw(self.screen)   #绘制英雄在屏幕上

        self.hero.bullets.update()           #更新英雄的子弹精灵组
        self.hero.bullets.draw(self.screen)  #绘制子弹在屏幕上

    #游戏退出的静态方法。
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()



#TODO 测试代码，这个函数的代码，只能在main内部执行，其他的调用也执行不了
if __name__ == '__main__':

    #创建游戏对象
    game = PlaneGame()
    #启动游戏
    game.start_game()



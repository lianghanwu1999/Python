# -*- coding: utf-8 -*-

"""
@project: 飞机大战
@author: EricNiu
@file: plane_main.py
@ide: PyCharm
"""


import random
import pygame

# 一些游戏基本信息
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
HERO_MOVE_SPEED = 4
# Image（提前指定照片为某个名称）
BACKGROUND_IMAGE = "./images/background.png"
ENEMY_IMAGE_1 = "./images/enemy1.png"
ENEMY_IMAGE_2 = "./images/enemy2.png"
HERO_IMAGE_1 = "./images/me1.png"
HERO_IMAGE_2 = "./images/me2.png"
ENEMY_CRASH_IMAGE_1 = "./images/enemy1_down{}.png"
ENEMY_CRASH_IMAGE_2 = "./images/enemy2_down{}.png"
HERO_CRASH_IMAGE = "./images/me_destroy_{}.png"
# Event
CREATE_ENEMY_EVENT_1 = pygame.USEREVENT
CREATE_ENEMY_EVENT_2 = pygame.USEREVENT + 1
HERO_FIRE_EVENT = pygame.USEREVENT + 2
ENEMY_FIRE_EVENT = pygame.USEREVENT + 3
ELITE_ENEMY_CRASH_EVENT = pygame.USEREVENT + 4


class GameSprite(pygame.sprite.Sprite):
    """
    飞机大战游戏精灵
    """
    def __init__(self, image_name, speed=1):
        # 游戏精灵初始化
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 更新精灵位置
        self.rect.y += self.speed


class BackGround(GameSprite):
    """
    游戏背景精灵
    """
    def __init__(self, is_alt=False):
        # 游戏背景
        super().__init__(BACKGROUND_IMAGE)
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 背景循环向下位移
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """
    敌机精灵
    """
    def __init__(self, image_name, max_speed):
        """
        普通的杂鱼敌机
        :param image_name: 敌机的贴图
        :param max_speed: 敌机最大速度
        """
        super().__init__(image_name)
        self.rect.y = -self.rect.height
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.speed = random.randint(1, max_speed)

    def update(self):
        # 敌机飞出边界后会自动销毁
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        # Debug用log
        print("敌机坠毁于{}".format(self.rect))


class EnemyElite(Enemy):
    """
    敌机精英精灵，继承自普通敌机精灵类
    """
    def __init__(self, image_name, max_speed):
        super().__init__(image_name, max_speed)
        self.health_point = 3 # 精英敌机生命值设置为3
        self.hit_flag = False

    def update(self):
        # 被击中时更换贴图，实现动画效果。HP - 1
        if self.hit_flag:
            self.image = pygame.image.load("./images/enemy2_hit.png")
            self.health_point -= 1
            self.hit_flag = False

        else:
            self.image = pygame.image.load(ENEMY_IMAGE_2)

        if self.health_point <= 0:
            # HP为0时抛出坠机event，event附带字典参数传递坠机位置。
            event = pygame.event.Event(ELITE_ENEMY_CRASH_EVENT, {"loc": self.rect})
            pygame.event.post(event)
            self.kill()

        super().update()

    def fire(self, bullets_group):
        """
        敌机开火函数
        :param bullets_group:子弹将加入这个精灵组
        :return: None
        """
        print("发射！")
        bullet = Bullet("./images/bullet2.png", 2)
        bullet.rect.top = self.rect.y + self.rect.height + 5
        bullet.rect.centerx = self.rect.centerx + 1
        bullets_group.add(bullet)

    def get_hit(self):
        # 更改击中状态的函数
        self.hit_flag = True


class Hero(GameSprite):
    """
    英雄精灵
    """
    __flag = True # 实现英雄飞机小动画的标识

    def __init__(self):
        super().__init__(HERO_IMAGE_1)
        self.speed_x = 0
        self.speed_y = 0
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 实现两张英雄贴图的交替
        if self.__flag:
            self.image = pygame.image.load(HERO_IMAGE_2)
            self.__flag = not self.__flag
        else:
            self.image = pygame.image.load(HERO_IMAGE_1)
            self.__flag = not self.__flag
        # 实现英雄的位移
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # 防止英雄出界
        if self.rect.x < -40:
            self.rect.x = -40
        elif self.rect.x > SCREEN_RECT.width - self.rect.width + 40:
            self.rect.x = SCREEN_RECT.width - self.rect.width + 40

        if self.rect.y < 10:
            self.rect.y = 10
        elif self.rect.y > SCREEN_RECT.height - self.rect.height + 40:
            self.rect.y = SCREEN_RECT.height - self.rect.height + 40

    def fire(self):
        # 英雄开火
        # for i in (0, 1):
        bullet = Bullet("./images/bullet1.png", -4)
        bullet.rect.bottom = self.rect.y - 18 # i * 18
        bullet.rect.centerx = self.rect.centerx + 1
        self.bullets.add(bullet)


class Bullet(GameSprite):
    """
    子弹精灵
    """
    def __init__(self, image_name, speed):
        super().__init__(image_name, speed)

    def update(self):
        super().update()
        # 敌机的子弹飞出界外也要子弹销毁
        if self.rect.bottom < 0 or self.rect.top > 700:
            self.kill()


class Blast(GameSprite):
    """
    爆炸动画精灵
    """
    counter = 1

    def __init__(self, blast_loc, image_name, frame_num):
        """
        爆炸动画的初始化
        :param blast_loc:爆炸的位置，Rect对象
        :param image_name:爆炸的贴图组名称
        :param frame_num:动画的帧数(爆炸动画有几张贴图)
        """
        super().__init__(image_name.format(1), 0)
        self.image_name = image_name
        self.frame_num = frame_num
        self.rect.x = blast_loc.centerx - (self.rect.width / 2)
        self.rect.y = blast_loc.centery - (self.rect.height / 2)

    def update(self):
        # 逐张更新爆炸贴图 简单定义一个计数器就可以了
        if self.counter > self.frame_num:
            self.kill()
        else:
            self.image = pygame.image.load(self.image_name.format(self.counter))
            self.counter += 1


class GameOver(GameSprite):
    """
    游戏结束精灵
    """
    def __init__(self):
        # 在屏幕中央显示结束游戏
        # 可以加入游戏重来的功能 也可以重新实现游戏暂停和恢复
        super().__init__("./images/gameover.png", 0)
        self.rect.x = SCREEN_RECT.centerx - self.rect.width / 2
        self.rect.y = SCREEN_RECT.centery - self.rect.height / 2


if __name__ == '__main__':
    print("飞机大战游戏精灵类及常量")

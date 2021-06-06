#coding=utf-8
import pygame
from pygame.locals import *
import time
import random
#飞机基类和子弹基类的基类
class Base(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)

#飞机基类
class BasePlane(Base):
    def __init__(self, screen_temp, x, y, image_name):
        Base.__init__(self,screen_temp,x,y,image_name)
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge(): #判断子弹是否越界
                self.bullet_list.remove(bullet)
#子弹基类
class BaseBullet(Base):
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

#玩家飞机类
class HeroPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp,205,700,"./images/hero1.png")
        self.key_right_status = False
        self.key_left_status = False
        self.key_up_status = False
        self.key_down_status = False

    def move(self):   #移动方法
        if self.key_right_status:
            self.x += 3
        if self.key_left_status:
            self.x -= 3
        if self.key_down_status:
            self.y += 3
        if self.key_up_status:
            self.y -= 3

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

#敌机类
class EnemyPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp,0,0,"./images/enemy0.png")
        self.direction = "right"#控制敌机默认显示方向

    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5
        if self.x > 420:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1,50)
        if random_num == 20 or random_num == 21:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))

#玩家子弹类
class Bullet(BaseBullet):
    def __init__(self, screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp,x+40,y-20,"./images/bullet.png")

    def move(self):
        self.y -= 10

    def judge(self):
        if self.y <  0:
            return True
        else:
            return False

#敌机子弹类
class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp,x+22,y+30,"./images/bullet1.png")

    def move(self):
        self.y += 10

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False

#键盘控制函数
def key_control(hero_temp):
    #获取事件，比如按键等
    for event in pygame.event.get():

        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.key_left_status = True
                #hero_temp.move_left()
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.key_right_status = True
                #hero_temp.move_right()
            #检测按键是否是w或者up
            elif event.key == K_w or event.key == K_UP:
                hero_temp.key_up_status = True
            #检测按键是否是s或者down
            elif event.key == K_s or event.key == K_DOWN:
                hero_temp.key_down_status = True
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()
        #判断是否是松了键
        elif event.type == KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                hero_temp.key_left_status = False
            elif event.key == K_d or event.key == K_RIGHT:
                hero_temp.key_right_status = False
            elif event.key == K_w or event.key == K_UP:
                hero_temp.key_up_status = False
            elif event.key == K_s or event.key == K_DOWN:
                hero_temp.key_down_status = False

def main():
    #1. 创建窗口
    screen = pygame.display.set_mode((480,852),0,32)

    #2. 创建一个背景图片
    background = pygame.image.load("./images/background.png")

    #3. 创建一个飞机对象
    hero = HeroPlane(screen)

    #4. 创建一个敌机
    enemy = EnemyPlane(screen)
    while True:
        screen.blit(background, (0,0))
        hero.display()#显示玩家飞机
        enemy.display()#显示敌机
        hero.move()#玩家飞机移动
        enemy.move()#敌机移动
        enemy.fire()#敌机开火
        pygame.display.update()
        key_control(hero)#控制方向
        time.sleep(0.01)#防崩

if __name__ == "__main__":
    main()
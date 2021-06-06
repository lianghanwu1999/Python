import pygame

#TODO 游戏的初始化
#初始化
pygame.init()

#创建游戏窗口 480 * 700
#创建窗口的方法：set_mode方法 ：pygame.display.set_mode(resolution(0,0),flags =0 ,depth = 0)
#resolution 指定屏幕的高和宽
#flags 指定屏幕附加项， depth 屏幕颜色，默认自动匹配 可以忽略。

screen = pygame.display.set_mode((480,700))

#绘制背景图像  ：导入照片背景
#1> 加载图像数据
bg = pygame.image.load("./images/background.png")
#2.调用blit 绘制图像
screen.blit(bg,(0,0))  #左上角为原点位置坐标


#绘制英雄飞机图像
#1.加载图像
hero = pygame.image.load("./image/me1.png")  #导入图片文件地址
#2.绘制在屏幕
screen.blit(hero,(200,500))



#刷新显示，可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()


#TODO 游戏循环 -》 意味着游戏真正开始 ！
#while True 循环的目的是让游戏窗口一直保持下去

i=0
while True:
    #clock.tick() 方法可以指定循环体内部的代码执行的频率
    # 定义游戏时钟可以设置游戏的刷新率：
    
    clock.tick(60)   #设置刷新率60帧


#结束游戏
pygame.quit()
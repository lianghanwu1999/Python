import pygame

#初始化
pygame.init()

#创建游戏窗口 480 * 700
#创建窗口的方法：set_mode方法 ：pygame.display.set_mode(resolution(0,0),flags =0 ,depth = 0)
#resolution 指定屏幕的高和宽
#flags 指定屏幕附加项， depth 屏幕颜色，默认自动匹配 可以忽略。

screen = pygame.display.set_mode((480,700))

#while True 循环的目的是让游戏窗口一直保持下去
while True:
    pass

#结束游戏
pygame.quit()

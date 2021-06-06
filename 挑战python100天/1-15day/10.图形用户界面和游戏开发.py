"""
#TODO  GUI开发
基本上使用tkinter来开发GUI应用需要以下5个步骤：
1.导入tkinter模块中我们需要的东西。
2.创建一个顶层窗口对象并用它来承载整个GUI应用。
3.在顶层窗口对象上添加GUI组件。
4.通过代码将这些GUI组件的功能组织起来。
5.进入主事件循环(main loop)。
# """
#TODO GUI应用(小窗口)

import tkinter  #导入tk模块开发GUI
import tkinter.messagebox

def main():
    flag = True

    #修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color , msg = ('red','Hello,world')\
            if flag else ('blue','Goodbye,world')
        label.config(text=msg, fg=color)

    #确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温情提示','确定要退出吗？'):
            top.quit()

    #创建顶层窗口
    top = tkinter.Tk()
    #设置窗口大小
    top.geometry('240x160')
    #设置窗口标题
    top.title('小游戏')
    #创建标签对象并添加到顶层窗口
    label = tkinter.Label(top,text='Hello,world!',font='Arial -32',fg='red')
    label.pack(expand=1)
    #创建一个装按钮的容器
    panel = tkinter.Frame(top)
    #创建对象，指定添加到那个容器，通过command（命令）回调想要执行的功能。
    button1 = tkinter.Button(panel,text='修改',command=change_label_text)
    #显示窗口
    button1.pack(side='left')
    button2 = tkinter.Button(panel,text='退出',command=confirm_to_quit)
    button2.pack(side='right')
    #显示容器
    panel.pack(side='bottom')
    #开启主事件循环
    tkinter.mainloop()

if __name__ == '__main__':
    main()
#
# #
# #TODO 绘制游戏窗口
# import pygame
# def main():
#     #初始化导入的pygame中模块
#     pygame.init()
#     #初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800,600))
#     #设置当前窗口标题
#     pygame.display.set_caption('大球吃小球')
#     running = True
#     #开启一个事件循环处理发生的事件
#     while running:
#         #从信息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:    #结束
#                 running = False
#
# if __name__ == '__main__':
#     main()
#
# #TODO 屏幕坐标系是将屏幕左上角设置为坐标原点(0, 0)，向右是x轴的正向，向下是y轴的正向，
# # 在表示位置或者设置尺寸的时候，我们默认的单位都是像素
#
# #TODO 在窗口中绘图
# import pygame
# def main():
#     #初始化导入的pygame中的模块
#     pygame.init()
#     #初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800,600))
#     #设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     #TODO 设置窗口的背景色（颜色是由红绿蓝三原构成的元组）
#     screen.fill((242,242,242))     #通过screen.fill()来填充背景色，其中的参数为(R,G,B)
#     #TODO 绘制一个圆（参数分别是：屏幕，颜色，圆心位置，半径，0表示填充圆）
#     pygame.draw.circle(screen,(255,0,0),(100,100),30,0)
#     #TODO 刷新当前窗口（渲染窗口将绘制图像呈现出来）
#     pygame.display.flip()
#     running =  True
#     while running:
#         #开启一个事件循环处理事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
# if __name__ == '__main__':
#     main()
#
# import pygame
#
# def main():
#     #初始化导入的pygame中的模块
#     pygame.init()
#     #初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800,600))
#     #设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     #设置窗口的背景色（颜色是由红绿蓝三原构成的元组）
#     screen.fill((242,242,242))     #通过screen.fill()来填充背景色，其中的参数为(R,G,B)
#     #TODO 通过指定的文件名加载图像
#     #ball_image = pygame.image.load('图片路径')
#     #TODO 在窗口上渲染图像
#     #screen.blit(ball_image,(50,50))
#     #刷新当前窗口（渲染窗口绘制图像呈现出来）
#     pygame.display.flip()
#     running = True
#     #开启一个事件循环处理发生的事件
#     while running:
#         #从消息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
# if __name__ == '__main__':
#     main()
#
# #TODO 实现动画效果
# import pygame
#
# def main():
#     #初始化导入的pygame 中的模块
#     pygame.init()
#     #初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800,600))
#     #设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     #定义变量来表示小球在屏幕上的位置
#     x,y = 50,50
#     running = True  #将running参数设置为True, 将循环默认设置为无限循环
#     #开启一个事件循环处理发生的事件进行处理
#     while running:
#         #从消息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         #设置窗口颜色
#         screen.fill((255,255,255))
#         #绘制图像
#         pygame.draw.circle(screen,(255,0,0),(x,y),30,0)
#         #屏幕刷新显示
#         pygame.display.flip()
#         #每隔50毫秒就改变小球的位置再刷新窗口
#         pygame.time.delay(50)
#         x,y = x+5 ,y+5
#
# if __name__ == '__main__':
#     main()
#
# #TODO  大球吃小球游戏
#
# #TODO 碰撞检测
# from enum import Enum,unique
# from math import sqrt
# from random import randint
#
# import pygame
#
# @unique
# class Color(Enum):
#     """颜色"""
#     RED = (255,0,0)
#     GREEN =(0,255,0)
#     BLUE = (0,0,255)
#     BLACK = (255,255,255)
#     GRAY = (242,242,242)
#
#     @staticmethod      #定义静态方法的标识
#     def random_color():
#         """获得随机颜色"""
#         #颜色用(rgb 三个变量组成，)
#         r =randint(0,255)
#         g =randint(0,255)
#         b =randint(0,255)
#         return (r,g,b)
# class Ball(object):
#     """球"""
#     def __init__(self,x,y,radius,sx,sy,color=Color.RED):
#         """初始化方法"""
#         self.x = x
#         self.y = y
#         self.radius = radius  #半径
#         self.sx = sx
#         self.sy = sy
#         self.color = color
#         self.alive = True
#
#     def move (self,screen):
#         """移动"""
#         self.x +=self.sx
#         self.y +=self.sy
#         if self.x - self.radius <= 0  or\
#             self.sx + self.radius >= screen.get_width():
#             self.sx = -self.sx
#
#         if self.y -self.radius <=0 or \
#             self.y + self.radius >= screen.get_height():
#             self.sy = -self.sy
#
#     def eat(self,other):
#         """吃掉其他球"""
#         if self.alive and other.alive and self !=other:
#             dx,dy = self.x -other.x ,self.y -other.y
#             distance = sqrt(dx ** 2 +dy ** 2)
#             if distance < self.radius + other.radius \
#                 and self.radius > other.radius:
#                 other.alive = False
#                 self.radius = self.radius + int(other.radius * 0.146)
#
#     def draw(self,screen):
#         """在窗口上绘制球"""
#         pygame.draw.circle(screen,self.color,
#                            (self.x ,self.y),self.radius,0)
#
# def main():
#     #定义用来装所有球是容器
#     balls = []
#     #初始化导入是pygame中的模块
#     pygame.init()
#     #初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800,600))
#     #设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     running = True
#     #开启一个事件循环处理发生的事件
#     while running:
#         #从消息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             #处理鼠标事件是代码
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
#                 #获得点击鼠标的位置
#                 x,y = event.pos
#                 radius = randint(10,100)
#                 sx,sy = randint(-10,10),randint(-10,10)
#                 color = Color.random_color()  #随机分配颜色
#                 #在点击鼠标的位置创建一个球（大小，速度和颜色）
#                 ball = Ball(x,y,radius,sx,sy,color )
#                 #将球添加到列表容器之中
#                 balls.append(ball)
#         screen.fill((255,255,255))
#         #取出容器中的球，如果没有被吃掉就绘制 ，被吃掉就移除
#         for ball in balls:
#             if ball.alive:
#                 ball.draw(screen)   #绘制
#             else:
#                 balls.remove(ball)  #移除
#         pygame.display.flip() #显示到屏幕上
#         #每隔50毫秒就改变球的位置再刷新窗口
#         pygame.time.delay(50)
#         for ball in balls:
#             ball.move(screen)
#             #检查球有没有吃到其他的球
#             for other in balls:
#                 ball.eat(other)
#
# if __name__ == '__main__':
#     main()






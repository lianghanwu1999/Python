#turtle模块

import turtle

# turtle.pensize(4)  #笔尖大小
# turtle.pencolor('red') #笔尖颜色
#
# turtle.forward(100) #前进 ，向什么移动多少
# turtle.right(90)    #向右偏转 多少度
#
# turtle.forward(100)
# turtle.right(90)
#
# turtle.forward(100)
# turtle.right(90)
#
# turtle.forward(100)
# turtle.right(90)

#turtle.mainloop()

"""
turtle
绘图原点为中心点，默认朝向前（右）
#导入turtle 库（绘图工具）
import turtle


笔画控住命令
up()      笔画抬起，笔头移动，不划线
down()     笔画落下，划线移动
setheading()  改变笔头朝向
pensize(大小)    改变笔画宽度
pencolor(colorstr)笔画颜色
reset()        回复所有设置，清空窗口，重置turtle
clear()        清空窗口，停留最后位置和属性
circle(r,e)    绘制半径为r的图形，e=steps=5为5边行

begin_fill()   开始填充
fillcolor(颜色)  填充颜色
end_fill()     结束填充

运动命令
forward(d) 向前移动d长度
backward(d)向后移动d长度
right(d)   向右转动多少度
left(d)    向左转动多少度
goto(x,y)  移动到（x,y）位置
speed(speed) 笔画绘制的速度

其他命令
done()   停留在结束界面
undo()    撤销上一次动作
hideturtle()  隐藏图标
showturtle()   显示图标
screensize(x,y)  屏幕大小
#画一个正方形边框（1）turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.done()
（2）
turtle.begin_fill()
turtle.fillcolor("red")
turtle.right(45)
turtle.circle(100,steps=4)
turtle.end_fill()
turtle.done()
"""
#奥运5环的绘制
turtle.pensize(10)  #笔尖大小

#第三个环
turtle.pencolor('red') #笔尖颜色
turtle.up()            #笔尖抬起
turtle.forward(200)    #前进
turtle.down()          #笔尖落下，写东西
turtle.circle(100) #半径R （画圆）

#第五个环
turtle.up()
turtle.pencolor('green') #笔尖颜色
turtle.backward(200)
turtle.down()
turtle.right(90)
turtle.circle(100)  #半径R

#第二个环
turtle.up()
turtle.pencolor('black') #笔尖颜色
turtle.left(90)
turtle.down()
turtle.circle(100)  #半径 R

#第四个环
turtle.up()
turtle.pencolor('yellow') #笔尖颜色
turtle.backward(200)
turtle.down()
turtle.right(90)
turtle.circle(100) #半径r

#第一个环
turtle.pencolor('blue') #笔尖颜色
turtle.left(90)
turtle.circle(100)
turtle.done()


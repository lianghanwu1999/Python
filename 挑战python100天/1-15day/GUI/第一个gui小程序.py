from tkinter import *
from tkinter import messagebox

"""
import Tkinter          只导入Tkinter，不包含其他模块，所以要使用时还要声明 tkinter
root = Tkinter.Tk()
或者
from Tkinter import *   表示：从Tkinter导入*（*所有东西）  不用声明
root = Tk()
都可以
"""
#创建顶层窗口
root = Tk()
btn01 = Button(root)
btn01['text'] = '点我的就送花'
btn01.pack() #布局安排组件 ，合理安排组件位置

def songhua(e):   #e 事件对象
    messagebox.showinfo('Message','送你一朵花') #窗口提示
    print('送你一朵花')

btn01.bind('<Button-1>',songhua) #绑定按钮1对象

root.mainloop() # 调用组件的mainloop()方法，进入事件2循环



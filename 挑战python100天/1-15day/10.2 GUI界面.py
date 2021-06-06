# #TODO Tkinter练习GUI界面
#
# #1.简单的GUI界面
# from tkinter import *
#
# #实例化第一个窗口
# root = Tk()
# #添加标题，对象+工具
# root.title('小游戏')
# #创建标签对象并添加到顶层窗口
# #窗体特性
# label =Label(root,text = 'Hello world')
# #配置标签其他功能
# #label.config(curror='gumby')
# label.config(width=50,heigh=10,fg='red',bg='dark green')
# #显示出来
# label.pack()
# #无限循环
# root.mainloop()
#
#
# class App():
#     def __init__(self,master):
#         frame = Frame(master)
#         frame.pack()
#
#         self.button = Button(frame,text='Exit Class' ,fg='red',command=frame.quit)
#         self.button.pack() #调用pack() 是显示出来
#
#         self.hibutton = Button(frame,text='Say Hi',command=self.Say_Hi)
#         self.hibutton.pack()
#
#     def Say_Hi(self):   #回调函数。
#         print("hi sundy ,Thanke!")
#
# root = Tk()
# app = App(root)
# root.mainloop()

#
#
# import tkinter  #导入tk模块开发GUI
# import tkinter.messagebox
#
# def main():
#     flag = True
#
#     #修改标签上的文字
#     def change_label_text():
#         nonlocal flag
#         flag = not flag
#         color , msg = ('red','Hello,world')\
#             if flag else ('blue','Goodbye,world')
#         label.config(text=msg, fg=color)
#
#     #确认退出
#     def confirm_to_quit():
#         if tkinter.messagebox.askokcancel('温情提示','确定要退出吗？'):  #询问选择对话窗
#             top.quit()
#
#     #创建顶层窗口
#     top = tkinter.Tk()
#     #设置窗口大小
#     top.geometry('240x160')
#     #设置窗口标题
#     top.title('小游戏')
#     #创建标签对象并添加到顶层窗口
#     label = tkinter.Label(top,text='Hello,world!',font='Arial -32',fg='red')
#     label.pack(expand=1)
#     #创建一个装按钮的容器
#     panel = tkinter.Frame(top)
#     #创建对象，指定添加到那个容器，通过command（命令）回调想要执行的功能。
#     button1 = tkinter.Button(panel,text='修改',command=change_label_text)
#     #显示窗口
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel,text='退出',command=confirm_to_quit)
#     button2.pack(side='right')
#     #显示按钮容器。
#     panel.pack(side='bottom')
#     #开启主事件循环
#     tkinter.mainloop()
#
# if __name__ == '__main__':
#     main()
# #
# #TODO 体重计数器
# import PySimpleGUI as sg
#
#
# def calc_bmi(h, w):
#     try:
#         h, w = float(h), float(w)
#         bmi = round(w / h ** 2, 1)
#         if bmi < 18.5:
#             standard = '过轻'
#         elif 18.5 <= bmi <= 23.9:
#             standard = '正常'
#         elif 24.0 <= bmi <= 27.9:
#             standard = '过重'
#         else:
#             standard = '肥胖'
#     except (ValueError, ZeroDivisionError):
#         return None
#     else:
#         return f'BMI: {bmi}, {standard}'
#
# layout = [[sg.Text('身高'), sg.InputText(size=(15,))],
#           [sg.Text('体重'), sg.InputText(size=(15,))],
#           [sg.Button('计算 BMI', key='submit')],
#           [sg.Text('', key='bmi', size=(20,2))],
#           [sg.Quit('退出', key='q')]]
#
# window = sg.Window('BMI计算', layout, font='微软雅黑')
#
# while True:
#     event, value = window.Read()
#     if event == 'submit':
#         bmi = calc_bmi(value[0], value[1])
#         if bmi:
#             window.Element('bmi').Update(bmi, text_color='black')
#         else:
#             window.Element('bmi').Update('输入有误！', text_color='red')
#     elif event == 'q':
#         break
#
# window.Close()
# # # #
# # #TODO GUI测试
# import tkinter as tk
# import tkinter.messagebox
#
# window = tk.Tk()
# window.geometry('200x150')
# window.wm_attributes('-topmost',1)
# #TODO 提醒窗口
# tk.messagebox.showinfo(title='借书', message='借书')   #调用跳转显示的窗口
#
# # window = tk.Entry(window, show='*') #输入框，输入时显示*
# # window.pack()
# # #设置图片
# # photo = tk.PhotoImage(file="111.jpg")
# # imgLabel = tk.Label(window,image=photo)
# # imgLabel.pack()
# #window.messagebox.showwarning(message='输入你想显示的内容')
# # var = tk.StringVar()    # 文字变量储存器
# # var.set('OMG! This is TK!')
# # label = tk.Label(window,
# #     textvariable=var,   # 使用 textvariable 替换 text, 因为这个是可以变化的
# #     bg='green', font=('Arial', 12), width=15, height=2)
# # label.pack()
# panel = tk.Frame(window)  #窗口布局框架。
# button1= tk.Button(panel,text='下载',command=True)
# button1.pack(side='left')  #显示出来并放置左边
# button2 = tk.Button(panel,text='关于',command=True)
# button2.pack(side='right') #显示出来并放置右边
# panel.pack(side='bottom')
# window.mainloop()


import tkinter
import tkinter.messagebox
#import book_tools
import tkinter.simpledialog

# def cun_shu():
#     tkinter.messagebox.showinfo(title='存书', message='请输入你要存的书本')
#     #book_tools.cun_book()
#     # 创建存书界面 ：
#     cun_shu = tkinter.TK()
#     # 创建顶层窗口
#     cun_shu = tkinter.Tk()
#     # 设置窗口大小
#     cun_shu.geometry('320x240')
#     # 设置窗口标题
#     cun_shu.title('存入书本界面')
#     # 1.提示label：
#     cun_shu_label = tkinter.Label(cun_shu, text="请你输入书本的相关信息 ，类别：文史【1】，艺术【2】，自然【3】，杂志【4】" \
#                                   , font='Arial -18', fg='red')
#     cun_shu_label.config(width=50, heigh=10, fg='red', bg='dark green')  # 背景。
#     cun_shu_label.pack(expand=1)
#     r = tkinter.simpledialog.askinteger('Python', '输入整数')
#     r.pack()
#
#
# cun_shu()
#
# #TODO 输入对话框
# import tkinter
# import tkinter.simpledialog
# def InStr():
# 	r = tkinter.simpledialog.askstring('Python',
# 			'字符串',
# 			initialvalue='字符串')
# 	print(r)
# def InInt():
# 	r = tkinter.simpledialog.askinteger('Python','输入整数')
# 	print(r)
# def InFlo():
# 	r = tkinter.simpledialog.askfloat('Python','I输入浮点数')
# 	print(r)
# root = tkinter.Tk()
# button1 = tkinter.Button(root,text = '输入字符串',
# 		command = InStr)
# button1.pack(side='left')
# button2 = tkinter.Button(root,text = '输入整数',
# 		command = InInt)
# button2.pack(side='left')
# button2 = tkinter.Button(root,text = '输入浮点数',
# 		command = InFlo)
# button2.pack(side='left')
# root.mainloop()


#
# #TODO 对话框
# import tkinter
# import tkinter.messagebox
# import tkinter.filedialog
# def but():
#     a=tkinter.messagebox.askokcancel('提示', '要执行此操作吗')
#     # a = tkinter.messagebox.askyesno('提示', '要执行此操作吗') #TODO 是否继续选择对话框。
#     print (a)
#
#
#     a = tkinter.filedialog.askopenfilename()
# root=tkinter.Tk()
# root.title('GUI')#标题
# root.geometry('800x600')#窗体大小
# root.resizable(False, False)#固定窗体
# tkinter.Button(root, text='hello button',command=but).pack()
# root.mainloop()

from tkinter import *

book_cun_list = []
book_cun_dict = {}


def cun_book():
    # 初始化Tk()
    myWindow = Tk()
    # 设置标题
    myWindow.title('存书系统')
    myWindow.geometry('420x420')

    # 标签+单行文本框
    #创建标签名
    Label(myWindow, text="书的名字").grid(row=0)
    Label(myWindow, text="书的编号").grid(row=1)
    Label(myWindow, text="书的价格").grid(row=2)
    Label(myWindow, text="书的类别").grid(row=3)
    #创建单行文本框
    entry1 = Entry(myWindow)
    entry2 = Entry(myWindow)
    entry3 = Entry(myWindow)
    entry4 = Entry(myWindow)
    #单行文本框排布
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    entry3.grid(row=2, column=1)
    entry4.grid(row=3, column=1)
    # 为Entry控制设置默认值
    entry1.insert(10, 'Jack')
    entry2.insert(10, '*******')
    entry3.insert(10, '￥元')
    entry4.insert(10, '文史/科学杂志')

    def show():
        """获取书籍信息"""
        # 获取Entry控件中的文本
        book_name =entry1.get()
        book_num =entry2.get()
        book_pice=entry3.get()
        book_lie=entry4.get()
        # 处理用户输入信息，创建一个专属字典处理数据
        book_cun_dict = {"book_name": book_name,
                         "book_num": book_num,
                         "book_pice": book_pice,
                         "book_lie": book_lie}
        # 存储用户输入信息，存储用户信息，将字典数据添加到列表中（重要）
        book_cun_list.append(book_cun_dict)
        # 查看刚添加的书籍信息,(用窗口提醒)提示用户输入成功
        print("书名：", end="")
        print(book_cun_dict["book_name"])  # 打印字典中是名字的值
        print("已经成功添加书籍到图书馆")
        #提醒框提示
        tkinter.messagebox.askokcancel("成功提示！","已经成功添加书籍到图书馆!")

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温情提示','确定要退出吗？'):
            myWindow.quit()

    #按键
    #TODO Grid把控件位置作为一个二维表结构来维护,即按照行列的方式排列控件:控件位置由其所在的行号和列号决定.
    # 行号相同而列号不同的几个控件会被彼此上下排列; 列号相同而行号不同的几个控件会被彼此左右排列.
    button1=tkinter.Button(myWindow,text='添加信息',width=10,command=show)\
        .grid(row=4,column=0,sticky="w", padx=10, pady=5) #TODO 按钮1的排布
    #button1.pack(side='right')
    button2=tkinter.Button(myWindow,text='退出系统',width=10,command=confirm_to_quit)\
        .grid(row=4,column=1,sticky="w", padx=10, pady=5) #TODO 按钮2的排布，将colunm 设置成2 就与按钮1并排
    #button2.pack(side='right')
# 进入消息循环
    myWindow.mainloop()


#cun_book()

def look():
    """查看页面"""
    # 按下查看键
    #创建查询显示窗口
    myWindow1 = Tk()
    # 设置标题
    myWindow1.title('查询系统')
    myWindow1.geometry('420x420')

    #书籍显示列表
    def look_book_list():
        chu_xx= Listbox(myWindow1)
        for biao_list in book_cun_list:
            chu_xx.insert(0,biao_list)
            print('表格显示在屏幕上')
        chu_xx.pack()

    #判断是否有存入书籍
    # if len(book_cun_list) ==0:
    # # 没有书籍，（抱歉，没有书籍）询问是否存入书籍
    #     #tkinter.messagebox.askokcancel("提示！", "没有书籍上架！是否存入书籍")
    #     #tkinter.quit()
    #     #print('没有书籍上架！是否存入书籍')
    #     #是 - 按键 返回 存书界面
    #     cun = input("y 或 n")
    #     if cun == 'y':
    #         return cun_book()
    #
    #     elif cun =='n':
    #         print("已经帮您取消借书操作") #提示框提示 ：tkinter.messagebox.askokcancel('提示', '要执行此操作吗')
    #         #tkinter.messagebox.askokcancel('提示', '要执行此操作吗')  #TODO  引用提醒框，
    #                                                                 # TODO 没有主框的情况下会弹出一个空白框
    #     else:
    #         tkinter.messagebox.askokcancel('输入有误', '要执行此操作吗') #提醒框提示
    #         return
    #
    # #有书籍，显示在屏幕上
    # else:
    #     for biao_list in book_cun_list:
    #         chu_xx.insert(0,biao_list)
    #     print('表格显示在屏幕上')
    #     chu_xx.pack()
    def confirm_to_quit1():
        #查询退出模块
        if tkinter.messagebox.askokcancel('温情提示','确定要退出吗？'):
            myWindow1.quit()
    #布局按键
    button1= tkinter.Button(myWindow1,text='查询',command= look_book_list)#.grid(row=1,column=2,sticky="w", padx=10, pady=5)
    button1.pack()
    button2=tkinter.Button(myWindow1,text='退出查询',command=confirm_to_quit1)
    button2.pack()
    myWindow1.mainloop()

look()
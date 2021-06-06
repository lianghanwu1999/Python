#图形环界面强化
"""
1.标题：【欢迎使用汉武图书管理系统  V 1.01】 ")
2.标题2： 选择服务项
3.按钮
        按钮1：存入   按钮2 查看
        按钮3：借书   按钮4：还书
4.要求 点击按钮可以连接到使用的服务页

"""
#TODO GUI 界面
import tkinter
import tkinter.messagebox
import tushu_tools
#import PySimpleGUI as sg

import tkinter.simpledialog

def Gui():
    """图书管理系统界面"""
    #图书管理系统的内部
    #def confirm_tushu():
    """图书馆"""
    #1.存书 -按下第一个按钮，切换到存书页面
    def cun():
        tushu_tools.cun_book()

    #查询
    def cha():
        tushu_tools.look()


    #借书
    def jie():
        tushu_tools.jie_book()

    #还书
    def hai():
        tushu_tools.hai_book()


    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温情提示','确定要退出吗？'): #TODO 询问选择对话窗
            root.quit()

    #创建顶层窗口
    root = tkinter.Tk()
    #设置窗口大小
    root.geometry('420x420') #root.geometry('420x420+100+200') （长X宽+窗口离x轴+窗口离y轴）
    #设置窗口标题
    root.title('图书管理系统')
    #创建标签对象并添加到顶层窗口
    label = tkinter.Label(root,text='图书管理系统!',font='Arial -18',fg='red')
    label.config(width=50,heigh=10,fg='red',bg='dark green')  #背景。
    label.pack(expand=1)
    # label = tkinter.Entry(top, show='*')  # 输入框，输入时显示*
    # label.pack()
    #创建一个装按钮的容器
    panel = tkinter.Frame(root)
    #创建对象，指定添加到那个容器，通过command（命令）回调想要执行的功能。
    button1 = tkinter.Button(panel,text='存入',command=lambda :cun()).grid(row=4,column=1,sticky="w", padx=10, pady=5)  #TODO 只要工具模块哪里不调用就不会自动调用
    #显示窗口
    #button1.pack(side='left')
    button2 = tkinter.Button(panel, text='查看', command=lambda :cha()).grid(row=4,column=2,sticky="w", padx=10, pady=5) #TODO command:指定按钮消息的回调函数；
    #button2.pack(side='right')
    button3 =tkinter.Button(panel,text='借书',command=lambda :jie()).grid(row=4,column=3,sticky="w", padx=10, pady=5)
    #button3.pack(side='left')
    button4=tkinter.Button(panel,text='还书',command=lambda :hai()).grid(row=4,column=4,sticky="w", padx=10, pady=5)
    #button4.pack(side='right')
    button5 = tkinter.Button(panel, text='退出', command=confirm_to_quit).grid(row=4,column=5,sticky="w", padx=10, pady=5)
    #button5.pack(side='right')
    #显示容器
    panel.pack(side='bottom')
    #开启主事件循环
    tkinter.mainloop()

if __name__ == '__main__':
    Gui()



#
# #TODO  图书管理系统
# import book_tools
#
# #TODO (hanwu) 图书馆借书系统
# #图书馆功能：欢迎页面，输入书本信息（买书输入），显示书本信息，搜索书本，还书。
#
# #图书管理系统登录界面
# #超级用户情况：
# #1.可以管理图书的输入和编辑（改书本信息），以及更多操作解锁
# #普通用户情况：查书本，借书，还书
# while True:
#     pass
#     # 1.图书系统欢迎界面
#     # """显示功能模块
#     book_tools.jm_show()
#     action_str = input("请你输入希望执行的操作 【1】存入，【2】查看，【3】借书，【4】还书：")
#     print("您选择的操作是 【%s】" % action_str)
# #操作如果输入你所要执行的操作
# # # 1.输入书本
# # # 2.查看所有
# # # 3.搜索书本（借书）
# # # 4.还书
# # # """
#     if action_str in ["1","2","3","4"]:
#         #存书
#         if action_str == "1":
#             print("-" * 50)
#             print("此为存书页面")
#             book_tools.cun_book()
#         #查看所有书本信息
#         elif action_str =="2":
#             print("-" * 50)
#             print("查看所有图书信息")
#             book_tools.look_book()
#         #借书
#         elif action_str =="3":
#             print("-" * 50)
#             print("借书")
#             book_tools.jie_book()
#         #还书
#         elif action_str =="4":
#             print("-" * 50)
#             print("还书")
#             book_tools.hai_book()
#     elif action_str =="0":
#         print("退出系统")
#         break
#
#     else:
#        print("你的操作有误，请重新输入！")
#
#
#
#
#
#
#
# #2.输入书本(存数)
#
# # 1.输入书本信息
# # 2.书本分类
# # 3.返回欢迎界面
#
#
# #输入书本信息
#
#
# # 3.查看所有
#
# # 循环遍历显示图书馆内所有图书的信息
#
#
#
# # 4.搜索书本（借书）
# # """
# # 1.询问用户查找的书名
# # 2.显示书本位置及信息
# # 3.借书操作
# #
# #
# # """
#
# #5. 还书
# # """
# # 1.提示用户还书信息
# # 2.输入还书书名，进行还书
# # 3.书本入库

from tkinter import *
import tkinter
import tkinter.messagebox
#import book_tools
import tkinter.simpledialog




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
    #设置大小
    myWindow1.geometry('420x420+100+200')
    myWindow1.resizable(False, False)  # TODO  固定窗体(禁止放大)

    label = tkinter.Label(myWindow1, text='查书系统!', font='Arial -18', fg='red')
    label.config(width=50, heigh=10, fg='red', bg='dark green')  # 背景。
    label.pack(expand=1)

    #label.grid(row=0, column=3, sticky="w", padx=10, pady=5)

    #书籍显示列表
    def look_book_list():
        chu_xx = Listbox(myWindow1)
        """显示列表框架"""

        for biao_list in book_cun_list:
            chu_xx.insert(1, "%s\n\t%s\n\t%s\n\t%s" % (biao_list["book_name"],
                                               biao_list["book_num"],
                                               biao_list["book_pice"],
                                               biao_list["book_lie"]))

            print('表格显示在屏幕上')
        chu_xx.pack()

    def confirm_to_quit1():
        #查询退出模块
        if tkinter.messagebox.askokcancel('温情提示','确定要退出吗？'):
            myWindow1.quit()
    #布局按键
    button1= tkinter.Button(myWindow1,text='查询',command=look_book_list,activeforeground='blue')#.grid(row=4,column=3,sticky="w", padx=10, pady=5)  #activeforeground='blue' 按键按下文件底色
    button1.pack(side='left')
    button2=tkinter.Button(myWindow1,text='退出',command=confirm_to_quit1,activeforeground='red')#.grid(row=4,column=5,sticky="w", padx=20, pady=10)
    button2.pack(side='right')
    myWindow1.mainloop()



# look()



def jie_book():
    """借书模块"""
    #借书窗口
    myWindow2 =Tk()
    #设置窗口标题
    myWindow2.title('借书系统')
    myWindow2.geometry('420x420')

    """借书输入框"""
    #借书书名：
    Label(myWindow2,text="书的名字").grid(row=0)
    #窗口输入框
    entry23 = Entry(myWindow2)
    entry23.place(width=150, height=50)
    #布局
    entry23.grid(row=0, column=1)  #row :横行，column ：纵行
    # 为Entry控制设置默认值
    entry23.insert(20, 'Jack')
    book_name = entry23.get()

    def jie_shu():
        """借书按钮"""
        for book_cun_dict in book_cun_list:
            if book_cun_dict['book_name'] == book_name:
                print('是否借书！')
                # 提醒框提示
                tkinter.messagebox.askokcancel("操作提醒！", "是否借书！!")
                if True :
                    tkinter.messagebox.showinfo('提示', '借书成功')
                    print('借书成功！')

            else:
                tkinter.messagebox.showinfo('提示', '借书失败')
                print('借书失败！')



    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温情提示','确定要退出吗？'):
            myWindow2.quit()

    button1=tkinter.Button(myWindow2,text='借书',command=jie_shu)\
        .grid(row=4,column=0,sticky="w", padx=10, pady=5)

    button2=tkinter.Button(myWindow2,text='退出',command=confirm_to_quit) \
        .grid(row=4, column=1, sticky="w", padx=10, pady=5)

    myWindow2.mainloop()


# jie_book()


def hai_book():
    """还书模块"""
    # 还书窗口
    myWindow3 = Tk()
    # 设置窗口标题
    myWindow3.title('还书系统')
    myWindow3.geometry('420x420')
    # 借书书名：
    Label(myWindow3, text="书的名字").grid(row=0)
    # 窗口输入框
    entry3 = Entry(myWindow3)
    entry3.place(width=300, height=100)

    # 布局
    entry3.grid(row=0, column=1)  # row :横行，column ：纵行
    # 为Entry控制设置默认值
    entry3.insert(20, 'Jack') #控制可以输入多少个值
    haibook_name = entry3.get()

    def haishu_annui():
        """还书按钮"""
        for book_cun_dict in book_cun_list:
            if book_cun_dict["book_name"] == haibook_name:
                # 确认无误后，提示还书成功
                print("还书成功！欢迎下次再来借阅哦")                  #TODO  bug 无论是否还书成功都显示 还书成功  ：可能 1.book_cun_dict["book_name"] == haibook_name:  判断不起作用，获循环不起作用。
                tkinter.messagebox.showinfo('提示', '还书成功！欢迎下次再来借阅哦')

            else:
                print("输入错误，请重新输入：")
                tkinter.messagebox.showinfo('提示', '输入错误，请重新输入')
            #return  # 因用户输入有误，应该返回操作，而不是用break,直接结束。

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温情提示', '确定要退出吗？'):
            myWindow3.quit()

    #设置图片
        #还书按钮
    button1 =tkinter.Button(myWindow3,text='还书',command=haishu_annui)\
            .grid(row=4,column=0,sticky="w", padx=20, pady=10)
    button2 =tkinter.Button(myWindow3,text='退出',command=confirm_to_quit)\
            .grid(row=4, column=1, sticky="w", padx=20, pady=10)

    myWindow3.mainloop()


#hai_book()











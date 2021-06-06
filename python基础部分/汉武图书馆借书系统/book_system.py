import book_tools

#TODO (hanwu) 图书馆借书系统
#图书馆功能：欢迎页面，输入书本信息（买书输入），显示书本信息，搜索书本，还书。

#图书管理系统登录界面
#超级用户情况：
#1.可以管理图书的输入和编辑（改书本信息），以及更多操作解锁
#普通用户情况：查书本，借书，还书
while True:
    pass
    # 1.图书系统欢迎界面
    # """显示功能模块
    book_tools.jm_show()
    action_str = input("请你输入希望执行的操作 【1】存入，【2】查看，【3】借书，【4】还书：")
    print("您选择的操作是 【%s】" % action_str)
#操作如果输入你所要执行的操作
# # 1.输入书本
# # 2.查看所有
# # 3.搜索书本（借书）
# # 4.还书
# # """
    if action_str in ["1","2","3","4"]:
        #存书
        if action_str == "1":
            print("-" * 50)
            print("此为存书页面")
            book_tools.cun_book()
        #查看所有书本信息
        elif action_str =="2":
            print("-" * 50)
            print("查看所有图书信息")
            book_tools.look_book()
        #借书
        elif action_str =="3":
            print("-" * 50)
            print("借书")
            book_tools.jie_book()
        #还书
        elif action_str =="4":
            print("-" * 50)
            print("还书")
            book_tools.hai_book()
    elif action_str =="0":
        print("退出系统")
        break

    else:
       print("你的操作有误，请重新输入！")







#2.输入书本(存数)

# 1.输入书本信息
# 2.书本分类
# 3.返回欢迎界面


#输入书本信息


# 3.查看所有

# 循环遍历显示图书馆内所有图书的信息



# 4.搜索书本（借书）
# """
# 1.询问用户查找的书名
# 2.显示书本位置及信息
# 3.借书操作
#
#
# """

#5. 还书
# """
# 1.提示用户还书信息
# 2.输入还书书名，进行还书
# 3.书本入库
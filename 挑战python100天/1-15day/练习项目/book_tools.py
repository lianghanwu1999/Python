book_cun_list =[]
book_cun_dict ={}

def jm_show():
    print("*" * 50)
    print("-" * 50)
    print("【欢迎使用汉武图书管理系统  V 1.01】 ")
    print("-" * 50)
    print("请问你要使用那种服务：")
    print("-" * 50)
    print("【1】存入",end ="\t\t")
    print("【2】查看")
    print("【3】借书",end="\t\t")
    print("【4】还书")
    print("-" * 50)
    print("*" * 50)



def cun_book():  #输入模块
    print("请你输入书本的相关信息 ，类别：文史【1】，艺术【2】，自然【3】，杂志【4】")
    #提示用户输入书本信息
    book_name = input("请输入书名： ")
    book_num = input("请输入书编号： ")
    book_pice = input("请输入书籍的价格：")
    book_lie = input("请输入书的类别：")
    #处理用户输入信息，创建一个专属字典处理数据
    book_cun_dict = { "book_name" : book_name,
                      "book_num" : book_num,
                      "book_pice" : book_pice,
                      "book_lie": book_lie}
    #存储用户输入信息，存储用户信息，将字典数据添加到列表中（重要）
    book_cun_list.append(book_cun_dict)

    #查看刚添加的书籍信息,提示用户输入成功
    print("书名：", end="")
    print(book_cun_dict["book_name"])  #打印字典中是名字的值
    print("已经成功添加书籍到图书馆")

def look_book():
    """查看图书馆所有藏书"""
    #如果没有藏书，请输入存书
    if len(book_cun_list) ==0:
        print("没有藏书，是否存入")
        return

    #给书的种类起一个表头
    for book_name_list in ["书名","书号","书价","类型"]:
        print(book_name_list ,end="\t\t")
    print("")   #数据换行

    for book_cun_dict in book_cun_list:
        #迭代遍历字典查看所有数据
        print("%s\t\t%s\t\t%s\t\t%s" %( book_cun_dict["book_name"],
                                        book_cun_dict["book_num"],
                                        book_cun_dict["book_pice"],
                                        book_cun_dict["book_lie"]))



def jie_book():
    """借书模块"""
    #显示当前书本信息
    print("-" * 50)
    print("可借书列表")
    print("*" * 50)
    look_see()

    # 输入书名进行借书
    jieshu_name = input("请输入要借的书名：")

    # 显示输入查找书的信息
    for book_cun_dict in book_cun_list:
        if book_cun_dict["book_name"] == jieshu_name:
            print("是否借阅:%s" % jieshu_name)
            queding = input("是否借阅:%s,确定【y】,取消【n】" % jieshu_name)
            if queding == "y":
                print("%s\t\t%s\t\t%s\t\t%s" % (book_cun_dict["book_name"],
                                                book_cun_dict["book_num"],
                                                book_cun_dict["book_pice"],
                                                book_cun_dict["book_lie"]))
                print("借阅成功")
            # 借完一本书后库存减少这本书的信息
            elif queding == "n":
                print("已经帮您取消借书操作")
                break
            else:
                print("输入有误，请重新输入")
                return


        # 没有相关查找的书，提示用户没有此书
        else:
            print("没有查找到你所要的书本:%s" % jieshu_name)
            #TODO(技术瓶颈，还不知道怎么继续返回嵌套的循环里重新输入)
            queding1 = input("是否重新借阅,确定【y】,取消【n】")
            if queding1 =="y":
                return
            elif queding1 =="n":
                break
            else:
                print("您的输入有误，请重新输入")
    #书本在图书馆移除
    #提示用户借书完成
def look_see():
    #封装图书馆库存模块
    for book_name_list in ["书名","书号","书价","类型"]:
        print(book_name_list ,end="\t\t")
    print("")   #数据换行

    for book_cun_dict in book_cun_list:
        #迭代遍历字典查看所有数据
        print("%s\t\t%s\t\t%s\t\t%s" %( book_cun_dict["book_name"],
                                        book_cun_dict["book_num"],
                                        book_cun_dict["book_pice"],
                                        book_cun_dict["book_lie"]))

#还书模块
def hai_book():      #TODO 有bug,没有书和没有借书也可以还书(x),如果根本没有存过书，就会直接跳出，以为没有建立过字典和列表：
    #用户输入要还书的书名
    haibook_name = input("请输入你要还书的书名：")

    #扫描书名是否是在图书馆借出的
    for book_cun_dict in book_cun_list:
        if book_cun_dict["book_name"] == haibook_name:
    #确认无误后，提示还书成功
            print("还书成功！欢迎下次再来借阅哦")

        else:
            print("输入错误，请重新输入：")
            return  #因用户输入有误，应该返回操作，而不是用break,直接结束。

    pass

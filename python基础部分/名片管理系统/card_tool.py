#定义一个空的列表变量,为所有变量记录的列表，来存储下面字典数据。
card_list = []

def show_card():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【汉武名片管理系统】  V 1.0")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新建名片"""
    print("新建名片")
    # 1.提示用户输入信息
    name = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str= input("请输入邮箱：")
    # 2.使用用户输入的信息建立一个字典
    card_dict = {"name": name,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3.将字典添加到列表中（重要）
    card_list.append(card_dict)

    # 4.提示用户添加成功
    print("添加%s 的名片成功！" % name)

def see_card():
    """显示全部"""
    print("查询全部")
    #判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何的名片记录，请使用新增功能添加名片！")
        #return 可以返回一个函数的执行结果
        #下方的代码不会被执行
        #如果return 后面没有任何的内容，表示会返回到调用函数的位置
        #并且不返回任何的结果
        return

    #打印表头
    for name in ["姓名","电话","qq","邮箱"]:
        print(name, end="\t\t")
    print("")
    #打印分割线
    print("=" * 50)
    #遍历名片列表依次输出字符串信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" %(card_dict["name"],
                                       card_dict["phone"],
                                       card_dict["qq"],
                                       card_dict["email"]))



def sousu_card():
    """搜索名片"""
    print("搜索名片")

    #1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名: ")

    #2.遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tqq\t\t邮箱") #输出表头
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # TODO 针对找到的名片记录执行修改和删除的操作：
            deal_card(card_dict)

            break

    else:
        print("抱歉，没有找到 %s " %find_name)
#定义一个处理的函数，用于后续的修改名片和储存名片
def deal_card(find_dict):
    print(find_dict)
    action_str = input("请你选择要执行的操作[1] 修改 [2] 删除 [0] 返回上一级")
# 为什么输入0 会返回上一级，因为，输入0没有对应的函数执行则会跳过。后引用到函数就会通过break跳出。
    if action_str == "1":
        #修改名片其实就是修改原有的用户字典，利用input()由用户修改字典的键。
        find_dict["name"] = input_card_info( find_dict["name"],"姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"],"电话：")
        find_dict["qq"] = input_card_info( find_dict["qq"],"QQ：")
        find_dict["email"] = input_card_info(find_dict["email"],"邮箱：")
        print("修改名片成功！")


    elif action_str == "2":
        #调用remove删除的功能
        card_list.remove(find_dict)
        print("删除名片成功！")

#新定义一个函数，如果用户没有修改信息，就可以沿用以前的值
def input_card_info(dict_value, tip_message):  #定义两个形参，来分别表示新输入的值和原来的值
    #提示用户输入内容
    result_str = input(tip_message)
    #针对用户的输入进行判断，如果用户输入了内容，就直接返回结果。
    if len(result_str) > 0:  #如果没有输入，就是输入的结果长度为0
        return  result_str    #则返回原有的结果
    #3.如果用户没有输入内容，返回“字典中原有的值”
    else:
        return dict_value






import card_tool

#编写名片管理系统的框架
while True:
    """定义while True 的循环为无尽循环，可以由用户主动决定什么什么时候退出循环。"""
    """欢迎界面,可以直接导入之前定义的模块"""
    card_tool.show_card()
    action_str = input("请你输入希望执行的操作：")
    print("您选择的操作是 【%s】" %action_str)

    #1,2,3的名片操作
    if action_str in ["1","2","3"]:

        #新增名片
        if action_str =="1":
            card_tool.new_card()
        #显示全部
        elif action_str == "2":
            card_tool.see_card()
        #查询名片
        elif action_str =="3":
           card_tool.sousu_card()
    #0 退出系统
    elif action_str == "0":
        print("欢迎你再次使用【名片管理系统】")

        break



    #其他情况
    else:
        print("您的输入有误，清重新输入")



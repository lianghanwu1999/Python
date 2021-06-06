def input_password():

    #1.提示用户输入密码
    pwd = input("请输入密码：")

    #2.判断密码的长度 >= 8 ,返回用户输入的密码
    if len(pwd)>=8:
        return pwd
    #3.如果<8 主动输入异常
    print("主动抛出异常")
    #1>创建异常对象
    ex =Exception("密码长度不够")
    #2>主动抛出异常
    raise ex

#提示用户输入密码
#在主程序进行异常排查：主动抛出异常‘
try:
    print(input_password())
except Exception as result:  #进行未知错误排查
    print(result)
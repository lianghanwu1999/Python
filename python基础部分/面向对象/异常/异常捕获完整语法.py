#异常捕获的完整语法
try:
        #提示用户输入一个整数
    num=int(input("请输入一个整数："))

        #使用8除以用户输入的整数并输出
    result = 8/num
    print(result)
except ValueError:          #输入错误最后一行的开头单词，系统运行程序既可以跳过排查此程序错误类型，从而运行正常
    print( "请正确输入整数：")
#捕获未知错误，当系统处理几个常见除外以为，还会有其他不知名错误
#为此不行其他未知名错误影响程序运行，我们可以进行捕获未知错误
except Exception as result:    #Exception 是系统固定变量，用as连接，
                               # 这里的result不是系统固定变量，是上面的储存结果变量，可以随意更换
    print("未知错误 %s" %result)  #排除其他未知变量的干扰。

#except(错误3,错误4): 多个错误的执行语句
     #print("")
else:
    #没有异常才会执行的代码
    print("执行成功：")
finally:
    #无论是否有异常，都会执行的代码
    print("无论是否有异常，都会执行的代码")
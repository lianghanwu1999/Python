#异常的传递性使用程序代码一步一步往下运行的特性
#只有控制在主程序进行异常处理，就可以避免过多使用排除异常程序的代码
#简化程序的使用
def dome1():
    return int(input("输入整数："))

def dome2():
    return  dome1()

#利用异常的传递性，在主程序捕获异常（控制了主程序就可以控制异常）
try:

    print(dome2())
except Exception as result:
    print("未知错误 %s " %result)
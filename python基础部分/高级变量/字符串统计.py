hello_str = "hello hello"

#1.统计字符串长度
print(len(hello_str))
#2.统计某一个小（子）字符串出现的次数
print(hello_str.count("llo"))
#在使用count方法，在没有的字符串时显示为0
print(hello_str.count("abc"))

#3.某一个子字符串出现的位置,用定义index方法定位确定
print(hello_str.index("llo"))
#注意：如果使用index方法传递的子字符串不存在，程序会报错！
#print(hello_str.index("abc"))


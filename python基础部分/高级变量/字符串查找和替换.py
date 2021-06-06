hello_str = "hello world"


#1.判断是否以指定字符串开始 ;正确返回true，否则返回false
print(hello_str.startswith("hello"))

#2.判断是否以指定字符串结束，正确返回true，否则返回false
print(hello_str.endswith("world"))

#3.查找指定字符串
#find查找字符串的位置
#index同样可以查找指定字符串在大写字符串中的索引
print(hello_str.find("llo"))
#index如果指定的字符串不存在，会报错
#find如果指定的字符串不存在，会返回-1
print(hello_str.find("abc"))


#4.替换字符串
#replace方法执行完成之后，会返回一个新的字符串
print(hello_str.replace("world","python"))
#注意：不会修改原有字符串的内容
print(hello_str)




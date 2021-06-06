# 指定编码的方式有两种
#第一种
# *-* coding:utf8 *-*

#第二种
#在字符串前面的u 告诉解析器这是一个utf8编码的格式字符串

hello_str = u"hello世界"

print(hello_str)

for c in hello_str:
    print(c)
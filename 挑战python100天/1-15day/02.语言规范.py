"""
使用type()检查变量类型
"""
"""
a = 100
b = 12.345
c = 1+5j
d = 'hello,world'
e = True

print(type(a))   #<class 'int'>    int()：将一个数值或字符串转换成整数，可以指定进制
print(type(b))   #<class 'float'>  float()：将一个字符串转换成浮点数。
print(type(c))   #<class 'complex'> str()：将指定的对象转换成字符串形式，可以指定编码。
print(type(d))   #<class 'str'>
print(type(e))   #<class 'bool'>
"""

"""
使用input() 函数获取键盘输入（字符串）
使用int()函数将输入的字符串转换成整数
使用print（）函数将输入带占位符的字符串

"""
"""
a = int (input(' 请输入整数 a =  '))
b = int(input('请输入整数 b =  '))
print('%d + %d = %d' %(a,b ,a+b))
print('%d - %d = %d' %(a,b ,a-b))
print('%d * %d = %d '%(a,b, a*b))
print('%d / %d = %f' %(a,b, a / b))  #%f 小数点占位符（默认取6位）,.2f：取小数点两位 
print('%d // %d  = %d' %(a,b, a//b))
print('%d %% %d =%d ' %(a,b, a % b))
print('%d ** %d = %d' %(a,b, a**b ))
"""

"""
赋值运算符
"""
"""
a = 10
b= 3
a+=b   #相当于：a=a+b  
a *=a+2 #相当于：a=a*(a+2)  
print(a)

"""
"""
比较运算符和逻辑运算符的使用
"""
"""
flag0 = 1 ==1
flag1 = 3>2
flag2 = 2<1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not(1!= 2)
print('flag0 = ',flag0)     # flag0 = True
print('flag1 =' ,flag1)     # flag1 = True
print('flag2 =',flag2)      # flag2 = False
print('flag3 =',flag3)      # flag3 = False
print('flag4 =',flag4)      # flag4 = True
print('flag5 = ',flag5)     # flag5 = False
"""
"""
将华氏温度转换为摄氏度 公式： $C=(F - 32) \div 1.8$。
"""
"""
f = float(input("请输入华氏温度："))    #转换为含小数的浮点数   %.xf 保留x位小数 
c = (f - 32) / 1.8
print('%.1f华氏温度 = %.1f 摄氏度 ' %(f,c ))
"""
"""
计算圆的周长和面积 
半径 ：r  周长 ：c   ,面积 ：q 
"""
"""
r = float(input('请输入圆的半径：'))
c = 2 * 3.1416 * r
q = 3.1416 * r**2

print("周长：%.2f"% c)
print("面积：%.2f" %q)

"""

"""
输入的年份是不是润年，是输出 True ,否输出False
"""
"""
year = int(input('输入年份：'))
#如果代码太长，写成一行不便阅读，可以使用\ 对代码进行折行
is_leap = year % 4 == 0 and year %100 != 0 or \
          year % 400 ==0
print(is_leap) 

比较运算符会产生布尔值，而逻辑运算符and和or会对这些布尔值进行组合
最终也是得到一个布尔值，闰年输出True，平年输出False
"""
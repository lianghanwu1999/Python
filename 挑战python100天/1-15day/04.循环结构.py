#TODO 循环结构 有两个 for -in  和 while

"""
用for 循环实现1-100求和

"""
sum = 0
for x in range(101):
    sum += x
print(sum)

"""
range(101) : 可以产生0到 100 范围的整数，需要注意的是取不到101
range(1,101):  可以产生1到100范围内的整数，相当于前面是闭区间后面是开区间
range(1,101,2): 可以产生1到100 的奇数，其中步长（公差）是2 ，即每次数值递增的值
range(100,0,-2): 可以用来产生100 到1 的偶数，其中步长是 - 2 ，即每次数字递减的值
"""
#TODO 用for 循环实现1-100之间的偶数求和

sum = 0
for x in range(1,100):
    if x %2 == 0:
        sum +=x
print(sum)

"""
猜数字游戏:
         引入了while 循环 ，break终止，和 while True 和while False 等知识点
"""

import random
answer = random.randint(1,100) #调用随机模块
counter = 0  #调用计数器

while True :     #while Ture：则是继续循环
    counter +=1
    number =int(input('请输入数字：'))
    if number < answer:   #输入的数字大于答案
        print('你输入的小了')
    elif number > answer:
        print('你输入的大了')
    else:
        print('恭喜你猜对了！')
        break
print("你总共猜了%d次" %counter)
if counter > 7:
    print('你的智商余额不足')


"""
输入九九乘法表
"""

for i in range(1,10):  #获取1到9 按循序排列的数
    for j in range(1,i+1):
        print('%d*%d = %d' %(i,j, i*j),end='\t')
    print()


"""
输入一个正整数判断是不是素数
"""

#TODO 模型叫”math，它包含了很多变量和函数
from math import sqrt
num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime= True
for x in range(2,end+1):
    if num %x ==0:
        is_prime =False
        break
if is_prime and num !=1:
    print('%d 是素数'%num)
else:
    print('%d不是素数' %num)
    



#TODO 输入两个正整数计算它们的最大公约数和最小公倍数

x= int(input('x = '))
y = int(input('y = '))
#如果x大于y就交换x和y的值
if x>y:
    #通过下面的操作将y的值赋值给x ，将x的值赋值给y
    x,y = y,x
#从两个数中比较的数递减的循环
for factor in range(x,0,-1):
    if x % factor == 0 and y%factor ==0:
        print('%d和%d的最大公约数是%d' %(x,y,factor))
        print('%d和%d的最小公倍数是%d ' %(x,y,x*y //factor))
        break
        

#TODO 打印三角图案
row = int(input('请输入行数：'))
for i in range(row): #记录要打印的行数
    for _ in range(i+1): #每循环一次加一
        print('*' ,end= '')
    print()  #将整个循环打印出来


for i in range(row):
    for j in range(row):
        if j < row -i-1:  #循环递减，输出空格
            print(' ' ,end='')
        else:
            print('*',end='')
    print()

for i in range(row):
    for _ in range(row -i -1):
        print(' ' ,end= '')
    for _ in range(2*i+1):
        print('*',end ='')
    print()
#TODO 字符串和数据结构

#可以在字符串中使用\（反斜杠）来表示转义，也就是说\后面的字符不再是它原来的意义，
# 例如：\n不是代表反斜杠和字符n，而是表示换行；而\t也不是代表反斜杠和字符t，
# 而是表示制表符。所以如果想在字符串中表示'要写成\'，同理想表示\要写成\\
s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

#TODO 不希望字符串中的\表示转义，我们可以通过在字符串的最前面加上字母r来加以说明
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

#TODO 运算符
s1 ='hello' * 3   #可以通过* 重复字符串
print(s1)    # hello ,hello ,hello
s2 = "world"
s1 +=s2
print(s1)   # hello hello hello world
print('11' in s1)    #True #使用in和not in来判断一个字符串是否包含另外一个字符串
print('good' in s1)  #False
str2 ='abc123456'
#从字符串中取出指定位置的字符串（下标运算）
print(str2[2])  #通过索引 取到相应字符。 #注：索引是从0开始。 // #c
#TODO 字符串切片（从指定的开始索引到指定的结束索引）
print(str2[2:5])  #c12    取2到5 的字符串
print(str2[2: ])  #c123456
print(str2[2::2])  #c246   开始值是2， 步长是2（公差是2）
print(str2[::2])   #ac246
print(str2[::-1])  #654321cba  #-1 代表反向取值
print(str2[-3:-1]) # 45  反向取值：0，-1，-2，-3.....


str1 ='hello,world'
#通过内置函数len 计算字符串的长度
print(len(str1))  #13
#获得字符串首字母大写的拷贝
print(str1.capitalize()) #Hello ,world
#获得字符串每一个单词首字母大写的拷贝
print(str1.title())     #Hello ,World  将每个单词的首字母大写
#获得字符串变大写后的拷贝
print(str1.upper())     # HELLO, WORLD ,将所有字符串变成大写
#从字符串中查找子串所在位置(查找某一个字符串所在字符串中位置)
print(str1.find('or')) #8
print(str1.find('shit')) #-1
# 与find类似，但找不到子串是会发生异常
# print(str1.index('or'))
# print(str1.index('shit'))
#检查字符串是否以指定的字符串开头
print(str1.startswith('He')) #False
print(str1.startswith('hel')) #True
#检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
#将字符串以指定的宽度居中并在两次填充指定的字符
print(str1.center(50,'*'))
#将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50 ,''))

str2='abc123456'
#检查字符串是否以数字构成
print(str2.isdigit()) #False
#检查字符串是否以字母构成
print(str2.isalpha()) #False
#检查字符串是否以数字和字母构成
print(str2.isalnum()) #True

str3 = '  jackfrued@126.com'
print(str3)
#获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

#TODO 使用列表
list1 = [1,3,5,7,100]
print(list1) #[1,3,5,7,100]
#乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2)    # ['hello', 'hello', 'hello']
#计算列表长度（元素个数）
print(len(list1)) #5
#下标（索引）运算  #列表索引从0开始，倒过来的话，-1，-2，-3进行编号
print(list1[0]) #1
print(list1[4]) #100
#通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
#通过for 循环遍历列表元素
for elem in list1:
    print(elem)
#通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index,elem in enumerate(list1):
    print(index,elem)

#TODO 在列表中添加和删除元素
list1 = [1,3,5,7,100]
#添加元素
list1.append(200)
list1.insert(1,400)
#合并两个列表
#list1.extend([1000,2000])
list1+=[1000,2000]
print(list1)    # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1)) #9
#先通过成员运算判断元素是否列表中，如果存在就删除该元素
if 3 in list1:    #如果3 在list1中，就删除 3
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]
#从指定的位置删除元素
list1.pop(0)  #利用索引删除指定位置元素
list1.pop(len(list1)-1)  #在列表去除列表末尾数
print(list1)  # [400, 5, 7, 100, 200, 1000]
#清空列表元素
list1.clear()
print(list1) #[]

#列表的切片

fruits = ['grape','apple','strawberry','waxberry']
fruits += ['pitaya','pear','mango']

#TODO 列表切片
fruits2 = fruits[1:4]
print(fruits2) #apple strawberry waxberrry
#可以通过完整切片操作；来复制列表
fruits3 = fruits[:]    #完整切片
print(fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4)  #['pitaya', 'pear']
#可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5) #['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']

#对列表排序
list1 = ['orange','apple','zoo','internationzation','blueberry']
list2 = sorted(list1)
#sorted函数返回列表排序后的拷贝不会修改传入的列表
#函数是设计就应该像sorted 函数一样应可能不产生副作用
list3 = sorted(list1,reverse=True)
#通过key 关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 =sorted(list1,key=len)
print(list1)
print(list2)
print(list3)
print(list4)
#给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)

#使用列表的生成式语法来创建列表
import sys
f = [x for x in range(1,10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
#用列表的生成表达式语法创建列表容器
#用这种语法创建列表之后元素已经准备就绪所以需要耗费较多内存空间
f=[x ** 2 for x in range(1,1000)]
print(sys.getsizeof(f)) #查看对象占用内存的字节数
print(f)
#请注意下面的代码创建的不是一个列表而是一个生成器对象
#通过生成器可以获取到数据但它不占用额外的空间存储数据
#每次需要数据的时候就通过内部的运算得到数据（需要花费额外的时间）
f = (x ** 2 for x in range(1,1000))
print(sys.getsizeof(f)) #查看对象占用内存的字节数
print(f)
for val in f:
    print(val)


#TODO 使用元组
#定义元组
t = ('汉武',38,True,'广东云浮')
print(t)
#获取元组中的元素
print(t[0])
print(t[3])
#遍历元组中的值
for member in t :
    print(member)
#重新给元组赋值
#t[0] = '王大锤' #TypenError  类型错误
#变量t重新引用新的元组原来的元组将被垃圾回收
t = ('王大锤',20,True,'云南昆明')
print(t)
#将元组转换成列表
person = list(t)
print(person)
#列表是可以修改它的元素的
#可以通过索引修改列表元素
person[0] = '李小龙'
person[1] = 25
print(person)
#将列表转换成元组
fruits_list = ['apple','banana','orange']
fruits_tuple = tuple(fruits_list)
print(fruits_list)

#TODO 使用集合
#创建集合的字面量语法
set1 = {1,2,3,3,3,2}
print(set1)
print('length = ',len(set1))
#创建集合的构造器语法（面向对象部分会进行详细讲解）
set2 = set(range(1,10))
set3 = set((1,2,3,3,2,1))
print(set2,set3)
#创建集合的推导式语法（推导式也可以用于推导集合）
set4 = {num for  num in range(1,100) if num %3 == 0 or num %5 == 0 }
print(set4)

#向集合添加元素和从集合删除元素
set1.add(4)
set1.add(5)       #添加
set2.update([11,12])   #更新字典的值或者是键，相当于插入或追加值
set2.discard(5)       #discard() 方法用于移除指定的集合元素。
if 4 in set2:
    set2.remove(4)
print(set1,set2)
print(set3.pop())
print(set3)

#集合的成员，交集，并集，差集等运算
print(set1&set2)    #交集
#print(set1.intersection(set2))
print(set1 | set2)   #并集
#print(set1.unon(set2))
print(set1 - set2)
#print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
#判断子集和超集
print(set2 <= set1)
#print(set2.issubset(set1))

print(set3<=set1)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))

#TODO 使用字典
#创建字典的字面语法
scores = {'汉武':95,'白元芳': 85 ,'狄仁杰':82}
print(scores)
#创建字典的构造器语法
items1 = dict(one = 1,tow=2,three=3,four=4)
#通过zip 函数将两个序列压成字典
items2 = dict(zip(['a','b','c'],'123'))
#创建字典的推导式语法
items3 ={num:num ** 2for num in range(1,10)}
print(items1,items2,items3)
#通过键可以获取字典中的对应的值
print(scores['汉武'])
print(scores['狄仁杰'])
#对字典中的所有键值对进行遍历
for key in scores:
    print(f'{key}:{scores[key]}')
#更新字典中的元素 #添加元素
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面 =67,方启鹤=86)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))    #输出一个none值就是证明字典里没有’武则天‘
#get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天',60))
#删除字典中的元素
print(scores.popitem())  #TODO 随机返回并删除字典中的最后一对键和值(删除并打印删除的值)。
print(scores.popitem())
print(scores.pop('汉武')) #删除字典给定键 key 及对应的值,没有给出键时，
                             # 默认用于移除列表中的一个元素（默认最后一个元素）

#清空字典
scores.clear()
print(scores)

#TODO 练习：在屏幕上显示跑马灯文字。

import os
import time

def main():
    content = '北京欢迎你为你开天辟地.....'
    while True:
        #清理屏幕上的输出
        os.system('cls')  #os.system('clear')
        print(content)
        #休眠200 毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]  #滚动字幕


if __name__ == '__main__':
    main()

#TODO 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random

def generate_code(code_len = 4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度（默认4个字符串）
    :return: 用大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' #所有字母
    last_pos = len(all_chars) -1
    code = ''
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]

    print(code)
    return code

if __name__ == '__main__':

    generate_code()

#TODO 练习3：设计一个函数返回给定文件名的后缀名。
def get_suffix(filename,has_dot = False):
    """
    获取文件名的后缀名
    :param filename:  文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) -1:
        index = pos if has_dot else pos +1
        return filename[index:]
    else:
        return ''

#TODO 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
def max(x):
    m1,m2 =(x[0],x[1] if x[0] >x[1] else (x[1],x[0]))
    for index in range(2,len(x)):
        if x [index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1,m2

#TODO 练习5：计算指定的年月日是这一年的第几天。
def is_leap_year(year):
    """
    判断指定的年份是不是润年
    :param year: 年份
    :return: 闰年返回True平年返回Fal
    """
    return year %4 == 0 and year % 100 != 0 or year % 400 ==0  #判断为闰年

def which_day(year,month ,date):
    """
    计算传入的日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], #平年月份
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #闰年月份
    ][is_leap_year(year)]
    total = 0         #计数器
    for index in range(month -1):
        total += days_of_month[index]
    return total +date    #返回第几天
def main():
    print(which_day(1980,11,28))
    print(which_day(1981,12,31))
    print(which_day(2018,1,1))
    print(which_day(2016,3,1))

if __name__ == '__main__':
    main()


#TODO 打印杨辉三角。
def main():
    num = int(input('请输入要执行的行数 : '))
    yh = [[]] * num
    for row in range(len(yh)):       #col 列数
        yh[row] = [None]*(row +1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:

                yh[row][col] = 1
            else:
                yh[row][col] = yh[row -1][col] + yh[row -1][col -1]
            print(yh[row][col],end='\t')
        print()
if __name__ == '__main__':
    main()

#TODO 案例1：双色球选号。
from random import randrange,randint,sample

def display(balls):
    """
    输出列表中的双色球号码
    :param balls:
    :return:
    """
    for index ,ball in enumerate(balls):
        if index == len(balls) -1:
            print('|',end=' ')
        print('%02d' %ball,end=' ')
    print()

def random_select():
    """
    随机选择一组号码
    :return:
    """
    red_balls = [x for x in range(1,34)]
    select_balls = []
    select_balls = sample(red_balls,6)
    select_balls.sort()
    select_balls.append(randint(1,16))
    return select_balls

def main():
    n = int(input('机选几注:'))
    for _ in range(n):
        display(random_select())

if __name__ == '__main__':
    main()



#TODO 井字棋游戏
import os

def print_board(board):
    print(board['TL']+'|' + board['TM'] + '|' +board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' +board['MM'] + '|' +board['MR'])
    print('-+-+-')
    print(board['BL'] +'|'+board['BM']+'|'+board['BR'])

def main():
    init_board = {
        'TL':' ','TM ' : ' ' ,'TR ': ' ',
        'ML' : ' ','MM ':' ','MR':' ',
        'BL' : ' ','BM ' :' ','BR' : ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0   #计数器
        os.system('clear') #调用系统功能
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s 走棋，请输入位置：' % turn)
            if curr_board[move] ==' ':
                counter += 1
                curr_board[move] = turn
                if turn =='x':
                    turn ='o'
                else:
                    turn='x'
            os.system('clear')  #清空屏幕重新开始
            print_board(curr_board)
        choice = input('再玩一局？(yes|no)')
        begin = choice == 'yes'

if __name__ == '__main__':
    main()
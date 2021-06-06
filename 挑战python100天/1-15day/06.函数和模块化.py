from random import randint
"""
def roll_dice(n = 2):
    #摇色子
    total = 0
    for _ in range(n):
        total +=randint(1,6)
    return total

def add(a=0,b=0,c=0):
    #三数相加
    return a+b+c

#如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())  #定义了实参为2
#摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
#传递参数时可以不按照设定顺序进行传递
print(add(c=50,a=100,b=200))
"""
"""
#在参数名前面的*表示args 是一个可变参数
def add (*args):      #*args 代表可变参数 ，表示可变同时，也可以用来占位
    total = 0         #total 表示为总数。
    for val in args:
        total +=val
    return total

#在调用add 函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(1,3,5,7,9))
"""
"""
# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
test.py

import module3

# 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
"""
"""
#TODO  实现判断一个数是不是素数的函数
def is_prinme(num):
    #判断
    for factor in range(2,int(num **0.5)+1):
        if num %factor == 0:
            return False
    return True if num != 1 else False
"""
"""
#TODO 变量的作用域
def foo():
    b = 'hello'  #局部变量
    #python 中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)
    bar()
    #print(c) #NameError :name 'c' is not defined

if __name__ == '__main__':
    a = 100   #全局变量
    #print(b) #NameError :name 'b' is not defined
    foo()
"""
#希望通过函数调用修改全局变量a 的值
def foo():
    a = 200   #重新定义的量，是局部变量，不是全局变量
    print(a)   #此时a=200

if __name__ == '__main__':
    a = 100
    foo()
    print(a)
#TODO 这是因为当我们在函数foo中写a = 200的时候，
# 是重新定义了一个名字为a的局部变量，它跟全局作用域的a并不是同一个变量


def foo():
    global a   #现在作用于全局变量‘
    a = 200
    print(a)  #200

if __name__ == '__main__':   #调用测试， 在其他文件中调用这个模块，不会调用这个下面的调用
    a = 100
    foo()
    print(a)



def main():
    pass

if __name__ == '__main__':
    main()

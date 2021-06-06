#TODO  初始化方法：内存中获得保存学生对象所需的内存空间，把数据放到内存空间中
class Student():
    """学生"""
    def __init__(self,name,age): #给学生对象添加name（姓名）和age（年龄）两个属性
        """初始化方法"""
        self.name =name
        self.age =age

    def study(self,course_name): #创建学生的动作（study）方法
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏')
def main():
    #创建对象
    stu1 =Student('汉武',20)
    stu2 =Student('王大锤',23)
    #对象要完成什么任务（调用方法）
    stu1.study('python程序设计')
    stu2.play()

if __name__ == '__main__':
    main()


#TODO 可见性和属性装饰器
# 对象的属性通常会被设置为私有（private）或受保护（protected）的成员，
# 简单的说就是不允许直接访问这些属性,由于对象的方法通常都是公开的（public），
# 因为公开的方法是对象能够接受的消息，暴露给外界的调用接口，这就是所谓的访问可见性，
# 用__name（双下划线）表示一个私有属性，_name（单下滑线）表示一个受保护属性

#设置私有属性
class Student:

    def __init__(self, name, age):
        self.__name = name  #设置__name为私有属性，在类的外面无法直接访问
        self.__age = age    #设置__age 为私有属性，在类的外面无法直接访问

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')


stu = Student('王大锤', 20)
stu.study('Python程序设计')
print(stu.__name)  #会报错，设置__name为私有属性，在类的外面无法直接访问

#TODO 破解私有属性
class Student:

    def __init__(self, name, age):
        self.__name = name   #设置__name为私有属性
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')


stu = Student('王大锤', 20)
stu.study('Python程序设计')
print(stu._Student__name, stu._Student__age)  #更换名字的规则，就可以访问私有属性（对象._类名+私有属性）。

#TODO 装饰器:保证私有的同时也提供读取和修改

class Student():
    def __init__(self,name,age):
        self.__name = name   #设置__name为私有属性
        self.__age =age

    #属性访问器（getter方法） -获取__name属性
    @property #装饰器
    def name(self):
        return self.__name    #-获取__name属性

    #属性修改器（setter方法） - 修改__name属性
    @name.setter   #前一个方法名.setter方法
    def name(self,name):
        self.__name = name or '无名氏'

    @property  #获取__age属性
    def age(self):
        return self.__age

stu = Student('王大锤',20)
print(stu.name,stu.age)
stu.name = ''    #可以修改，因为调用了调用setter 方法可以修改name值
print(stu.name)  #无名氏
#stu.age = 30  #会报错 ，因为它没有调用setter 方法不可以修改age值

#TODO 限定属性__slots__魔法
class Student():
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
# AttributeError: 'Student' object has no attribute 'sex'
stu.sex = '男'   #由于使用魔法方法，限定了属性，添加新的属性会报错。

class Student(object):
    #__init__是一个特殊方法用于在创建对象时进行初始化操作
    #通过这个方法我们可以为学生对象绑定name 和age 两个属性(名称属性在初始化方法，其余的动作在定义方法)
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #其余的方法为class 要完成的动作
    def study(self,course_name):
        print('%s正在学习%s.'%(self.name,course_name))

    #PEP 8要求标识符的名字用全小写多个单词用下划线连接
    #但是部分程序员和公司更倾向使用驼峰命名法（驼峰标识）
    def watch_movie(self):
        if self.age < 18:
            print('%s只能看《熊出没》'%self.name)
        else:
            print('%s正在观看美国大电影.'%self.name)

#创建对象
#TODO 当我们定义好一个类之后，可以通过下面的方式来创建对象并给对象发消息。
def main():
    #创建学生对象并指定姓名和年龄
    stu1 =Student('汉武',38)
    #给对象发study信息
    stu1.study('python程序设计')
    #给对象发watch_av信息
    stu1.watch_movie()
    stu2=Student('王大锤',15)
    stu2.study('思想品德')
    stu2.watch_movie()

if __name__ == '__main__':
    main()

#TODO 在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，
# 如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
# 不想属性直接暴露在外界的私隐问题，就可以将他们设置为私有属性和私有方法。用单划线

class Test:
    def __init__(self,foo):
        self._foo = foo     #定义私有属性，在前面加__

    def __bar(self):
        print(self._foo)
        print('__bar')

def main():
    test =Test('hello')
    #用于bar是私有化方法，这在其他方法中调用不了
    test._bar()
    #__foo，是私有化属性，在其他方法中也调用不了
    print(test._foo)

if __name__ == '__main__':
    main()



#TODO  封装：隐藏一切可以隐藏的实现细节，只向外界暴露简单的调用接口。
#TODO 模拟数字时钟
from time import sleep

class Clock (object):
    """
    数字时钟
    """
    def __init__(self,hour=0,minute=0,second=0):
        """

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self.__hour = hour    #定义时分秒，为私有方法。只在Clock 类中才能被执行。
        self.__minute = minute
        self.__second = second

    def run(self):
        """走字"""
        self.__second +=1
        if self.__second == 60:
            self.__second = 0
            self.__minute +=1
            if self.__minute ==  60:
                self.__minute = 0
                self.__hour +=1
                if self.__hour == 24:
                    self.__hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' %\
               (self.__hour,self.__minute,self.__second)

def main():
    clock = Clock(23,59,59)  #全局变量
    while True:
        print(clock.show())
        sleep(1) #休眠间隙：间隙显示频率1
        clock.run()

if __name__ == '__main__':
    main()

#TODO 定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法

from math import sqrt
#调用数学计算的模块

class Point(object):

    def __init__(self,x=0 , y=0):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y =y

    def move_to(self,x,y):
        """
        移动到指定的位置
        :param x: 新的横坐标
        :param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self,dx,dy):
        """
        移动指定的增加量
        :param dx: 横坐标的增加量
        :param dy: 纵坐标的增加量
        """
        self.x +=dx
        self.y +=dy

    def distance_to(self,other):
        """
        计算与另一点的距离
        :param other: 另一点
        :return:
        """
        dx = self.x - other.x
        dy = self.y -other.y
        return sqrt(dx **2 + dy **2)
    def __str__(self):
        return '(%s,%s)' %(str(self.x),str(self.y))

def main():

    p1 = Point(3,5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1,2)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()


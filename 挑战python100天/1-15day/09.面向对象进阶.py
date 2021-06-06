class Person(object):

    def __init__(self,name,age):
        self.__name =name
        self.__age = age

    #访问器 -getter方法
    #TODO  property属性：定义时：实例方法时仅要一个self参数，调用时无需括号（不需要考虑传参问题）
    # （就像复杂的方法封装成一个属性方法，调用时相当于调用一个属性一样简单，无需复杂的调用。
    @property
    def name(self):
        return self.__name

    #访问器 -getter方法
    @property               #TODO @property 装饰器负责把一个方法变成属性方便调用
    def age(self):
        return self.__age   #TODO 用@property 修饰age方法，获取方法返回值

    #修改器 -setter方法      #TODO 用@property 修饰age方法，利用setter 具有赋值功能
    @age.setter
    def age(self,age):
        self.__age = age

    def play(self):
        if self.age <= 16:
            print('%s正在玩飞行棋.' %self.__name)
        else:
            print('%s 正在玩斗地主.' %self.__name)

def main():
    person = Person('王大锤',12)
    person .play()
    person.age = 22      #TODO  修改赋值
    person.play()

if __name__ == '__main__':
    main()

#TODO __slots__魔法
# 可以通过在类中定义__slots__变量来进行限定，对子类不起作用。

class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性,  为私有化方法
    __slots__ = ('__name','__age','__gender')

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property   #TODO @property 装饰器负责把一个方法变成属性方便调用
    def name(self):
        return self.__name

    @property           #TODO @property 装饰器负责把一个方法变成属性方便调用
    def age(self):      #TODO 用@property 修饰age方法，获取方法返回值
        return self.__age

    @age.setter         #TODO 用@property 修饰age方法，利用setter 具有赋值功能
    def age(self,age):
        self.__age = age

    def play(self):
        if self.__age <= 16:
            print('%s正在玩飞行棋.'%self.__name)
        else:
            print('%s正在玩斗地主。'%self.__name)

def main():
    person =Person('王大锤',22)
    person.play()
    person.__gender = '男'


from math import sqrt
class Triangle(object):

    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c

    @staticmethod    #TODO 静态方法 ：不访问实例属性self/类属性(cls)情况下，用静态方法
    def is_valid(a,b,c):  #TODO 即是不需要使用实例和调用类的一些方法，只是某个单纯作用时，使用类方法。
        return a+b+c  and b+c>a and a+c >b

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """判断三条边长能否构成三角形(类方法)"""
    #     return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self.__a + self.__b +self.__c

    def area(self):
        half = self.perimeter()/2
        return sqrt(half*(half - self.__a)*
                    (half-self.__b)*(half -self.__c))

def main():
    a,b,c = 3,4,5
    #静态方法和类方法都是通过给类发信息来调用的
    if Triangle.is_valid(a,b,c):
        t = Triangle(a,b,c )
        print(t.perimeter())
        #也可以通过给类发消息来调用对象方法，但是要传入接收消息作为对象参数
        #print(Triangle.perimeter(t))
        print(t.area())
        #print(Triangle.area())

    else:
        print('无法构成三角形。')

if __name__ == '__main__':
    main()


from time import time,localtime,sleep

class Clock(object):
    """数字时钟"""

    def __init__(self,hour =0,minute=0,second=0):
        self.__hour = hour   #私有属性
        self.__minute =minute
        self.__second = second

    @classmethod  #定义类方法 ：使用类属性来记录某样东西的数量
    def now(cls):     #类方法表识cls
        ctime = localtime(time())   #获取本地时间

        #  #使用赋值语句定义类属性，记录所有工具对象的数量
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)

    def run(self):
        """走字"""
        self.__second +=1
        if self.__second ==60:  #如果秒针满60
            self.__second = 0   #将秒针调回0
            self.__minute +=1   #分针加1
            if self.__minute == 60:
                self.__minute =0
                self.__hour +=1
                if self.__hour == 24:
                    self.__hour =0
    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self.__hour, self.__minute, self.__second)

def main():
    #通过类方法创建对象，并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main()

#TODO 继承
#TODO 父类与自身都同时具有的属性时，为了避免重复书写代码，
# 通过重写父类，继承父类与自身都具有的属性，声明自己特有的属性
# 最后声明自己特有的方法就可以了

class Person(object):
    """人"""
    def __init__(self,name,age):
        self._name = name  #定义私有属性，只在类中使用
        self._age = age

    # 将方法转换成属性使用
    @property
    def name(self):
        return self._name
    @property              #TODO （获取 修饰age方法，（获取）方法返回值
    def age(self):
        return self._age
    @age.setter         #TODO （设置）修饰age方法，利用setter 具有（设置）赋值功能（修改值功能）
    def age(self,age):
        self._age =age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)
    def watch_av(self):
        if self._age >= 18:
            print('%s观看动作片。' % self._name)

        else:
            print('%s只能观看《熊出没》。' % self._name)

class Student(Person):
    """学生"""
    def __init__(self,name,age,grade):
        super().__init__(name,age)  #重写父类，继承父类的方法和属性
        self._grade = grade         #声明自己特有的属性

    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self,grade):
        self._grade = grade

    def study(self,course):
        print('%s的%s正在学习 %s .' % (self._grade, self._name, course))

class Teacher(Person):
    """老师"""
    def __init__(self,name,age,title):
        super().__init__(name,age)  #继承了父类Person的name 和 age 方法，减少代码使用
        self._title = title          #声明自己特有的属性

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        self._title = title

    def teach(self,course):
        print('%s%s 正在讲%s.' % (self._name, self._title, course))

def main():
    stu = Student('王大锤',15,'初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('汉武',21,'专家')
    t.teach('Python程序设计')
    t.watch_av()

if __name__ == '__main__':
    main()

#TODO （单划线与双划线说明：）单前置下划线,私有化属性或方法，类对象和子类可以访问,(最保险的方法)
# 双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)，类对象和子类不能访问
# 子类不能访问父类中两个下划线__修饰的方法和属性，也不能修改父类中双下划线的属性

#小结：想要保险，在设置私有化方法是统一单划线。双划线子类和对象访问不了
from abc import ABCMeta ,abstractmethod

class Pet(object,metaclass=ABCMeta):
    """宠物"""
    def __init__(self,nickname):
        self._nickname =nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass

class Dog(Pet):
    """狗"""
    def make_voice(self):
        print('%s:汪汪....'%self._nickname)
class Cat(Pet):
    """猫"""
    def make_voice(self):
        print('%s喵。。喵。。'%self._nickname)

def main():
    pets = [Dog('旺财'),Cat('凯蒂'),Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()

#TODO 奥特曼打小怪兽

from abc import ABCMeta ,abstractmethod
from random import randint,randrange

class Fighter (object,metaclass=ABCMeta):
    """战斗者"""
    #通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name','_hp')

    def __init__(self,name,hp):
        """
        初始化方法
        :param name:名字
        :param hp: 生命值
        """
        self._name = name
        self._hp = hp

    @property   #设置这种装饰器，目的限制参数的暴露性，不能随意更改
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter  #在property 装饰器创建 setter 这个，开放一部分功能，将变得可读可写。
    def hp(self,hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp >0

    @abstractmethod
    def attack(self,other):
        """
        攻击
        :param other:  被攻击对象
        :return:
        """
        pass

class Ultraman(Fighter):
    """奥特曼"""
    __slots__ = ('name','_hp','_mp')
    def __init__(self,name,hp,mp):
        """
        初始化方法
        :param name:姓名
        :param hp: 生命值
        :param mp: 魔法值
        """
        super().__init__(name,hp)
        self._mp = mp

    def attack(self,other):
        other.hp -= randint(15,25)  #产生随机数从15-25区间

    def huge_attack(self,other):
        """
        究极必杀技(打掉对方至少50点或四分之三的血)
        :param other: 被攻击对象
        :return: 使用成功返回True 否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50   #放技能消耗能力值
            injury = other.hp *3// 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack()
            return False

    def magic_attack(self,others):
        """
        魔法攻击
        :param self:
        :param others: 被攻击的群体
        :return: 使用魔法成功返回True 否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10,15)
            return True
        else:
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1,10)
        self._mp += incr_point
        return incr_point
    #只返回一条字符串
    def __str__(self):
        return '~~~%s奥特曼~~~\n'%self._name+\
            '生命值：%d\n' %self._hp +\
            '魔法值：%d\n' %self._mp


class Monster(Fighter):
    """小怪兽"""
    __slots__ = ('_name','_hp')
    def attack(self,other):
        other.hp -=randint(10,20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    """判断有没有小怪兽是活着的"""
    for monster in monsters:
        if monster.alive >0:
            return True
    return False

def select_alive_one(monsters):
    """选中一只活着的小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive >0:
            return monster

def display_info(ultraman,monsters):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster,end='')

def main():
    u = Ultraman('汉武',1000,120)
    m1 = Monster('狄仁杰',250)
    m2 = Monster('白元芳',500)
    m3 = Monster('王大锤',750)
    ms =[m1,m2,m3]

    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)  #选中一只小怪兽
        skill= randint(1,10) # 通过随机数选择使用哪种技能
        if skill <= 6:       #60%的概率使用普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))

        elif skill <=9 : # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)

        else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))

        if m.alive>0:# 如果选中的小怪兽没有死就回击奥特曼
            print('%s 回击了%s.'%(m.name,u.name))
            m.attack(u)

        display_info(u,ms) #每个回合结束后显示奥特曼和小怪兽的信息
        fight_round +=1

    print('\n========战斗结束!========\n')
    if u.alive >0:
        print('%s 奥特曼胜利了'%u.name)
    else:
        print('小怪兽胜利了')
if __name__ == '__main__':
    main()


#TODO 工资结算系统
"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

from abc import ABCMeta,abstractmethod
#ABCMeta 创建抽象类，平时相当于实现共同的接口，避免不同的类出现不兼容

class Employee(object,metaclass=ABCMeta): #实现不同class，有共同接口，避免不兼容报错。
    """员工"""
    def __init__(self,name):
        """
        初始化方法
        :param name: 姓名
        """
        self._name = name

    @property      #TODO @property包装器来包装getter(访问器)和setter（修改器）方法，
                     # TODO 使得对属性的访问既安全又方便
    def name(self):
        return self._name
    @abstractmethod
    def get_salary(self):
        """
        获得月薪
        :return: 月薪
        """
        pass

class Manager(Employee):
    """部门经理"""
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    """程序员"""
    def __init__(self,name,working_hour = 0):
        super().__init__(name)
        self._working_hour = working_hour #设置为私有方法

    @property    #只读
    def working_hour(self):
        return self._working_hour

    @working_hour.setter  #可以访问
    def working_hour(self,working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0*self.working_hour

class Salesman(Employee):
    """销售员"""
    def __init__(self,name,sales = 0):
        super().__init__(name)  #重新父类，继承父类的name属性
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter         #TODO 修改器，使得访问安全属性（保护属性和方法）
    def sales(self,sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales*0.05

def main():
    emps = [
        Manager('刘备'),Programmer('诸葛亮'),
        Manager('曹操'),Salesman('荀彧'),
        Salesman('吕布'),Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps :
        if isinstance(emp,Programmer):
            emp.working_hour = int(input('请输入%s本月工作时间：'%emp.name))
        elif isinstance(emp,Salesman):
            emp.sales = float(input('请输入%s本月销售额：'%emp.name))
        #同样接收get_salary这个消息但是不同的员工表现出不同的行为（多态）
        print('%s本月工作为：￥%s 元'%(emp.name,emp.get_salary()))

if __name__ == '__main__':
    main()


#TODO Property  新式类使用的模板
from abc import ABCMeta,abstractmethod

class Goods(object):

    def __init__(self):
        #原价
        self.original_price = 100
        #折扣
        self.discount = 0.8

    @property         #获取返回值
    def price(self):
        #实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter     #修改
    def price(self,value):
        self.original_price = value

    @price.deleter     #删除
    def price(self):
        del self.original_price


obj = Goods()    #创建对象
obj.price       #获取商品价格（获取返回值）
obj.price = 200  #修改商品原价
del obj.price  #删除商品原价


#TODO 扑克牌游戏
import random
class Card(object):
    """一张牌"""
    def __init__(self,suite,face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):     #TODO  __str__ 方法需要返回一个字符串，当做这个对象的描写,打印return数据
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str ='J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' %(self._suite,face_str)

    def __repr__(self):
        return self.__str__()

class Poker(object):
    """一副牌"""
    def __init__(self):
        self._cards = [Card(suite,face)
                       for suite in '$#&*'
                       for face in range(1,14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards   #获取cards值

    def shuffle(self):
        """洗牌（随机乱序）"""
        self._current = 0  #计数器
        random.shuffle(self._cards)

    @property
    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)

class Player(object):
    """玩家"""
    def __init__(self,name):
        self._name = name
        self._cards_on_hand =[]

    #使用property 方法可以获取返回的return，方便调用其方法
    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self.cards_on_hand

    def get(self,card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self,card_key):
        """玩家整理手上的牌"""
        self._cards_on_hand.sort(key=card_key)

#排序规则-先根据花色再根据点数排序
def get_key(card):
    return (card.suite,card.face)

def main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'),Player('西毒'),Player('南帝'),Player('北丐')]
    for _ in  range(13) : #TODO 获取到列表 ： [0,1,2,......12] 的数字
        for player in players:
            player.get(p.has_next)
    for player in players:
        print(player.name + ':' ,end=' ')
        #players.arrange(get_key)
        print(player._cards_on_hand)

if __name__ == '__main__':
    main()

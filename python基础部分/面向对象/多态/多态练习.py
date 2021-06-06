class Dog(object):  #定义其为以object 为基类的新式类

    def __init__(self,name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)

class xiaotianDog(Dog):  #xiaotianDog 继承了父类Dog 的所有方法，
    def game(self):       #自己新增创建的方法
        print("%s 飞到天上去玩耍..." %self.name)

class Person(object):
    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog):      #多态，就是在两个不同的方法类中，互相可以被引（调）用。
        print("%s 和 %s 快乐的玩耍..." %(self.name,dog.name))

        #让狗玩耍
        dog.game()


#1.创建狗对象
wangcai = Dog("旺财")
xiaotianDog = Dog("飞天旺财")
#2.创建一个小明对象
xiaoming = Person("小明")
#3.让小明和狗玩耍
xiaoming.game_with_dog(wangcai)


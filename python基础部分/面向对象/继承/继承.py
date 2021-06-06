class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

class Dog(Animal):   #Dog 作为子类继承父类Animal的所有方法。
    def bark(self):   #增添新方法bark()
        print("汪汪叫")

class xiaotianquan(Dog):
    pass

#创建一个对象：狗
wangcai = Dog()

wangcai.run()
wangcai.eat()
wangcai.drink()
wangcai.bark()
wangcai.sleep()
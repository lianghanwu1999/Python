#小明爱跑步
class Person:

    def __init__(self,name,welght):  #创建初始方法，初始方法的作用是创建的属性，可以为后续方法可以调用。
        #self.属性 = 形参
        self.name = name
        self.weight = welght

    def __str__(self):  #调用__str__方法，输出增加的描述 （内置方法）
        return "我的名字叫 %s 体重是 %.2f 公斤" %(self.name,self.weight)

    def run(self):  #方法1
        print("%s 爱跑步，跑步锻炼身体" %self.name)
        self.weight -= 0.5     #对象的方法内部是可以直接访问对象的属性的
    def eat(self):   #方法2，
        print("%s 是吃货，吃完这顿再减肥" %self.name)
        self.weight +=1

xiaoming = Person("小明",75.0)  #给self 和 属性 以实参的方式输入给形参

xiaoming.run()   #调用跑步的方法
xiaoming.eat()   #调用吃的方法

print(xiaoming)

#多对象扩展：新增一个对象，只会对类中定义的方法进行调用，而不会影响其他的对象数据。
xiaomei = Person("小美",45)  #即是同一个类创建的多个对象之间，属性互不干扰

xiaomei.eat()
xiaomei.run()

print(xiaomei)

class Cat:

    def __init__(self,new_name):  #创建方法1，在self 后增加一个属性初始值，相当于形参。

        print("这是一个初始化方法")
        #self.属性名 = 属性的初始值（形参）
        self.name = new_name

    def __del__(self): #创建方法2    
        print("%s 我去了" %self.name)

    def __str__(self):  #现在print输出中输出特定的内容，就可以调用这个方法
        #必须返回一个字符串
        return "我是小猫[%s]" %self.name

#使用类名（）创建对象的时候，会自动调用初始化方法__init__
tom = Cat("Tom")  #用实参与形参的思维，赋值给属性初始值

print(tom.name)     #因为对象应用了谁，self就调用代替谁。
print(tom)

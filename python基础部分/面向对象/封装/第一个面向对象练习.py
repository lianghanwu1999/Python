
#定义类
class Cat:
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫爱喝水")

#创建猫对象
tom = Cat()

#调用对象方法：
tom.eat()
tom.drink()

#可以查看对象的内存地址可以用print（对象名）查看，
# 同时也可以用这个方法判断是否是相同的两个对象
#显示的内存中的位置用16进制来显示。
print(tom)

#调用多个对象方法，同一个类可以创建不同的对象，对象之间各不相同（可以用内存中的位置判断）
lazy_cat = Cat()
#可以使用. 属性名，利用赋值语句就可以给对象增加赋值（只有在python中可以）
lazy_cat.name = "蓝猫"

#调用对象方法
lazy_cat.eat()
lazy_cat.drink()

#判断在内存中的地位
print(lazy_cat)







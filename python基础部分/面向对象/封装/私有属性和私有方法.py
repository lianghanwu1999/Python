class Women:

    def __init__(self,name):

        self.name = name
        #定义一个私有属性，只有允许在内部调用
        self.__age =18

    def secret(self): #在对象的方法内部，是可以访问对象的私有属性的。
        print("%s 的年龄是 %d " %(self.name,self.__age))  #私有属性可以在内部被调用。


#创建一个对象叫小芳
xiaofang = Women("小芳")
#外部不可以直接调用私有变量小芳的年龄，所有出错。
#print(xiaofang.__age)
#调用小芳秘密方法
xiaofang.secret()

#想破解私有属性私有方法：_类名_名称  格式就可以将原有被禁止访问的私有方法，在外部访问
#在原有基础上中间插入：_类名
print(xiaofang._Women__age)


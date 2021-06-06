class Tool(object):
    #使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0  #(类属性)
    #定义一个类方法  类方法有其独特的（cls) 表识
    @classmethod
    def show_tool_cout(cls):
        print("工具对象的数量 %d" %cls.count)

    def __init__(self,name):
        self.name = name

        #让类属性的值+1
        Tool.count +=1

#1.创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

#调用类方法  类名.类方法名，调用类方法。
Tool.show_tool_cout()

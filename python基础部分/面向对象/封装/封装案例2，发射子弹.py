class Gun:

    def __init__(self,model):
        #1.枪的型号
        self.model = model
        #2.子弹的数量
        self.bullet_count = 0



    def add_bullet(self,count):
        #统计子弹数量，传递参数装填子弹
        self.bullet_count += count

    def shoot(self):
        #发射动作
        #1.判断子弹数量
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了...." % self.model)
            return
        #发射子弹，数量-1.
        self.bullet_count -= 1

        #3.提示发射信息
        print("[%s] 突突突.... [%d]" %(self.model,self.bullet_count))


class Soldier:

    def __init__(self,name):

        #1.姓名
        self.name = name

        #枪 --新生士兵没有枪
        self.gun = None     #定义没有初始值是可以用None

    def fire(self):
        #1.判断士兵是否有枪
        if self.gun ==None:
            print("[%s] 还没有枪...." % self.name)

            return

        #高喊开战口号
        print("冲啊...[%s]" %self.name)

        #3.让枪装填子弹  #调用上一个类中的方法
        self.gun.add_bullet(50)

        #4.让枪发射子弹  #调用上一个类中的方法
        self.gun.shoot()

# TODO（作用：这段代码演示就是证明，一个类中可以调用另一个类中的方法）

#创建枪对象
ak47 = Gun("AK47")

#创建许三多
xusanduo = Soldier("许三多")

xusanduo.gun = ak47
xusanduo.fire()

print(xusanduo.gun)
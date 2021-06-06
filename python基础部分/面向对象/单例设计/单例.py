#单例模式验证：
#单例模式是调用无数次属性创建的对象，内存地址都是一样的
#这证明这是单例模式

class MusicPlayer(object):

    #记录第一个被创建对象的引用 ，定义一个类属性，初始值设置为None
    instance = None
    def __new__(cls, *args, **kwargs):
        #1.判断类属性是否是空对象
        if cls.instance is None:
            #2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        #3.返回类属性保存的对象引用 ：返回调用的值，就形成一个循环。
        # 就会导致一直都是这个结果。形成单例。
        return cls.instance

#创建两个对象，通过创建的对象的内存地址，来判断是否为单例方法。
Player1 = MusicPlayer()
print(Player1)
Player2 = MusicPlayer()
print(Player2)

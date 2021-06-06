class MusicPlayer(object):

    #记录第一个被创建对象的引用 ，定义一个类属性，初始值设置为None
    instance = None
    #记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        #1.判断类属性是否是空对象
        if cls.instance is None:
            #2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        #3.返回类属性保存的对象引用 ：返回调用的值，就形成一个循环。
        # 就会导致一直都是这个结果。形成单例。
        return cls.instance

    def __init__(self):
        #1.判断是否执行过初始化动作（如果判断为False是继续执行）
        if MusicPlayer.init_flag:
            return
        #2.如果没有执行过，在执行初始化动作（）
        print("初始化播放器...")

        #修改类属性的标记（在下一次执行时变回True 退出循环。）
        MusicPlayer.init_flag = True


#创建两个对象，通过创建的对象的内存地址，来判断是否为单例方法。
Player1 = MusicPlayer()
print(Player1)
Player2 = MusicPlayer()
print(Player2)
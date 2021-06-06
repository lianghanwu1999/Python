class MusicPlayer(object):

    #__new__方法是为对象分配内存空间的功能，然后一定要返回super().__new__(cls)的结果
    # 否则不会调用对象的初始值方法
    #返回了结果之后，才会被引用传递到初始方法里面。

    def __new__(cls, *args, **kwargs):
        #1.创建对象时，new方法会被自动调用
        print("创建对象，分配空间")

        #2.为对象分配空间（用super().__new__(cls)返回new方法在父类的值）
        instance = super().__new__(cls )
        #3.返回对象的引用（用return 返回super().__new__(cls)的结果,若不返回，则不会执行下面的代码）
        return instance

    def __init__(self):
        print("播放器初始化")

#创建播放器对象
player = MusicPlayer()


print(player)
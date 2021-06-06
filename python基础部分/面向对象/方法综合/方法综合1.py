class Game(object):
    pass
    #历史最高分 (定义个类属性记录历史最高分)
    top_score = 0
    #定义一个实例方法，定义一个实例对象
    def __init__(self,player_name):
        self.player_name = player_name

    #定义一个静态方法（定义这个方法既不访问需要访问类属性，也不需要调用实例属性，所以定义为静态方法）
    @staticmethod
    def show_help():
     print("帮助信息：让僵尸打开大门")

    #定义一个类方法记录游戏的历史记录(历史记录只访问类的属性，所以定义为类方法)
    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" %cls.top_score)

    #定义一个实例方法来记录游戏方法
    def start_game(self):
        print("%s 开始游戏啦...." %self.player_name)

#1.查看游戏的帮助信息
Game.show_help()
#2.查看历史最高分（类方法和静态方法都是通过 类名.方法名  进行调用）
Game.show_top_score()

#创建游戏对象小明
game =Game("小明")

game.start_game()




from snake import *
from map import *
from hud import *
from menu import *
from chat import *
from scene import *


class Game:
    """
    游戏主题，一共有六个阶段：主菜单，关卡选择，对话场景，关卡显示场景，关卡进行，关卡结果场景
    可以根据current_level来改变当前关卡，用于继续上次游戏
    """
    def __init__(self, current_level=0):
        self.snake_move_cycle = Cycle(2, 1)
        self.current_level = current_level
        self.current_playing = 0

        self.map = None

        self.snake = None

        self.scene = None

        self.info_hud = None

        self.menu = MainMenu()

        self.shaking = [False, False]
        self.shake_cycle = [ReCycle(15, 1), ReCycle(15, 1)]
        self.shake_countdown = [0, 0]

    # 摇晃当前屏幕，特效
    def shake(self, direction, dur_t):
        if direction == "v":
            self.shaking[1] = True
            self.shake_countdown[1] = dur_t
        else:
            self.shaking[0] = True
            self.shake_countdown[0] = dur_t

    # 获取当前渲染offset，为了让屏幕随着蛇移动
    def get_offset(self):
        if self.shaking[0] and self.shaking[1]:
            return self.shake_cycle[0].get()-int(self.snake.position[0] - screen_width/2), \
                   self.shake_cycle[1].get()-int(self.snake.position[1] - screen_height/2)
        elif self.shaking[0]:
            return self.shake_cycle[0].get()-int(self.snake.position[0] - screen_width/2), \
                   -int(self.snake.position[1] - screen_height/2)
        elif self.shaking[1]:
            return -int(self.snake.position[0] - screen_width/2), \
                   self.shake_cycle[1].get()-int(self.snake.position[1] - screen_height/2)
        return -int(self.snake.position[0] - screen_width/2), \
               -int(self.snake.position[1] - screen_height/2)

    # 开始一个场景
    def start_scene(self, scene):
        self.scene = scene

    # 开始一个游戏
    def start(self, level=7):
        self.menu = None
        self.snake = Snake(self)
        for _ in range(5):
            self.snake.grow()
        self.info_hud = InfoBar(self.snake)
        if level == 1:
            self.map = Level1(self)
        elif level == 2:
            self.map = Level2(self)
        elif level == 3:
            self.map = Level3(self)
        elif level == 4:
            self.map = Level4(self)
        elif level == 5:
            self.map = Level5(self)
        elif level == 6:
            self.map = Level6(self)
        elif level == 7:
            self.map = Level7(self)
        elif level == 8:
            self.map = Level8(self)
        self.map.set_snake(self.snake)
        self.update()
        self.start_scene(TalkScene("snake_1", "snake_2", level_chats[level-1]))
        bgs[3].play_non_stop()

    # 绘制当前状态，菜单优先，其次场景，最后是游戏本身
    def draw(self):
        if not self.scene and self.menu:
            self.menu.draw()
        elif not self.scene:
            self.map.draw_background(self.get_offset())
            self.snake.draw()
            self.map.draw(self.get_offset())

            self.info_hud.draw()
        else:
            if self.scene.name == "text" or self.scene.name == "level":
                self.map.draw(self.get_offset())
            self.scene.draw()

    # 触发成员的键盘鼠标事件，并且根据返回的值来更新自己的状态
    def handle_event(self, event):
        if self.menu:
            result = self.menu.handle_event(event)
            if result != -1:
                if result >= 0:
                    self.current_playing = result
                    self.start(result+1)
                else:
                    if result == -3:
                        self.menu = LevelSelect(self.current_level)
                    elif result == -2:
                        self.current_level = 0
                        self.menu = LevelSelect(self.current_level)
        elif not self.scene:
            pass
        else:
            self.scene.handle_event(event)

    # 更新当前状态，菜单优先，其次场景，最后是游戏本身。同时处理屏幕摇晃，根据结束场景开始游戏或者开始另外一个场景。
    def update(self):
        if not self.scene and self.menu:
            self.menu.update()
        elif not self.scene:
            self.snake.set_direction(env["mouse_direction"])
            self.map.update()

            if self.snake_move_cycle.get() == 0:
                self.snake.crawl()
            self.snake.update()

            self.info_hud.update()
            if self.map.is_dead():
                self.menu = LevelSelect(self.current_level)
                self.scene = TextScene("lose_text")
            elif self.map.is_passed() and self.current_level == self.current_playing:
                self.current_level += 1
                self.menu = LevelSelect(self.current_level)
                self.scene = TextScene("win_text")
            elif self.map.is_passed():
                self.menu = LevelSelect(self.current_level)
                self.scene = TextScene("win_text")
        else:
            self.scene.update()
            if self.scene.is_ended():
                if self.scene.name == "chat":
                    m = random.randint(0, 1)
                    if m == 0:
                        bgs[1].play_non_stop()
                    else:
                        bgs[2].play_non_stop()
                    self.scene = LevelNum(self.current_playing+1)
                else:
                    self.scene = None

        if self.shaking[0]:
            self.shake_countdown[0] -= 1
            if self.shake_countdown[0] <= 0:
                self.shaking[0] = False
        if self.shaking[1]:
            self.shake_countdown[1] -= 1
            if self.shake_countdown[1] <= 0:
                self.shaking[1] = False

from config import *
from cycle import *


class RectPoint:
    """
    方周运动点，在pos位置以speed速度在side大小的长方形边上循环
    用于主菜单的按钮悬浮动画
    """
    def __init__(self, pos, speed, side):
        self.start = (pos[0], pos[1])
        self.pos = pos
        self.vel = (speed, 0)
        self.speed = speed
        self.side = side

    # 移动这个点，在长方形周边移动
    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if self.pos[0] < self.start[0]:
            self.pos[0] = self.start[0]
            self.vel = (0, -self.speed)
        elif self.pos[0] > self.start[0] + self.side[0]:
            self.pos[0] = self.start[0] + self.side[0]
            self.vel = (0, self.speed)
        elif self.pos[1] < self.start[1]:
            self.pos[1] = self.start[1]
            self.vel = (self.speed, 0)
        elif self.pos[1] > self.start[1] + self.side[1]:
            self.pos[1] = self.start[1] + self.side[1]
            self.vel = (-self.speed, 0)

    # 获取点的位置
    def get(self):
        return self.pos


class MainMenu:
    """
    主菜单，有两个按钮一个标题，均有动画
    """
    def __init__(self):
        self.points = [-150, 0, 150, 300, 450]
        self.float_cycle = ReCycle(8, 3)
        self.float_cycle2 = ReCycle(8, 3, 3)
        self.point_set1 = [RectPoint([207, 198], 10, (190, 40)) for _ in range(15)]
        self.point_set2 = [RectPoint([206, 250], 10, (191, 40)) for _ in range(15)]
        for i in range(len(self.point_set1)):
            for _ in range(i*2):
                self.point_set1[i].move()
                self.point_set2[i].move()
        self.hovered = 1
        self.con_hovered = 1
        bgs[0].play_non_stop()

    # 主要进行动画更新，以及判断当前鼠标是否悬浮在某个按钮上
    def update(self):
        for i in range(5):
            self.points[i] += 2
            if self.points[i] >= 600:
                self.points[i] = -150
        if self.hovered == 1:
            for point in self.point_set1:
                point.move()
        if self.con_hovered == 1:
            for point in self.point_set2:
                point.move()
        self.hovered = 0
        self.con_hovered = 0
        if 207 < env["mouse_x"] < 397:
            if 198 < env["mouse_y"] < 238:
                self.hovered = 1
        if 210 < env["mouse_x"] < 420:
            if 250 < env["mouse_y"] < 290:
                self.con_hovered = 1

    # 绘制当前菜单
    def draw(self):
        screen.blit(texture_lib["title_shadow"], (0, 46 + self.float_cycle.get()))
        screen.blit(texture_lib["title"], (0, 47 + self.float_cycle2.get()))
        if self.hovered == 1:
            screen.blit(texture_lib["start_button_hovered"], (0, 197))
        else:
            screen.blit(texture_lib["start_button"], (0, 197))
        if self.con_hovered == 1:
            screen.blit(texture_lib["continue_button_hovered"], (0, 240))
        else:
            screen.blit(texture_lib["continue_button"], (0, 240))
        for point in self.points:
            pygame.draw.polygon(screen, (170, 170, 170),
                                ((point, 163), (point+75, 161), (point+150, 163), (point+75, 165), (point, 163)))
        if self.hovered == 1:
            for i in range(len(self.point_set1)-1):
                pygame.draw.line(screen, (255, 255, 255), self.point_set1[i].get(), self.point_set1[i+1].get())
        if self.con_hovered == 1:
            for i in range(len(self.point_set2)-1):
                pygame.draw.line(screen, (255, 255, 255), self.point_set2[i].get(), self.point_set2[i+1].get())
        screen.blit(texture_lib["copyright"], (0, 0))

    # 处理鼠标点击事件，call的时候根据返回的值来确定处理结果
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.hovered:
                ses[1].play_once()
                return -2
            elif self.con_hovered:
                ses[1].play_once()
                return -3
        return -1


class LevelSelect:
    """
    关卡选择界面，有一个地图，左右两个可拖动箭头，以及8个可点击的关卡选择点
    """
    status_texture = (texture_lib["level_d"], texture_lib["level_p"], texture_lib["level_c"], texture_lib["level_s"])

    def __init__(self, level_at):
        bgs[4].play_non_stop()
        self.float_cycle = ReCycle(6, 4)
        self.level_float = ReCycle(6, 2)
        self.level_points = ((46, 144), (134, 227), (290, 202), (412, 274), (558, 241), (734, 302), (872, 231),
                             (729, 194))
        self.scroll = 0

        self.point_status = [0 for _ in range(9)]
        self.point_status[0] = 2

        self.c_float = 0

        self.current_level = 0

        for _ in range(level_at):
            self.next_level()
        self.arrow_cycle = ReCycle(10, 3)

    # 开启下一关
    def next_level(self):
        self.point_status[self.current_level] = 1
        self.current_level += 1
        self.point_status[self.current_level] = 2

    # 绘制当前地图
    def draw(self):
        screen.blit(texture_lib["menu_route"], (-self.scroll, self.c_float))
        for i in range(len(self.level_points)):
            screen.blit(self.status_texture[self.point_status[i]], (self.level_points[i][0] - self.scroll,
                                                                    self.level_points[i][1] + self.c_float))
            title = chat_font.render("关卡" + str(i+1), False, (255, 255, 255))
            title2 = chat_font.render("关卡" + str(i + 1), False, (0, 0, 0))
            screen.blit(title, (self.level_points[i][0] - self.scroll + 10,
                                self.level_points[i][1] + self.c_float + 35))
            screen.blit(title2, (self.level_points[i][0] - self.scroll + 8,
                                 self.level_points[i][1] + self.c_float + 33))
            if self.point_status[i] == 3:
                screen.blit(texture_lib["level_base"],
                            (self.level_points[i][0] + 7 - self.scroll,
                             self.level_points[i][1] + self.c_float + self.level_float.get() - 75))
                screen.blit(texture_lib["icon" + str(i+1)], (self.level_points[i][0] + 7 - self.scroll,
                                                             self.level_points[i][
                                                            1] + self.c_float + self.level_float.get() - 75))
        arrow_way = self.arrow_cycle.get()
        if self.scroll > 0:
            screen.blit(texture_lib["left_arrow"], (arrow_way, 0))
        if self.scroll < 450:
            screen.blit(texture_lib["right_arrow"], (550-arrow_way, 0))

    # 主要更新动画，同时检测有哪个关卡点被悬浮，以及地图左右滚动
    def update(self):
        self.c_float = self.float_cycle.get()
        for i in range(len(self.level_points)):
            if self.point_status[i] != 0:
                if i == self.current_level:
                    self.point_status[i] = 2
                else:
                    self.point_status[i] = 1
                if self.level_points[i][0] - self.scroll < env["mouse_x"] < self.level_points[i][0] + 75 - self.scroll:
                    if self.level_points[i][1] + self.c_float < env["mouse_y"] \
                            < self.level_points[i][1] + 33 + self.c_float:
                        self.point_status[i] = 3
        if env["mouse_x"] < 50:
            self.scroll -= 5
            if self.scroll < 0:
                self.scroll = 0
        elif env["mouse_x"] > 550:
            self.scroll += 5
            if self.scroll > 450:
                self.scroll = 450

    # 根据鼠标点击来返回处理结果，-1为什么都每点到，否则返回当前点到的关卡
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(len(self.point_status)):
                if self.point_status[i] == 3:
                    ses[1].play_once()
                    return i
        return -1

from animations import *


class Segment:
    """
    蛇的一段，中心在center，以angle角度摆放，宽度是width
    """
    def __init__(self, center, angle, width):
        self.angle = angle + pi/2
        self.width = width
        self.center = center
        self.draw_displacement = [0, 0]
        self.update()

    # 设置宽度
    def set_width(self, width):
        self.width = width

    # 根据角度更新蛇的绘制点
    def update(self):
        self.draw_displacement[0] = cos(self.angle) * self.width
        self.draw_displacement[1] = sin(self.angle) * self.width

    # 获取绘制点一
    def get_point1(self, offset):
        return (self.center[0] + self.draw_displacement[0] + offset[0],
                self.center[1] + self.draw_displacement[1] + offset[1])

    # 获取绘制点二
    def get_point2(self, offset):
        return (self.center[0] - self.draw_displacement[0] + offset[0],
                self.center[1] - self.draw_displacement[1] + offset[1])


class Snake:
    """
    贪吃蛇本体，由许多Segment构成
    """
    def __init__(self, game):
        self.game = game
        self.width = 10
        self.speed = 7
        self.segments = []
        self.direction = 0
        self.poly_points = []
        self.length = 0
        self.seg_width = []
        self.position = [0, 0]
        self.turn_limit = pi/3
        self.outofbound = False
        self.color = (255, 255, 255)

        self.level = 1
        self.current_exp = 0
        self.hp = 100
        self.pre_hp = self.hp
        self.dead = False

        self.hit_points = []

    # 设置当前蛇前进角度
    def set_direction(self, angle):
        d_angle = (angle - self.direction) % (2 * pi)
        if d_angle < self.turn_limit or d_angle > 2 * pi - self.turn_limit:
            self.direction = angle
        elif d_angle < pi:
            self.direction += self.turn_limit
        else:
            self.direction -= self.turn_limit

    # 在蛇前面加一个Segment，segment的宽由一个函数生成
    def increase_length(self):
        self.length += 1
        self.seg_width.append(self.width)
        if self.length > 1:
            a = -(self.width/((self.length - 1)*(self.length - 1)))
            for i in range(self.length):
                self.seg_width[self.length - i - 1] = a * (i * i) + self.width

    # 移动蛇的位置，用于更新offset
    def move(self, dx, dy):
        self.position[0] += dx
        self.position[1] += dy

    # 让蛇长长一节
    def grow(self):
        self.add_head_segment()
        self.increase_length()
        self.add_head_segment()
        self.increase_length()

    # 添加一个头部Segment
    def add_head_segment(self):
        self.move(cos(self.direction) * self.speed, sin(self.direction) * self.speed)
        self.segments.append(Segment((self.position[0], self.position[1]), self.direction, self.width))
        self.hit_points.append((self.position[0], self.position[1]))

    # 移除一个尾部Segment
    def remove_tail_segment(self):
        del self.segments[0]
        del self.hit_points[0]

    # 让蛇往前爬一次
    def crawl(self):
        self.add_head_segment()
        self.remove_tail_segment()

    # 进行更新，更新Segment宽度，当前经验升级，更新血量信息，以及碰撞点与绘制点列表
    def update(self):
        for i in range(self.length):
            self.segments[i].set_width(self.seg_width[i])
            self.segments[i].update()

        del self.poly_points[:]
        for seg in self.segments:
            self.poly_points.append(seg.get_point1(self.game.get_offset()))
        for i in range(self.length - 1, -1, -1):
            self.poly_points.append(self.segments[i].get_point2(self.game.get_offset()))

        if self.current_exp > 100:
            ses[4].play_once()
            # 一级变十级
            # self.level += 10
            self.level += 1
            self.grow()
            self.current_exp = 0
            for point in self.hit_points:
                self.game.map.animations.append(LevelUp(point))

        # 掉血量
        if self.outofbound:
            # self.hp -= 1
            # 出边界血量
            self.hp -= 0

        if self.hp < 0:
            self.dead = True
        if self.pre_hp > self.hp:
            self.color = (255, 100, 100)
        else:
            self.color = (255, 255, 255)
        self.pre_hp = self.hp

    # 使用多边形方法绘制蛇
    def draw(self):
        pygame.draw.polygon(screen, self.color, self.poly_points)
        pygame.draw.circle(screen, self.color, (int(self.position[0] + self.game.get_offset()[0]),
                                                int(self.position[1] + self.game.get_offset()[1])),
                           self.width + 2)

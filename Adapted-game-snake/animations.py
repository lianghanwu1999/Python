from config import *
from cycle import *
import random


class ChargeLine:
    """
    ChargeLine为多条线向中心聚集的动画，为巨型激光前摇
    此类为一条线
    """
    def __init__(self, pos, width, height):
        self.height = height
        self.pos = [pos[0], pos[1]]
        self.distance = width
        self.color = random.randint(100, 200)
        self.thickness = random.randint(2, 5)
        self.dead = False

    # 绘制动画
    def draw(self, offset):
        pygame.draw.line(screen, (self.color, self.color, self.color),
                         (self.pos[0] + self.distance + offset[0], self.pos[1] + offset[1]),
                         (self.pos[0] + self.distance + offset[0], self.pos[1] + self.height + offset[1]),
                         self.thickness)

        pygame.draw.line(screen, (self.color, self.color, self.color),
                         (self.pos[0] - self.distance + offset[0], self.pos[1] + offset[1]),
                         (self.pos[0] - self.distance + offset[0], self.pos[1] + self.height + offset[1]),
                         self.thickness)
        self.distance -= 10
        if self.distance <= 0:
            self.dead = True


class Charge:
    """
    为激光前摇，多条ChargeLine向中间聚集
    """
    def __init__(self, pos, width, height, num_lines):
        self.lines = []
        self.num_lines = num_lines
        self.width = width
        self.height = height
        self.pos = pos
        self.count = 0
        self.dead = False
        self.current_chance = num_lines/2

    # 绘制所有ChargeLine
    def draw(self, offset):
        for i in range(len(self.lines) - 1, -1, -1):
            if self.lines[i].dead:
                del self.lines[i]
            else:
                self.lines[i].draw(offset)

    # 更新所有ChargeLine，同时生成新的Lines
    def update(self):
        if self.count < self.num_lines:
            if random.randint(0, int(self.current_chance)) == 0:
                self.count += 1
                self.current_chance -= 0.5
                self.lines.append(ChargeLine(self.pos, self.width, self.height))
        elif not self.lines:
            self.dead = True


"""
下面所有动画均为循环帧绘制，绘制一次则死亡
"""


class ParticleExplode:
    def __init__(self, pos):
        self.cycle = Cycle(4, 2)
        self.pos = (pos[0] - 25, pos[1] - 25)
        self.dead = False

    def draw(self, offset):
        screen.blit(texture_lib["particle_explode"], (self.pos[0] + offset[0], self.pos[1] + offset[1]),
                    pygame.Rect(0, self.cycle.get()*50, 50, 50))

    def update(self):
        if self.cycle.one:
            self.dead = True


class LevelUp:
    def __init__(self, pos):
        self.cycle = Cycle(4, 3)
        self.pos = (pos[0] - 30, pos[1] - 30)
        self.dead = False

    def draw(self, offset):
        screen.blit(texture_lib["level_up"], (self.pos[0] + offset[0], self.pos[1] + offset[1]),
                    pygame.Rect(0, self.cycle.get()*60, 60, 60))

    def update(self):
        if self.cycle.one:
            self.dead = True

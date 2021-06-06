from animations import *
from cycle import *


class Obstacles:
    """
    所有可以伤害到玩家的物品的父类
    """
    def __init__(self, map_in):
        self.map = map_in
        self.damage = 0
        self.attack = False
        self.dead = False
        self.bounded = False
        self.pos = [0, 0]

    # 判断物品是否与玩家碰撞
    def collide_with(self, snake):
        pass

    # 绘制当前物品
    def draw(self, offset):
        pass

    # 更新当前物品
    def update(self):
        pass


class Beam(Obstacles):
    """
    激光对象，在map_in里pos位置添加一个width宽度length长度color颜色damage伤害的激光，
    改激光的朝向是direction，在发射前又pre_t帧的前摇，动画时间为last_t * 2
    """
    def __init__(self, map_in, pos, length, direction, width=30, pre_t=100, last_t=6, color=(242, 245, 66), damage=20):
        Obstacles.__init__(self, map_in)
        self.damage = damage
        self.color = color
        self.pos = pos
        self.point1 = [pos[0], pos[1]]
        self.point2 = [pos[0], pos[1]]
        if direction == "v":
            self.point2[1] += length
        elif direction == "h":
            self.point2[0] += length
        self.width = width
        self.tick = 0
        self.direction = direction

        self.pre_t = pre_t
        self.last_t = last_t

        self.speed = width / self.last_t

    # 同父类
    def collide_with(self, snake):
        if self.direction == "v":
            for i in range(0, len(snake.hit_points)-2, 2):
                if not(self.pos[0] - self.width/2 > max(snake.hit_points[i][0], snake.hit_points[i+2][0]) or
                        self.pos[0] + self.width/2 < min(snake.hit_points[i][0], snake.hit_points[i+2][0])):
                    self.map.animations.append(ParticleExplode(snake.hit_points[i]))
                    self.map.animations.append(ParticleExplode(snake.hit_points[i + 2]))
                    ses[3].play_once()
                    return True

        elif self.direction == "h":
            for i in range(0, len(snake.hit_points)-2, 2):
                if not (self.pos[1] - self.width/2 > max(snake.hit_points[i][1], snake.hit_points[i + 2][1]) or
                        self.pos[1] + self.width/2 < min(snake.hit_points[i][1], snake.hit_points[i + 2][1])):
                    self.map.animations.append(ParticleExplode(snake.hit_points[i]))
                    self.map.animations.append(ParticleExplode(snake.hit_points[i + 2]))
                    ses[3].play_once()
                    return True
        return False

    # 同父类
    def update(self):
        if self.tick == self.pre_t:
            if self.width < 100:
                ses[6].play_once()

        if self.tick > self.pre_t + self.last_t*2:
            self.dead = True
        else:
            self.tick += 1

        if self.tick == self.pre_t + self.last_t:
            self.attack = True
        else:
            self.attack = False

    # 同父类
    def draw(self, offset):
        if self.tick < self.pre_t:
            pygame.draw.line(screen, (255, 100, 100),
                             (self.point1[0] + offset[0], self.point1[1] + offset[1]),
                             (self.point2[0] + offset[0], self.point2[1] + offset[1]), 2)
        elif self.tick < self.pre_t + self.last_t:
            pygame.draw.line(screen, self.color,
                             (self.point1[0] + offset[0], self.point1[1] + offset[1]),
                             (self.point2[0] + offset[0], self.point2[1] + offset[1]),
                             int(self.speed * (self.tick - self.pre_t)))
        elif self.tick < self.pre_t + self.last_t*2:
            pygame.draw.line(screen, self.color,
                             (self.point1[0] + offset[0], self.point1[1] + offset[1]),
                             (self.point2[0] + offset[0], self.point2[1] + offset[1]),
                             int(self.speed * (self.pre_t + self.last_t*2 - self.tick)))


class LastBeam(Obstacles):
    """
    移动激光，同激光，object_t为跟随移动的目标
    """
    def __init__(self, map_in, pos, height, orientation, object_t, width=30, pre_t=100, dur_t=60,
                 last_t=6, color=(242, 245, 66), damage=20):
        Obstacles.__init__(self, map_in)
        self.damage = damage
        self.color = color
        self.pos = [pos[0], pos[1]]
        self.point1 = [pos[0], pos[1]]
        self.point2 = [pos[0], pos[1]]
        self.orientation = orientation
        if self.orientation == "v":
            self.point2[1] += height
        else:
            self.point2[0] += height
        self.width = width
        self.tick = 0
        self.height = height

        self.pre_t = pre_t
        self.dur_t = dur_t
        self.last_t = last_t
        self.objectT = object_t

        self.speed = width / self.last_t
        self.attack_cycle = Cycle(20, 0)

    # 同父类
    def collide_with(self, snake):
        if self.orientation == "v":
            for i in range(0, len(snake.hit_points)-2, 2):
                if not(self.pos[0] - self.width/2 > max(snake.hit_points[i][0], snake.hit_points[i+2][0]) or
                        self.pos[0] + self.width/2 < min(snake.hit_points[i][0], snake.hit_points[i+2][0])):
                    self.map.animations.append(ParticleExplode(snake.hit_points[i]))
                    self.map.animations.append(ParticleExplode(snake.hit_points[i + 2]))
                    ses[3].play_once()
                    return True

        elif self.orientation == "h":
            for i in range(0, len(snake.hit_points)-2, 2):
                if not (self.pos[1] - self.width/2 > max(snake.hit_points[i][1], snake.hit_points[i + 2][1]) or
                        self.pos[1] + self.width/2 < min(snake.hit_points[i][1], snake.hit_points[i + 2][1])):
                    self.map.animations.append(ParticleExplode(snake.hit_points[i]))
                    self.map.animations.append(ParticleExplode(snake.hit_points[i + 2]))
                    ses[3].play_once()
                    return True
        return False

    # 同父类
    def update(self):
        self.tick += 1
        self.attack = False
        if self.pre_t + self.last_t < self.tick < self.pre_t + self.last_t + self.dur_t:
            if self.attack_cycle.get() == 0:
                self.attack = True

    # 同父类
    def draw(self, offset):
        if self.tick == self.pre_t + self.last_t:
            ses[6].play_once()
        if self.tick < self.pre_t:
            pygame.draw.line(screen, (255, 100, 100),
                             (self.point1[0] + offset[0], self.point1[1] + offset[1]),
                             (self.point2[0] + offset[0], self.point2[1] + offset[1]), 2)
        elif self.tick < self.pre_t + self.last_t:
            pygame.draw.line(screen, self.color,
                             (self.point1[0] + offset[0], self.point1[1] + offset[1]),
                             (self.point2[0] + offset[0], self.point2[1] + offset[1]),
                             int(self.speed * (self.tick - self.pre_t)))
        elif self.tick < self.pre_t + self.last_t + self.dur_t:
            pygame.draw.line(screen, self.color,
                             (self.point1[0] + offset[0], self.point1[1] + offset[1]),
                             (self.point2[0] + offset[0], self.point2[1] + offset[1]),
                             self.width)
        elif self.tick < self.pre_t + self.last_t*2 + self.dur_t:
            pygame.draw.line(screen, self.color,
                             (self.point1[0] + offset[0], self.point1[1] + offset[1]),
                             (self.point2[0] + offset[0], self.point2[1] + offset[1]),
                             int(self.speed * (self.pre_t + self.last_t*2 + self.dur_t - self.tick)))
        else:
            self.dead = True


class Bullet(Obstacles):
    """
    子弹，在map_in的x，y位置生成一个damage伤害半径radius的子弹，以vx，vy的速度移动，若one_time为True
    则在碰撞后删除自己。
    """
    def __init__(self, map_in, damage, radius, x, y, vx, vy, one_time=True):
        Obstacles.__init__(self, map_in)
        self.damage = damage
        self.radius = radius
        self.speed = [vx, vy]
        self.pos = [x, y]
        self.bounded = True

        self.attack = True
        self.dead_on_collide = one_time

    # 同父类
    def update(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

    # 同父类
    def draw(self, offset):
        screen.blit(texture_lib["bullet"], (self.pos[0] + offset[0] - 20, self.pos[1] + offset[1] - 20))

    # 同父类
    def collide_with(self, snake):
        for i in range(0, len(snake.hit_points), 2):
            if get_distance(snake.hit_points[i], self.pos) < snake.width + self.radius - 3:
                if self.dead_on_collide:
                    self.dead = True
                self.map.animations.append(ParticleExplode(snake.hit_points[i]))
                ses[3].play_once()
                return True
        return False


class ExpBall:
    """
    在pos位置经验为points的经验球
    """
    def __init__(self, pos, points=10):
        self.pos = pos
        self.points = points
        self.cycle = Cycle(4, 6)

    # 绘制经验球
    def draw(self, offset):
        screen.blit(texture_lib["food"], (self.pos[0] + offset[0] - 22, self.pos[1] + offset[1] - 22),
                    pygame.Rect(0, self.cycle.get()*45, 45, 45))


class OneCanon:
    """
    发射Bullet的大炮
    """
    def __init__(self, pos):
        self.cast = False
        self.attacking = False
        self.attack_cycle = Cycle(2, 50)
        self.attack_ani_cycle = Cycle(4, 2)
        self.pos = [pos[0], pos[1]]
        self.dead = False

    # 进行攻击
    def attack(self):
        self.attacking = True
        self.attack_ani_cycle = Cycle(4, 4)

    # 更新大炮，主要处理更新以及动画
    def update(self):
        self.cast = False
        if self.attacking:
            if self.attack_ani_cycle.one:
                self.attacking = False
                self.cast = True
        else:
            if self.attack_cycle.get() == 0 and self.attack_cycle.changed():
                self.attack()
                self.attack_cycle.current += random.randint(0, 20)

    # 绘制大炮
    def draw(self, offset):
        if self.attacking:
            screen.blit(texture_lib["one_cannon"], (self.pos[0]+offset[0], self.pos[1]+offset[1]),
                        pygame.Rect(0, self.attack_ani_cycle.get() * 80, 80, 80))
        else:
            screen.blit(texture_lib["one_cannon"], (self.pos[0] + offset[0], self.pos[1] + offset[1]),
                        pygame.Rect(0, 0, 80, 80))


class CrossCanon:
    """
    十字激光发射器
    """
    def __init__(self, pos):
        self.cast = False
        self.attacking = False
        self.attack_cycle = Cycle(2, 80)
        self.attack_ani_cycle = Cycle(4, 4)
        self.pos = [pos[0], pos[1]]
        self.dead = False

    # 进行攻击
    def attack(self):
        self.attacking = True
        self.attack_ani_cycle = Cycle(4, 4)

    # 更新激光发射器，主要是动画以及攻击循环
    def update(self):
        self.cast = False
        if self.attacking:
            if self.attack_ani_cycle.one:
                self.attacking = False
                self.cast = True
        else:
            if self.attack_cycle.get() == 0 and self.attack_cycle.changed():
                self.attack()
                self.attack_cycle.tick += random.randint(0, 40)

    # 绘制激光炮
    def draw(self, offset):
        if self.attacking:
            screen.blit(texture_lib["cross_cannon"], (self.pos[0]+offset[0], self.pos[1]+offset[1]),
                        pygame.Rect(0, self.attack_ani_cycle.get() * 80, 80, 80))
        else:
            screen.blit(texture_lib["cross_cannon"], (self.pos[0] + offset[0], self.pos[1] + offset[1]),
                        pygame.Rect(0, 0, 80, 80))


class MovingBeamCannon:
    """
    移动激光炮，在map_in的pos位置绘制一个高度为height朝向orientation，向着
    direction移动length距离的移动激光炮，前摇为cd
    """
    def __init__(self, map_in, pos, orientation, direction, length, height, cd=60):
        self.orientation = orientation
        self.height = height
        self.cast = False
        self.attacking = False
        self.pos = [pos[0], pos[1]]
        self.speed = 2
        if self.orientation == "v":
            self.end = pos[0] + length * direction
        else:
            self.end = pos[1] + length * direction
        self.dead = False
        self.length = length
        self.cd = cd
        self.direction = direction
        self.end_tick = cd
        self.dying = False
        self.beam = LastBeam(map_in, self.pos, self.height, self.orientation, self,
                             pre_t=cd-20, last_t=20, dur_t=self.length/self.speed)

    # 获取该激光炮的激光
    def get_beam(self):
        return self.beam

    # 更新激光炮，主要是移动位置，以及进行attack tick判断
    def update(self):
        if not self.attacking:
            if self.cd > 0:
                self.cd -= 1
            else:
                self.attacking = True
        elif self.dying:
            self.end_tick -= 1
            if self.end_tick < 0:
                self.dead = True
        else:
            if self.direction == 1:
                if self.orientation == "v":
                    self.pos[0] += self.speed
                    if self.pos[0] > self.end:
                        self.dying = True
                elif self.orientation == "h":
                    self.pos[1] += self.speed
                    if self.pos[1] > self.end:
                        self.dying = True

            elif self.direction == -1:
                if self.orientation == "v":
                    self.pos[0] -= self.speed
                    if self.pos[0] < self.end:
                        self.dying = True
                elif self.orientation == "h":
                    self.pos[1] -= self.speed
                    if self.pos[1] < self.end:
                        self.dying = True
            self.beam.pos[0] = self.pos[0]
            self.beam.pos[1] = self.pos[1]
            if self.orientation == "v":
                self.beam.point1[0] = self.pos[0]
                self.beam.point2[0] = self.pos[0]
            else:
                self.beam.point1[1] = self.pos[1]
                self.beam.point2[1] = self.pos[1]

    # 绘制激光炮
    def draw(self, offset):
        if self.orientation == "v":
            screen.blit(texture_lib["line_top"], (self.pos[0] + offset[0] - 40, self.pos[1] + offset[1] - 50))
            screen.blit(texture_lib["line_bottom"], (self.pos[0] + offset[0] - 40,
                                                     self.pos[1] + offset[1] - 40 + self.height))
        else:
            screen.blit(texture_lib["line_right"], (self.pos[0] + offset[0] - 50, self.pos[1] + offset[1] - 40))
            screen.blit(texture_lib["line_left"], (self.pos[0] + offset[0] + self.height - 40,
                                                   self.pos[1] + offset[1] - 40))


class CenterSlice(Obstacles):
    """
    中心十字旋转，boxed目前没用因为没时间做，本来打算是激光四周是方形的
    伤害为damage，以speed速度在map_in旋转，中心是0，0
    """
    def __init__(self, map_in, damage, speed, boxed):
        Obstacles.__init__(self, map_in)
        self.boxed = boxed
        self.damage = damage
        self.radius = boxed*1.414

        self.angle = 0.0
        self.speed = speed
        self.pos = [0, 0]
        self.bounded = False
        self.attack = True
        self.dead_on_collide = False
        self.shade = 0.05

        self.current_rise = [0, 0, 0, 0]
        self.attack = True

    # 同父类
    def update(self):
        self.angle += self.speed
        if self.angle > pi:
            self.angle -= 2 * pi
        self.current_rise[0] = cos(self.angle - self.shade) * self.radius
        self.current_rise[1] = sin(self.angle - self.shade) * self.radius
        self.current_rise[2] = cos(self.angle + self.shade) * self.radius
        self.current_rise[3] = sin(self.angle + self.shade) * self.radius

    # 同父类
    def draw(self, offset):
        pygame.draw.polygon(screen, (170, 0, 0),
                            ((-self.current_rise[0] + offset[0], -self.current_rise[1] + offset[1]),
                             (self.current_rise[0] + offset[0], self.current_rise[1] + offset[1]),
                             (self.current_rise[2] + offset[0], self.current_rise[3] + offset[1]),
                             (-self.current_rise[2] + offset[0], -self.current_rise[3] + offset[1])))

        pygame.draw.polygon(screen, (170, 0, 0),
                            ((-self.current_rise[1] + offset[0], self.current_rise[0] + offset[1]),
                             (self.current_rise[1] + offset[0], -self.current_rise[0] + offset[1]),
                             (self.current_rise[3] + offset[0], -self.current_rise[2] + offset[1]),
                             (-self.current_rise[3] + offset[0], self.current_rise[2] + offset[1])))

    # 同父类
    def collide_with(self, snake):
        for i in range(0, len(snake.hit_points), 2):
            for i2 in range(4):
                diff = self.angle + (i2*pi/2) - get_angle(snake.hit_points[i][0], snake.hit_points[i][1])
                while diff > pi:
                    diff -= pi * 2
                if -self.shade < diff < self.shade:
                    self.map.animations.append(ParticleExplode(snake.hit_points[i]))
                    return True
        return False

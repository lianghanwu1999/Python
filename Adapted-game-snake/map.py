from fights import *


class Level:
    """
    关卡父类
    """
    def __init__(self):
        pass

    # 判断是否过关
    def is_passed(self):
        return False


class Map(Level):
    """
    地图，存储数据有所有攻击，经验球，动画以及物品（大炮，激光炮等）
    per_exp为每个经验球的经验，food_count是场上经验球数量，pass_level是过关等级
    """
    def __init__(self, game):
        Level.__init__(self)
        self.game = game
        self.objects = []
        self.exp_balls = []
        self.deme = [300, 300]
        self.snake = None
        self.attacks = []
        self.food_count = 5
        self.per_exp = 10
        self.pass_level = 1

        self.boarder_cycle = ReCycle(6, 1)

        self.animations = []

    # 判断当前蛇是否死亡
    def is_dead(self):
        return self.snake.hp < 0

    # 绘制四周边框，是动画
    def draw_boarder(self, offset):
        c = self.boarder_cycle.get()
        pygame.draw.line(screen, (255, 255, 255),
                         (-self.deme[0] + offset[0] + c, -self.deme[1] + offset[1]),
                         (-self.deme[0] + offset[0] + c, self.deme[1] + offset[1]), 2)
        pygame.draw.line(screen, (255, 255, 255),
                         (-self.deme[0] + offset[0] - c, -self.deme[1] + offset[1]),
                         (-self.deme[0] + offset[0] - c, self.deme[1] + offset[1]), 2)

        pygame.draw.line(screen, (255, 255, 255),
                         (self.deme[0] + offset[0] + c, -self.deme[1] + offset[1]),
                         (self.deme[0] + offset[0] + c, self.deme[1] + offset[1]), 2)
        pygame.draw.line(screen, (255, 255, 255),
                         (self.deme[0] + offset[0] - c, -self.deme[1] + offset[1]),
                         (self.deme[0] + offset[0] - c, self.deme[1] + offset[1]), 2)

        pygame.draw.line(screen, (255, 255, 255),
                         (self.deme[0] + offset[0], self.deme[1] + offset[1] + c),
                         (-self.deme[0] + offset[0], self.deme[1] + offset[1] + c), 2)
        pygame.draw.line(screen, (255, 255, 255),
                         (self.deme[0] + offset[0], self.deme[1] + offset[1] - c),
                         (-self.deme[0] + offset[0], self.deme[1] + offset[1] - c), 2)

        pygame.draw.line(screen, (255, 255, 255),
                         (self.deme[0] + offset[0], -self.deme[1] + offset[1] + c),
                         (-self.deme[0] + offset[0], -self.deme[1] + offset[1] + c), 2)
        pygame.draw.line(screen, (255, 255, 255),
                         (self.deme[0] + offset[0], -self.deme[1] + offset[1] - c),
                         (-self.deme[0] + offset[0], -self.deme[1] + offset[1] - c), 2)

        pygame.draw.rect(screen, (255, 255, 255),
                         pygame.Rect(offset[0] - self.deme[0] - 15, offset[1] - self.deme[1] - 15, 30,
                                     30))
        pygame.draw.rect(screen, (255, 255, 255),
                         pygame.Rect(offset[0] + self.deme[0] - 15, offset[1] - self.deme[1] - 15, 30,
                                     30))
        pygame.draw.rect(screen, (255, 255, 255),
                         pygame.Rect(offset[0] - self.deme[0] - 15, offset[1] + self.deme[1] - 15, 30,
                                     30))
        pygame.draw.rect(screen, (255, 255, 255),
                         pygame.Rect(offset[0] + self.deme[0] - 15, offset[1] + self.deme[1] - 15, 30,
                                     30))

    # 添加一个激光，具体参数清参考fights里的Beam类
    def add_beam(self, position, length, direction, width=30):
        self.attacks.append(Beam(self, position, length, direction, width))

    # 添加一个子弹，具体参数清参考fights里的Bullet类
    def add_bullet(self, position, speed, radius, damage):
        self.attacks.append(Bullet(self, damage, radius, position[0], position[1], speed[0], speed[1]))

    # 设置当前蛇
    def set_snake(self, snake):
        self.snake = snake

    # 绘制背景底色
    def draw_background(self, offset):
        pygame.draw.rect(screen, (70, 70, 70),
                         pygame.Rect(offset[0] - self.deme[0], offset[1] - self.deme[1], self.deme[0] * 2,
                                     self.deme[1] * 2))

    # 绘制地图上的所有物件
    def draw(self, offset):
        for i in range(len(self.exp_balls)-1, -1, -1):
            self.exp_balls[i].draw(offset)
        for i in range(len(self.attacks) - 1, -1, -1):
            self.attacks[i].draw(offset)
        for i in range(len(self.objects) - 1, -1, -1):
            self.objects[i].draw(offset)
        for i in range(len(self.animations)-1, -1, -1):
            self.animations[i].draw(offset)

        if self.snake.outofbound:
            screen.blit(texture_lib["danger"], (0, 0))

        self.draw_boarder(offset)
        pass_render = chat_font.render("目标等级"+str(self.pass_level), False, (255, 255, 255))
        screen.blit(pass_render, (450, 30))

    # 更新地图上的所有物品，若有物品为dead则删除物品，同时判断攻击tick，以及经验球与蛇的碰撞
    def update(self):
        for i in range(len(self.exp_balls)-1, -1, -1):
            if get_distance(self.snake.position, self.exp_balls[i].pos) < 20:
                self.snake.current_exp += self.exp_balls[i].points
                ses[2].play_once()
                del self.exp_balls[i]

        for i in range(len(self.animations) - 1, -1, -1):
            if self.animations[i].dead:
                del self.animations[i]
            else:
                self.animations[i].update()

        for i in range(len(self.attacks)-1, -1, -1):
            self.attacks[i].update()
            if self.attacks[i].attack:
                if self.attacks[i].collide_with(self.snake):
                    self.snake.hp -= self.attacks[i].damage
            if self.attacks[i].bounded:
                if self.attacks[i].pos[0] > self.deme[0] or \
                     self.attacks[i].pos[0] < -self.deme[0] or \
                     self.attacks[i].pos[1] > self.deme[1] or \
                     self.attacks[i].pos[1] < -self.deme[1]:
                    self.attacks[i].dead = True
            if self.attacks[i].dead:
                del self.attacks[i]

        for i in range(len(self.objects)-1, -1, -1):
            self.objects[i].update()
            if self.objects[i].dead:
                del self.objects[i]

        if len(self.exp_balls) < self.food_count:
            self.exp_balls.append(ExpBall((random.randint(-self.deme[0], self.deme[0]),
                                           random.randint(-self.deme[1], self.deme[1])), self.per_exp))

        if (self.snake.position[0] < -self.deme[0] or
                self.snake.position[0] > self.deme[0] or
                self.snake.position[1] < -self.deme[1] or
                self.snake.position[1] > self.deme[1]):
            self.snake.outofbound = True
        else:
            self.snake.outofbound = False


class Level1(Map):
    """
    第一关，场地为200，200
    """
    def __init__(self, game):
        Map.__init__(self, game)
        self.deme[0] = 200
        self.deme[1] = 200
        self.pass_level = 3

    # 同父类
    def is_passed(self):
        if self.snake.level >= self.pass_level:
            return True
        return False

    # 同父类
    def update(self):
        Map.update(self)


class Level2(Map):
    """
    第二关，有两个大炮
    """
    def __init__(self, game):
        Map.__init__(self, game)
        self.deme[0] = 250
        self.deme[1] = 250
        self.pass_level = 5
        self.per_exp = 15

        self.objects.append(OneCanon((-310, 100)))
        self.objects.append(OneCanon((-310, -100)))

    # 同父类
    def is_passed(self):
        if self.snake.level >= self.pass_level:
            return True
        return False

    # 大炮发射炮弹
    def update(self):
        Map.update(self)
        if self.objects[0].cast:
            self.add_bullet((self.objects[0].pos[0]+70, self.objects[0].pos[1]+40), (5, 0), 15, 10)
            ses[5].play_once()
        if self.objects[1].cast:
            self.add_bullet((self.objects[1].pos[0]+70, self.objects[1].pos[1]+40), (5, 0), 15, 10)
            ses[5].play_once()


class Level3(Map):
    """
    第三关，一个十字激光
    """
    def __init__(self, game):
        Map.__init__(self, game)
        self.deme[0] = 300
        self.deme[1] = 300
        self.per_exp = 30
        self.pass_level = 10

        self.objects.append(CrossCanon((-40, -40)))

    # 同父类
    def is_passed(self):
        if self.snake.level >= self.pass_level:
            return True
        return False

    # 发射十字激光
    def update(self):
        Map.update(self)
        if self.objects[0].cast:
            self.add_beam((-300, 0), 600, "h")
            self.add_beam((0, -300), 600, "v")


class Level4(Map):
    """
    第四关，一个移动激光
    """
    def __init__(self, game):
        Map.__init__(self, game)
        self.deme[0] = 350
        self.deme[1] = 350
        self.per_exp = 30
        self.beam_cycle = Cycle(80, 0)
        self.pass_level = 10

    # 同父类
    def is_passed(self):
        if self.snake.level >= self.pass_level:
            return True
        return False

    # 一共有八种激光移动方式，随机生成一个
    def update(self):
        Map.update(self)
        if not self.attacks:
            if self.beam_cycle.get() == 0:
                generated = random.randint(0, 7)
                if generated == 0:
                    self.objects.append(MovingBeamCannon(self, (-350, -350), "h", 1, 300, 700))
                    self.attacks.append(self.objects[-1].get_beam())
                elif generated == 1:
                    self.objects.append(MovingBeamCannon(self, (-350, 0), "h", 1, 300, 700))
                    self.attacks.append(self.objects[-1].get_beam())
                elif generated == 2:
                    self.objects.append(MovingBeamCannon(self, (-350, 350), "h", -1, 300, 700))
                    self.attacks.append(self.objects[-1].get_beam())
                elif generated == 3:
                    self.objects.append(MovingBeamCannon(self, (-350, 0), "h", -1, 300, 700))
                    self.attacks.append(self.objects[-1].get_beam())
                elif generated == 4:
                    self.objects.append(MovingBeamCannon(self, (-350, -350), "v", 1, 300, 700))
                    self.attacks.append(self.objects[-1].get_beam())
                elif generated == 5:
                    self.objects.append(MovingBeamCannon(self, (0, -350), "v", 1, 300, 700))
                    self.attacks.append(self.objects[-1].get_beam())
                elif generated == 6:
                    self.objects.append(MovingBeamCannon(self, (350, -350), "v", -1, 300, 700))
                    self.attacks.append(self.objects[-1].get_beam())
                elif generated == 7:
                    self.objects.append(MovingBeamCannon(self, (0, -350), "v", -1, 300, 700))
                    self.attacks.append(self.objects[-1].get_beam())


class Level5(Map):
    """
    第五关，有一个旋转激光
    """
    def __init__(self, game):
        Map.__init__(self, game)
        self.deme[0] = 400
        self.deme[1] = 400
        self.per_exp = 30
        self.count_down = 80
        self.pass_level = 10

    # 同父类
    def is_passed(self):
        if self.snake.level >= self.pass_level:
            return True
        return False

    # 在最开始延时一段时间再生成激光
    def update(self):
        Map.update(self)
        self.count_down -= 1
        if self.count_down == 0:
            self.attacks.append(CenterSlice(self, 1, 0.005, 400))


class Level6(Map):
    """
    第六关，有一个巨型激光
    """
    def __init__(self, game):
        Map.__init__(self, game)
        self.deme[0] = 300
        self.deme[1] = 300
        self.per_exp = 25
        self.attacked = True
        self.current_attack_pos = (-150, -300)
        self.pass_level = 10

        self.attack_countdown = 90
        self.attack_tick = self.attack_countdown

    # 同父类
    def is_passed(self):
        if self.snake.level >= self.pass_level:
            return True
        return False

    # 在激光前摇动画结束的时候生成一个巨型激光，否则根据攻击tick来生成一个前摇
    def update(self):
        Map.update(self)

        if not self.attacked and not self.animations:
            self.attack_tick = self.attack_countdown
            self.attacked = True
            self.attacks.append(Beam(self, self.current_attack_pos, 600, "v", last_t=10, pre_t=0, width=300, damage=40))
            ses[0].play_once()
            self.game.shake("v", 60)
        elif not self.animations and not self.attacks:
            self.attack_tick -= 1
            if self.attack_tick < 0:
                self.attacked = False
                if random.randint(0, 1) == 0:
                    self.current_attack_pos = (-150, -300)
                else:
                    self.current_attack_pos = (150, -300)
                self.animations.append(Charge(self.current_attack_pos, 150, 600, 20))


class Level7(Map):
    """
    第七关，有四条随机横向或者竖向的激光
    """
    def __init__(self, game):
        Map.__init__(self, game)
        self.deme[0] = 400
        self.deme[1] = 400
        self.per_exp = 40
        self.pass_level = 15

        self.current_wave = ((300, -400), (100, -400), (-100, -400), (-300, -400), "v")
        self.attacking = True
        self.attack_tick = 0
        self.attack_speed = 20

        self.attack_cycle = Cycle(120, 0)

    # 同父类
    def is_passed(self):
        if self.snake.level >= self.pass_level:
            return True
        return False

    # 生成四条横向或者竖向的激光
    def update(self):
        Map.update(self)
        if self.attacking:
            self.attack_tick += 1
            if self.attack_tick == self.attack_speed:
                self.attacks.append(Beam(self, self.current_wave[0], 800, self.current_wave[4],
                                         pre_t=80, width=50, damage=20))
            elif self.attack_tick == self.attack_speed*2:
                self.attacks.append(Beam(self, self.current_wave[1], 800, self.current_wave[4],
                                         pre_t=80, width=50, damage=20))
            elif self.attack_tick == self.attack_speed*3:
                self.attacks.append(Beam(self, self.current_wave[2], 800, self.current_wave[4],
                                         pre_t=80, width=50, damage=20))
            elif self.attack_tick == self.attack_speed*4:
                self.attacks.append(Beam(self, self.current_wave[3], 800, self.current_wave[4],
                                         pre_t=80, width=50, damage=20))
            elif self.attack_tick > self.attack_speed * 4:
                self.attacking = False
                self.attack_tick = 0
        elif self.attack_cycle.get() == 0:
            self.attacking = True
            mode = random.randint(1, 4)
            if mode == 1:
                self.current_wave = ((300, -400), (100, -400), (-100, -400), (-300, -400), "v")
            elif mode == 2:
                self.current_wave = ((-300, -400), (-100, -400), (100, -400), (300, -400), "v")
            elif mode == 3:
                self.current_wave = ((-400, -300), (-400, -100), (-400, 100), (-400, 300), "h")
            elif mode == 4:
                self.current_wave = ((-400, 300), (-400, 100), (-400, -100), (-400, -300), "h")


class Level8(Map):
    """
    第八关，每吃一个果子升一级，可以（基本上）无限玩下去
    """
    def __init__(self, game):
        Map.__init__(self, game)
        self.deme[0] = 400
        self.deme[1] = 400
        self.per_exp = 101
        self.food_count = 20
        self.pass_level = 99999

    def is_passed(self):
        return False

    def update(self):
        Map.update(self)

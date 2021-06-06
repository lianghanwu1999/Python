import random


class Cycle:
    """
    正序循环对象，主要用于动画帧，以及攻击间距，num为循环数量，speed为循环速度
    """
    def __init__(self, num, speed):
        self.tick = 0
        self.current = 0
        self.speed = speed
        self.num = num
        self.one = False
        self.prev = self.current

    # 获取当前循环次数以及更新到下一个次数
    def get(self):
        self.tick += 1
        self.prev = self.current
        if self.tick > self.speed:
            self.tick = 0
            self.current += 1
            if self.current >= self.num:
                self.current = 0
        if self.tick+1 > self.speed and self.current+1 >= self.num:
            self.one = True
        return self.current

    # 重置循环
    def reset(self):
        self.tick = 0
        self.current = 0

    # 判断本次循环次数与上次是否发生变化
    def changed(self):
        return self.prev != self.current


class ReCycle:
    """
    正序循环，到结尾后倒序循环回来，num是循环次数，speed为循环速度，从start开始循环，
    主要用于悬浮动画
    """
    def __init__(self, num, speed, start=0):
        self.tick = 0
        self.current = start
        self.speed = speed
        self.num = num
        self.one = False
        self.v = 1
        self.prev = self.current

    # 获取当前循环次数以及更新到下一个次数
    def get(self):
        self.tick += 1
        if self.tick > self.speed:
            self.tick = 0
            self.prev = self.current
            self.current += self.v
            if self.current >= self.num:
                self.current = self.num - 1
                self.v = -1
                self.one = True
            elif self.current < 0:
                self.current = 0
                self.v = 1
        return self.current

    # 重置循环
    def reset(self):
        self.tick = 0
        self.current = 0

    # 判断本次循环次数与上次是否发生变化
    def changed(self):
        return self.prev != self.current


class RandCycle:
    """
    随机循环，depreciated
    同正序循环，但是每次走随机数量的步数，range_in为每次步数的范围
    """
    def __init__(self, num, speed, range_in):
        self.tick = 0
        self.current = 0
        self.speed = speed
        self.num = num
        self.one = False
        self.range = range_in
        self.prev = self.current

    # 判断本次循环次数与上次是否发生改变
    def changed(self):
        return self.prev != self.current

    # 获取当前循环次数，并更新到下次循环次数
    def get(self):
        self.tick += random.randint(self.range[0], self.range[1])
        self.prev = self.current
        if self.tick > self.speed:
            self.tick = 0
            self.current += 1
            if self.current >= self.num:
                self.current = 0
        if self.tick+1 > self.speed and self.current+1 >= self.num:
            self.one = True
        return self.current

    #重置循环
    def reset(self):
        self.tick = 0
        self.current = 0

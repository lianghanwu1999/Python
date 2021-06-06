from config import *
from cycle import *


class ChatBox:
    """
    聊天框对象，在pos位置绘制一个宽度为200像素的聊天框，动画从start开始往上进行，
    text若超过200像素宽度则会自动换行。在动画过程中左击可终止动画，结束后左击可
    kill这个聊天框。
    """

    def __init__(self, text, pos, start):
        self.start = start
        self.width = 200
        self.lines = []
        self.stage = 0
        self.tick = 0
        self.show_time = 10
        self.dead = False
        self.click_cycle = Cycle(2, 8)
        while text:
            self.lines.append(text[0])
            text = text[1:]
            flag = True
            while flag and text:
                if chat_font.size(self.lines[-1] + text[0])[0] > self.width:
                    flag = False
                else:
                    self.lines[-1] += text[0]
                    text = text[1:]
        for i in range(len(self.lines)):
            self.lines[i] = chat_font.render(self.lines[i], True, (255, 255, 255))
        self.height = len(self.lines * chat_font_size) + 10
        self.pos = (pos[0], pos[1] - self.height)
        self.rect = pygame.Rect((self.pos[0] - 5, self.pos[1] - 3),
                                (self.width + 10, self.height))

    # 根据当前状态绘制聊天框，在进入最后阶段一段时间后会显示鼠标点击的提示
    def draw(self):
        if self.stage == 0:
            if self.tick < self.show_time:
                dif1 = ((self.pos[0] + self.width / 2 - 15 - self.start[0]) / self.show_time * self.tick,
                        (self.pos[1] + self.height - 3 - self.start[1]) / self.show_time * self.tick)
                dif2 = ((self.pos[0] + self.width / 2 + 15 - self.start[0]) / self.show_time * self.tick,
                        (self.pos[1] + self.height - 3 - self.start[1]) / self.show_time * self.tick)
                pygame.draw.line(screen, (255, 255, 255), self.start,
                                 (self.start[0] + dif1[0], self.start[1] + dif1[1]), 2)
                pygame.draw.line(screen, (255, 255, 255), self.start,
                                 (self.start[0] + dif2[0], self.start[1] + dif2[1]), 2)
            else:
                pygame.draw.line(screen, (255, 255, 255), self.start,
                                 (self.pos[0] + self.width / 2 - 15, self.pos[1] + self.height - 3), 2)
                pygame.draw.line(screen, (255, 255, 255), self.start,
                                 (self.pos[0] + self.width / 2 + 15, self.pos[1] + self.height - 3), 2)
            self.tick += 1
            if self.tick > self.show_time + 5:
                self.stage += 1
                self.tick = 0
        elif self.stage == 1:
            for i in range(len(self.lines)):
                screen.blit(self.lines[i], (self.pos[0], self.pos[1] + i * chat_font_size))
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
            pygame.draw.line(screen, (255, 255, 255), self.start,
                             (self.pos[0] + self.width / 2 - 15, self.pos[1] + self.height - 3), 2)
            pygame.draw.line(screen, (255, 255, 255), self.start,
                             (self.pos[0] + self.width / 2 + 15, self.pos[1] + self.height - 3), 2)
            if self.tick < 60:
                self.tick += 1
            else:
                screen.blit(texture_lib["mouse_click"], (self.pos[0] + self.width - 10, self.pos[1] + self.height - 15),
                            pygame.Rect(0, 25 * self.click_cycle.get(), 25, 25))


class TalkScene:
    """
    一个对话场景，左边的材质是character1，右边的材质是character2，chats的
    格式为[(角色-int，"发言"), (角色-int，"发言")]
    """
    def __init__(self, character1, character2, chats):
        self.name = "chat"
        self.c1 = "close_" + character1
        self.c2 = "close_" + character2
        self.stage = 0
        self.stage_tick = 0
        self.stage_duration = [50, 0, 25]
        self.chats = []
        for piece in chats:
            self.chats.append(piece)
        self.chats.pop(0)
        self.current_chat = None
        if chats[0][0] == 1:
            self.current_chat = ChatBox(chats[0][1], (130, 200), (180, 240))
        elif chats[0][0] == 2:
            self.current_chat = ChatBox(chats[0][1], (270, 200), (420, 240))

    # 判断当前场景是否结束
    def is_ended(self):
        return self.stage == 3

    # 获取下一个对话框，将其置入当前显示栏里
    def next_chat(self):
        chat = self.chats.pop(0)
        if chat[0] == 1:
            self.current_chat = ChatBox(chat[1], (130, 200), (180, 240))
        elif chat[0] == 2:
            self.current_chat = ChatBox(chat[1], (270, 200), (420, 240))

    # 处理鼠标点击事件，左击可快速跳过对话
    def handle_event(self, event):
        if self.current_chat:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.current_chat.stage == 1:
                    self.current_chat.dead = True
                    ses[7].play_once()
                elif self.current_chat.stage == 0:
                    self.current_chat.stage = 1
                    self.current_chat.tick = 0

    # 更新事件，主要负责动画，以及显示阶段，若当前对话框被kill则显示下一个
    def update(self):
        if self.stage == 1:
            if not self.chats and (not self.current_chat or self.current_chat.dead):
                self.stage_tick = 0
                self.stage += 1
            elif self.current_chat.dead:
                self.next_chat()
        else:
            self.stage_tick += 1
            if self.stage_tick > self.stage_duration[self.stage]:
                self.stage_tick = 0
                self.stage += 1

    # 绘制场景，根据当前显示阶段绘制两个角色，一个当前显示对话框
    def draw(self):
        if self.stage == 0:
            if self.stage_tick < 25:
                screen.blit(texture_lib[self.c1], (self.stage_tick * 12 - 300, 250))
            else:
                screen.blit(texture_lib[self.c1], (0, 250))
                screen.blit(texture_lib[self.c2], (600 - (self.stage_tick - 25) * 12, 250))

        elif self.stage == 1:
            self.current_chat.draw()
            screen.blit(texture_lib[self.c1], (0, 250))
            screen.blit(texture_lib[self.c2], (300, 250))
        elif self.stage == 2:
            screen.blit(texture_lib[self.c1], (-self.stage_tick * 13, 250))
            screen.blit(texture_lib[self.c2], (300 + self.stage_tick * 13, 250))
        else:
            screen.blit(texture_lib[self.c1], (0, 250))
            screen.blit(texture_lib[self.c2], (300, 250))


class TextScene:
    """
    纯文本场景，用于显示游戏胜利以及游戏失败
    """
    def __init__(self, texture):
        self.name = "text"
        self.tick = 0
        self.texture = texture

    # 判断当前场景是否结束
    def is_ended(self):
        return self.tick >= 150

    # 背景以及文字分别从左到右进场，然后依次退场
    def draw(self):
        if self.tick < 20:
            screen.blit(texture_lib["result_background"], (30 * self.tick - 600, 0))
        elif self.tick > 130:
            screen.blit(texture_lib["result_background"], (30 * (self.tick - 130), 0))
        else:
            screen.blit(texture_lib["result_background"], (0, 0))
            if self.tick < 50:
                screen.blit(texture_lib[self.texture], ((self.tick - 20) * 20 - 600, 0))
            elif self.tick < 100:
                screen.blit(texture_lib[self.texture], (0, 0))
            elif self.tick < 130:
                screen.blit(texture_lib[self.texture], ((self.tick - 100) * 20, 0))

    # 负责动画更新
    def update(self):
        self.tick += 1

    # 循环需要，可使用抽象类代替，但是由于子类太少便有些多余
    def handle_event(self, event):
        pass


class LevelNum:
    """
    当前关卡场景，用于显示开始关卡之前的关卡数量显示
    """
    def __init__(self, num):
        self.name = "level"
        self.tick = 0
        self.num = num
        self.texture = level_font.render("关卡" + str(num), False, (0, 0, 0))

    # 判断场景是否结束
    def is_ended(self):
        return self.tick >= 150

    # 绘制，与纯文本的方法一样
    def draw(self):
        if self.tick < 20:
            screen.blit(texture_lib["result_background"], (30 * self.tick - 600, 0))
        elif self.tick > 130:
            screen.blit(texture_lib["result_background"], (30 * (self.tick - 130), 0))
        else:
            screen.blit(texture_lib["result_background"], (0, 0))
            if self.tick < 50:
                screen.blit(self.texture, ((self.tick - 20) * 20 - 600 + 250, 165))
            elif self.tick < 100:
                screen.blit(self.texture, (0 + 250, 165))
            elif self.tick < 130:
                screen.blit(self.texture, ((self.tick - 100) * 20 + 250, 165))

    # 更新动画帧
    def update(self):
        self.tick += 1

    # 循环需要
    def handle_event(self, event):
        pass

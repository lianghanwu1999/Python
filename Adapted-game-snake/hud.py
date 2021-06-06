from config import *


class InfoBar:
    """
    HUD，Head up display用于显示当前血量，经验值，经验等级
    """
    def __init__(self, snake):
        self.snake = snake
        self.hp_lag = 300

        self.level_text = None
        self.update()

    # 根据蛇来更新当前HUD数值
    def update(self):
        self.level_text = chat_font.render("Lv." + str(self.snake.level), False, (255, 255, 255))
        if self.hp_lag > self.snake.hp*3:
            self.hp_lag -= 2
        else:
            self.hp_lag = self.snake.hp*3

    # 将当前数值绘制出来
    def draw(self):
        screen.blit(self.level_text, (30, 15))
        screen.blit(texture_lib["exp_bar"], (6, 50), pygame.Rect(0, 10, self.snake.current_exp, 10))
        screen.blit(texture_lib["exp_bar"], (6, 50), pygame.Rect(0, 0, 100, 10))
        screen.fill(-1, pygame.Rect(150, 370, self.hp_lag, 20))
        screen.blit(texture_lib["hp_bar"], (150, 370),
                    pygame.Rect(300 - self.snake.hp * 3, 20, self.snake.hp * 3, 20))
        screen.blit(texture_lib["hp_bar"], (150, 370), pygame.Rect(0, 0, 300, 20))

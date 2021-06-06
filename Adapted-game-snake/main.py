from game import *
from scene import *
import sys

# 读取当前存档，如果没有的话则开始新的游戏
if os.path.exists("save"):
    f = open("save", "r")
    c_level = int(f.read())
    f.close()
    g = Game(c_level)
else:
    g = Game()


# 主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        # 关闭事件，在关闭的时候存下当前关卡
        if event.type == pygame.QUIT:
            f = open("save", "w")
            f.write(str(g.current_level))
            f.close()
            pygame.quit()
            sys.exit()
        # 鼠标事件，更新环境变量
        if event.type == pygame.MOUSEMOTION:
            env["mouse_x"] = pygame.mouse.get_pos()[0]
            env["mouse_y"] = pygame.mouse.get_pos()[1]
            env["mouse_direction"] = atan2(env["mouse_y"] - screen_height/2, env["mouse_x"] - screen_width/2)
        # 让游戏处理事件
        g.handle_event(event)
    # 游戏更新
    g.update()

    # 清空屏幕，然后绘制一个新的屏幕
    screen.fill(0)
    g.draw()
    # 因为基本上每次都需要更新整个屏幕，直接使用flip来刷新整个屏幕
    pygame.display.flip()

    # 将帧速率限制到40fps
    clock.tick(40)

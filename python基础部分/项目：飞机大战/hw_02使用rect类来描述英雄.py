#导入pygame模块
import pygame
#rect 函数描绘英雄的数据信息
hero_rect = pygame.Rect(100,500,120,125)

print("英雄的原点 %d %d " %(hero_rect.x , hero_rect.y))
print("英雄的尺寸 %d %d " %(hero_rect.width , hero_rect.height))
print("%d %d" %hero_rect.size)

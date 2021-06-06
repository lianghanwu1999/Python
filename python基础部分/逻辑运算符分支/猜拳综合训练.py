#平行顺应判断时，用 if....elif....else
#导入随机工具包 :import 工具包名
#注意：把工具包放在文件的顶部，下面随时可以引用这个工具包。
import random
#从控制台输入出拳 ---石头 （1）/ 剪刀 （2）/ 布 (3)
player = int(input("请您输入你要出的拳 : " ))
#电脑随机出拳，先假设电脑只能出石头 ，完成整体代码
computer = random.randint(1,3)
print("玩家出的拳头 %d  -> 电脑要出的拳是 : %d 石头 （1）/ 剪刀 （2）/ 布 (3) " %(player,computer))

#比较胜负
#1 石头 胜 布
#2 剪刀 胜 布
#3 布   胜 石头
#if的格式也可以这样if (( )
#                     or(  )
#                     or(  ));
#玩家胜
if (( player==1 and computer==3)
        or(player==2 and computer == 3 )
        or (player ==3 and computer ==1)):
    print("我赢了")
#平局
elif(player == computer):
    print("平局，我们再来一盘")
#电脑获胜
else:
    print("我输了，下次我可不会掉以轻心了")
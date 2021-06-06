#TODO  水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
# 它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$
# 找出所有水仙花数
"""
for num in range(100,1000):
    low = num%10
    mid = num // 10%10      # // 代表整数除法
    high = num // 100
    if num ==low **3 +mid **3 +high **3:
        print(num)
"""
"""
#TODO 正整数反转
num = int(input('num = '))
reversed_num = 0
while num >0:
    reversed_num = reversed_num *10 +num %10
    num //=10
print(reversed_num)
"""
"""
#TODO 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

for x in range(0,20):  #x 的取值范围
    for y in  range(0,33):
        z = 100 -x - y
        if 5*x + 3*y +z/3 == 100:
            print('公鸡：%d只，母鸡：%d只，小鸡：%d只' %(x,y,z))

"""
"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

"""
from random import randint

money = 1000
while money > 0:
    print('您的总资产为：',money)
    needs_go_on = False
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:   #下注的钱大于你的资产，会跳出循环。
            break
    first = randint(1,6) + randint(1,6)   #两颗色子所摇到的点数
    print('玩家摇出了%d点' %first)
    if first == 7 or first == 11:
        print('玩家胜！')
        money +=debt      #debt 下注金额
    elif first == 2 or first == 3 or first ==12:
        print('庄家胜！')
        money -=debt
    else:
        needs_go_on = True     #继续执行。
    while needs_go_on:
        needs_go_on = False
        current = randint(1,6)+randint(1,6)
        print('玩家摇出了%d点'%current)
        print('玩家摇出了%d点' %current)
        if current == 7:
            print('庄家胜！')
            money -=debt
        elif current == first:
            print('玩家胜！')
            money += debt
        else:
            needs_go_on =True

print('你破产了，游戏结束')


#break语句在循环语句中的练习
# 先设置一个计数器 i
i = 0
# 循环语句while,打印1到10的数,不执行4的数字
while i <= 10:
    #不执行4这个数字，即是如果到4时，满足条件执行if语句，continue跳过。
    if i==4:
        #跳过4数字
        #为了不会一直进行死循环，所以在continue语句前增加一个处理计数器
        i+=1
        continue
    print(i)
    i+=1




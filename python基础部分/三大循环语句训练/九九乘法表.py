#函数封装：def 定义一个函数名():
def chengfabiao():
#定义列的变量计数器lie


    lie = 1
    while lie <= 9:
        #定义行的计数器 hang
        hang = 1
        while  hang <= lie:
            print("%d * %d  = %d" %(hang,lie ,hang * lie ),end="\t")  #把星星替换成九九乘法表，1先改成9*9=81 ，
                                    # 2.把行的9替换成行数，列的9替换成列数，总数为行*列
                                    #调整九九乘法表的格式，利用制表符 \t
            hang +=1
        print(" ")
        lie +=1
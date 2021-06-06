#练习大文件的复制动作

#打开
#创建文件的复件名
file_read = open("README")
file_write = open("README[大复件]", "w")  # w 只写文件
#2.读，写
while True:
    #只读取一行
    text = file_read.readline() #将源文件的内容读取出来

    #判断是否读取到内容
    if not text:
        break
    file_write.write(text)  #复件将写入原文件的内容
#3.关闭
file_read.close()
file_write.close()
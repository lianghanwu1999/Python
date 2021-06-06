#练习小文件的复制动作

#打开
#创建文件的复件名
file_read = open("README")
file_write = open("README[复件]", "w")
#2.读，写
text = file_read.read() #将源文件的内容读取出来
file_write.write(text)  #复件将写入原文件的内容
#3.关闭
file_read.close()
file_write.close()
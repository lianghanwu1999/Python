#1.打开文件（输入文件名是区分大小写的）
file = open("README")  #open 后输入文件名

#2.读取文件  #读取文件中文会有 编码问题，要设置编码格式为 gdk 
text = file.read()
print(text)
#3.关闭文件
file.close()
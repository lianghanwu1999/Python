#1.打开文件（输入文件名是区分大小写的）
file = open("README")  #open 后输入文件名

#2.读取文件  #读取文件中文会有 编码问题，要设置编码格式为 gdk
text = file.read()
print(text)
print(len(text))

print("-" * 50)
#调用了read（）方法后，指针会到文件末尾，
#测试再次调用指针是否会继续回到开头执行内容
text = file.read()
print(text)
print(len(text))
#结论：显而易见并不会回到开头

#3.关闭文件
file.close()
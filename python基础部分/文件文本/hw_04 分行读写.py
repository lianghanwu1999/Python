file = open("README")
while True:
    #readline(）函数每次只读一行内容
    text = file.readline()
    #判断是否读取到内容
    if not text:
        break
    print(text)
    print(text,end="")

file.close()
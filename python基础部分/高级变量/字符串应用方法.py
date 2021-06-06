#1.判断空白字符，用.isspace方法，若是输入空白字符，都输出为True,否则输出为false
space_str = "  \t\n\r"

print(space_str.isspace())
#总结：空格和 \t \n \r 在python都定义为空白字符

#1> 共同点都不能判断小数，num_str = "1.1"
num_str = " 一千零一"

print(num_str)
#如果字符串全为数字，则返回一个True
print(num_str.isdecimal())
#如果字符串输出的为数字，（1），次方数，则返回为 True
print(num_str.isdigit())
#如果字符串输出的为数字，汉字，次方，则返回为True
print(num_str.isnumeric())


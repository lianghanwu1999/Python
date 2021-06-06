#eval() 函数十分强大 --将字符串当成 有效的表达式来求值 计算结果
#TODO eval() 函数的作用：eval函数就是实现list、dict、tuple与str之间的转化
#TODO eval()函数的应用
#基本的数学计算器（可以进行加减乘除计算）
input_str = input("请输入一个算数题：")
print(eval(input_str))

#字符串重复
eval("'*'" * 10)


#将字符串转换成列表
type(eval("[1,2,3,4,5]"))


#将字符串转换成字典
type(eval("{'name' :'xiaoming' ,'age' : '18'}"))


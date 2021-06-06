#创建一个列表name_list 来储存名字信息
name_list = ["zhangsan","lisi","wangwu"]
#取值和索引
print (name_list[0])  #取值
#取索引

#知道数据内容，想要数据在列表的位置
#使用index（index 是用于取索引）方法需要注意，如果传递数据不在列表中，程序会报错
print(name_list.index("zhangsan"))
#修改利用索引位置修改相应数字
name_list[1] = "李四"

#增加数据使用append方法可以向列表的末尾追加数据
name_list.append("王小二")

#index方法可以在列表的指定索引位置插入数据.insert(索引位置,"插入内容")
name_list.insert(1,"小明")
#插入列表内容.extend(),插入一个新列表的内容 xin.list
xin_list = ["孙悟空","猪八戒","沙和尚"]
name_list.extend(xin_list)
#删除
name_list.remove("wangwu")
#pop方法默认可以把列表中最后一个元素删除
name_list.pop()
#pop方法可以指定要删除元素的索引
name_list.pop(3)
#clear 方法可以清空列表所有
name_list.clear()
#del关键词可以删除列表元素指定索引元素
#del name_list [0]
#del 关键词本质上是用于将一个变量从内存中删除，后续代码就不能使用这个变量了
#统计
#统计长度 len(相当于length 长度)函数可以统计列表中元素的总数
list_len = len(name_list)
print("列表中包含%d 个元素" %list_len)
#统计次数 count 方法可以统计列表中某一个数据出现的次数
count = name_list.count("张三")
print("张三出现了%d 次" %count)
#.remove 方法 从列表中删除第一次出现的数据，如果数据不存在，程序会报错
name_list.remove("zhangsan")
#排序
name_list1 = ["zhangsan","lisi","wangwu","zhaoliu"]
num_list = [1,2,3,4,6,8,9]
#升序.sort 方法：从小到大，升序排列
num_list.sort()
name_list1.sort()
#降序：从大到小排列，降序排列
name_list1.sort(reverse=True)
#逆序:在原有顺序反过来
name_list1.reverse()

print(num_list)
print(name_list1)

print(name_list)



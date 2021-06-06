#使用多个键值对，存储描述的相关信息描述更复杂的信息
#将多个字典放在一个列表中，进行遍历
#定义一个列表存储字典
card_list = [
    {"name": "张三",
     "qq": "12345",
     "phone" : "110"
},
{"name": "李四",
     "qq": "54321",
     "phone" : "10086"
}
]
for card_info in card_list:
    print(card_info)
#for迭代遍历的用处是每一个元素都访问一次，并输出结果

xiaoming_dict = {"name":"小明",
                 "height":1.75}
#取值：在字典中取值，要指定key键，而不是索引
#在取值的时候，如果指定的key不存在，程序会报错
#print(xiaoming_dict["name"])

#增加/修改
#如果key不存在，会新增键值对
xiaoming_dict["age"]  = 18
#如果key存在，会修改已经存在的键值对，有键时，会修改键的值
xiaoming_dict["name"] = "小小明"

print(xiaoming_dict)

#删除:删除了键，值同时也会被删除。
xiaoming_dict.pop("name")
#在删除指定键值对的时候，如果指定的key不存在，程序会报错

print(xiaoming_dict)
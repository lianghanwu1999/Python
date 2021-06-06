#TODO 常用数据结构
# 1.重要知识点

#TODO 生成式（推导式）的用法
# 说明：生成式（推导式）可以用来生成列表、集合和字典。
prices = {
    'AAPL' : 191.88,
    'GOOG' : 1186.96,
    'IBM':149.24,
    'ORCL':48.44,
    'ACN':166.89,
    'FB':208.09,
    'SYMC' :21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 ={key:value for key,value in prices.items() if value > 100} # items()返回生成字典元组或者数组
print(prices2)

"""
TODO ：heapq模块（堆排序
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1))  #从大到小 ：nlargest(要取个数，所在列表)
print(heapq.nsmallest(3, list1)) #从小到大 ：nsmallest(要取个数，所在列表)
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

#TODO itertools模块
"""
迭代工具模块
"""
import itertools

#产生ABCD的全排列
itertools.permutations('ABCD')
#产生ABCDE的五选三组合
itertools.permutations('ABCDE',3)
#产生ABCD和123的笛卡尔积
itertools.product('ABCD','123')
#产生ABC的无限循环序列
itertools.cycle(('A','B','C'))


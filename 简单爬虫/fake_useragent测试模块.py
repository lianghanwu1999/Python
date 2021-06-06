#TODO 使用fake_useragent 库方法：
#1.安装 fake_useragent库：
   # （1） 在cmd 中 输入 pip install fake-useragent
   #（2） 在pycharm中安装 ：
#   file -> 选择 Settings... -> project:训练项目 -> project interperter 选择加号 输入 fake-useragent 的库 安装
from fake_useragent import UserAgent
ua = UserAgent()
print(ua.chrome)

"""
from fake_useragent import UserAgent
ua = UserAgent()
#ie浏览器的user agent
print(ua.ie)

#opera浏览器
print(ua.opera)

#chrome浏览器
print(ua.chrome)

#firefox浏览器
print(ua.firefox)

#safri浏览器
print(ua.safari)

#最常用的方式
#写爬虫最实用的是可以随意变换headers，一定要有随机性。支持随机生成请求头
print(ua.random)
print(ua.random)
print(ua.random)

"""
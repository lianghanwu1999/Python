#发送对象调用urlopen模块
from urllib.request import urlopen

#创建一个目标对象
url = "http://www.baidu.com"
#发送请求
response = urlopen(url)
#读取内容
info1 = response.read()
#打印内容:直接打印会出现乱码错误，使用.decode() 方法，默认使用utf -8 格式
print(info1.decode())



#补充方法
#返回HTTP的相应，成功返回200，返回400 服务器页面错误，返回5 服务器问题 卡慢
#打印状态码
print(response.getcode())
#打印真实url
print(response.geturl())
#打印响应头
print(response.info())
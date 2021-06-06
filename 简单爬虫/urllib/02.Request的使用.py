#调用发送请求模块
from urllib.request import urlopen
from urllib.request import Request

from random import choice

url = "http://www.baidu.com"

#如何动态变化用户代理：User-agents
user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"]
#调用随机模块
print(choice(user_agents))

#TODO (由于反爬虫会根据用户代理user-agents，检测你是否为机器人爬虫还是浏览器，
# 这时我们可以根据修改用户代理来伪装成浏览器从而骗过服务器)
#伪装请求头，改为 Chrome浏览器骗过服务器
headers = {
    "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
request = Request(url,headers=headers)

#查看请求头 的信息，注意第二个agent 要小写。
print(request.get_header("User-agent"))

# #发送请求
response = urlopen(request)
#读取内容
info = response.read()
#打印内容
print(info.decode())
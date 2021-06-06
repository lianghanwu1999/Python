from urllib.request import ProxyHandler,build_opener
from fake_useragent import UserAgent
from urllib.request import urlopen,Request

url = "https : http://www.baidu.com/"  #https:需要代理的网站\
headers = {
    "User-Agent" :UserAgent().chrome
}
request = Request(url,headers= headers)
#TODO 设置代理服务器(构建代理)（选择其中一种模式）
# heandler = ProxyHandler({"http": "username : password@ ip: port})  #模板
# heandler = ProxyHandler({"http": "用户名" : "密码" "@ ip地址": "端口"})  #模板
# heandler = ProxyHandler({"http": "118.190.95.43": "16818"})
# heandler = ProxyHandler({"http": "ip地址": "端口"})  #模板

heandler = ProxyHandler({"http":"51.158.186.242:8811"})

#TODO 自定义代理
opener = build_opener(heandler)
response = opener.open(request)
print(response.read().decode())

"""
代理访问:ProxyHandler()：

#步骤：使用ProxyHandler构建一个handler（代理）

handler=request.ProxyHandler({http:'proxyip'})

#使用构建好的handler 构建一个opener

opener=request.build_opener(handler)

#使用opener发送一个请求

response =opener.open(url)

"""
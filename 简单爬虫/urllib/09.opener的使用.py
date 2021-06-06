from urllib.request import Request
from urllib.request import build_opener
from fake_useragent import UserAgent

url = "http:// www.baidu.com"
headers = {
    "User-Agent" : UserAgent().chrome
}
request = Request(url,headers=headers)
handler = HTTPHandler()
opener = build_opener(handler)
response = opener.open(request)
print(request.read().dcode())


"""
代理访问:ProxyHandler()：

步骤：使用ProxyHandler构建一个handler

handler=request.ProxyHandler({http:'proxyip'})

使用构建好的handler 构建一个opener

opener=request.build_opener(handler)

使用opener发送一个请求(代理)

response=opener.open(url)   # 不需要进行代理情况下 response = urlencode(url) 

"""

from urllib.request import Request,urlopen
from fake_useragent import UserAgent

"""
cookie设置方法1：
小结：通过在请求中增加cookie 来为下次登录不用再登录账号密码。

"""

url = "https://www.wenjuan.com/"  #TODO 已经登录上了网站网址
#TODO 设置cookie 方法一，在header里面设置cookie。     #设置cookie 就是为了下次登录不用账号密码
headers = {
    "User-Agent" : UserAgent().chrome,
    "Cookie" :"grwng_uid=181780bd-f643-48e6-8f5f-c08344ac6dc3"
}
#构造请求
request = Request(url,headers= headers)
#接收请求
response = urlopen(request)
#读取请求
print(response.read().decode())

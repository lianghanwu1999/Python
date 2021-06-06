from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor,build_opener

"""
设置cookie 方法2.：
步骤：1.找出登录前的网页的url，输入错误账号密码，找到账号密码对应的参数名。
      2.增加一个参数来储存，设置刚才找到的账面密码参数
      3.调用#HTTPCookieProcessor()默认创建一个cookie位置来储存cookie
      4.创建登录后的url ，在进行请求访问。


"""

#登录
login_url = "https://www.wenjuan.com/jslogin/" #TODO 登录前有显示登录密码的网站。

headers = {
    "User-Agent" : UserAgent().chrome,
}
form_data = {
    "emailorusername": "18344416835",    #可以通过输入密码错误，来检测出账号密码的参数名
     "password" : "lhw13192604270hw"
}
f_data = urlencode(form_data).encode()
#构造请求
request = Request(login_url,headers= headers,data=f_data)
#接收请求
#桥接一个代理(存储cookie)
handler = HTTPCookieProcessor() #HTTPCookieProcessor()默认创建一个cookie位置来储存cookie
opener = build_opener(handler)
#避免显示太多暂不打印
# response =opener.open(request)
# print(response.read().decode())

#访问页面
info_url = "https://www.wenjuan.com/" #TODO 已经登录了的页面，在f12 中找。
request = Request(info_url,headers=headers)
response = opener.open(request)
print(response.read().decode())

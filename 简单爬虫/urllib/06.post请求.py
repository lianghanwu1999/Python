from urllib.request import Request,urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

url = "http://www.sxt.cn/index/login/login.html"
#TODO post请求特有部分，post请求需要转换成data的数据格式
form_data = {
    "usre" : "17703181473",
    "password" :"123456"
}
#伪装请求头
headers = {
    "User-Agent" :UserAgent().chrome
}
#post请求所要的是data类型，所以需要进行转换。
f_data = urlencode(form_data)
#处理请求头
request = Request(url,data=f_data.encode(),headers=headers)    #data = f_data.encode()，为什么要加encode(),将转成beyts(字节)将中文或其他转为字符串。
#发送请求
response = urlencode(request)
#读取请求
print(response.read().decode())

#请求模块(Request),接受请求(urlopen)
from urllib.request import Request,urlopen
#解析模块 urlencode
from urllib.parse import urlencode

#get请求转译方法2：(适合多个对象)

args = {
    "wd" : "尚学堂",
    "ie": "utf-8"
}
url = "https://www.baidu.com/s?{}".format(urlencode(args))   #get请求方法，动态调用。
print(url)
headers = {
"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
request = Request(url,headers=headers)
response = urlopen(request)
info = response.read()
print(info.decode())
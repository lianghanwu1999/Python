from urllib.request import Request,urlopen
from urllib.parse import quote

#get请求转译方法1：
url = "https://www.baidu.com/s?wd={}".format(quote("尚学堂"))    #后接format(quote("自定义内容))这步进行了get的请求中的quote方法转码


#定义用户代理
headers = {
"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
request =Request(url,headers=headers)

#发送请求
response = urlopen(request)
#读取内容
info =response.read()

#打印内容
print(info.decode())




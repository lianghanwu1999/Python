from fake_useragent import UserAgent
import requests

#TODO requests 方法之添加代理
url = "http://www.baidu.com"
headers = {
    "User-Agent" :UserAgent().chrome

}
proxies = {
    "http":"http://51.158.186.242:8811"  #添加代理（会过期）
}
response = requests.get(url ,headers= headers,proxies=proxies)
print(response.text)
#你向ajax后台的程序发送xmlhttp请求的时候,
# 后台程序接到请求会进行处理,处理结束后,可以返回一串数据给前台,这个就是responseText.

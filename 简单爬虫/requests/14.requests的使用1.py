import requests
from fake_useragent import UserAgent

#TODO requests 方法之get请求

headers = {
    "User-Agent" : UserAgent().chrome
}
url = "https://www.baidu.com/s?"
params = {
    "wd" : "尚学堂"
}
response = requests.get(url,headers= headers,params=params)  #get请求
print(response.text)
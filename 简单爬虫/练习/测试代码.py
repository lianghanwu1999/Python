import urllib.parse
import urllib.request
from fake_useragent import UserAgent

#测试获取头部信息
url = "http://www.baidu.com"
headers = {
    "User-Agent" : UserAgent().chrome
}
request =urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
#print(request)
print(response.read().decode())

print(response.getcode())  #getcode()获取当前的网页的状态码，
                            # 200状态码表示网页正常，403表示不正常。
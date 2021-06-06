from fake_useragent import UserAgent
import requests

#TODO request请求之ssl验证

url = "https://www.12306.cn/index/"
headers = {
    "User-Agent" :UserAgent().chrome
}
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings()
#在request 中添加ssl验证：将verify = False。
response = requests.get(url ,headers= headers,verify = False)
#将响应的请求默认设置为utf-8 格式。
response.encoding = "utf-8"
print(response.text)

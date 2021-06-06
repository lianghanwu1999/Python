import requests
from fake_useragent import UserAgent
import re

url = "https://www.runoob.com/html/html-tutorial.html"
headers = {
    "User-Agent" : UserAgent().chrome
}
response = requests.get(url,headers= headers)   #用request库用get/post方法请求头
info = response.text
print(info)
infos = re.findall(r'',info)
print(infos)
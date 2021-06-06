import requests
from fake_useragent import UserAgent

#TODO requests方法之post请求
headers = {
    "User-Agent" : UserAgent().chrome
}
login_url = "https://www.wenjuan.com/jslogin/"
params = {
    "emailorusername": "18344416835",    #可以通过输入密码错误，来检测出账号密码的参数名
     "password" : "lhw13192604270hw"
}
response = requests.post(login_url,headers= headers,data=params)  #post 请求
print(response.text)
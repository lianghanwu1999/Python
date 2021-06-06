from fake_useragent import UserAgent
import requests

session = requests.Session()
headers = {
    "User-Agent" : UserAgent().chrome
}
login_url = "https://www.wenjuan.com/jslogin/"
params = {
     "emailorusername": "18344416835",    #可以通过输入密码错误，来检测出账号密码的参数名
    "password" : "lhw13192604270hw"
}
response = session.post(login_url,headers= headers,data=params)  #多值传递用post请求。
info_url = "https://www.wenjuan.com/"
response = session.get(info_url,headers=headers )                           #单值传递用get请求
print(response.text)


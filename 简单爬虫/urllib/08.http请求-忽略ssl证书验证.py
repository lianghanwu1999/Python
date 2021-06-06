from urllib.request import Request,urlopen
from fake_useragent import UserAgent
import ssl

url = "https://www.12306.cn/index/ "
headers = {
    "User-Agent" :UserAgent().chrome
}
request = Request(url,headers=headers)
#忽略验证证书:网络有要验证安全的证书，一般要允许才可以登录操作。我们想不验证时，选择跳过。
centext =ssl._create_unverifed_context()  #跳过证书验证。
#接受请求
response = urlopen(request,centext = centext)

info = response.read().decode()

print(info)
from urllib.request import Request,build_opener,HTTPCookieProcessor
from fake_useragent import UserAgent
#储存cookie
from http.cookiejar import MozillaCookieJar
from urllib.parse import urlencode

#登录
def get_cookie():
    #定义登录前的url
    login_url  = "https://www.wenjuan.com/jslogin/"
    headers = {

        "User-Agent" : UserAgent().chrome
    }
    #设置用户账号密码
    form_data = {
        "emailorusername": "18344416835",  # 可以通过输入密码错误，来检测出账号密码的参数名
        "password": "lhw13192604270hw"
    }
    #将账号密码转译为字节bytes 。
    f_data = urlencode(form_data).encode()
    #构造请求（将要想服务器请求的点，放在一起提交给服务器）
    request = Request(login_url,headers= headers,data=f_data)
    #TODO (疑问点)
    cookie_jar = MozillaCookieJar()
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    #发送请求 将构造请求的点，和要构造的点，打包发给服务器。
    response = opener.open(request)
    #保存cookie文件于文件目录里，为后续使用。
    cookie_jar.save("cookie.txt",ignore_expires=True,ignore_discard=True)
    """
    gnore_discard的意思是即使cookies将被丢弃也将它保存下来(遗弃不用也会保留)
    ignore_expires的意思是如果cookies已经过期也将它保存并且文件已存在时将覆盖（过期也会保存）
    
    """

#使用cookie
def use_cookie():
    #定义登录后的url：
    info_url = "https://www.wenjuan.com/"
    headers = {

        "User-Agent": UserAgent().chrome
    }
    #构造请求
    request = Request(info_url, headers=headers)
    cookie_jar = MozillaCookieJar()
    #加载文件
    cookie_jar.save("cookie.txt", ignore_expires=True, ignore_discard=True)
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    print(response.read().decode())

#从登录中获取cookie文件的获取一次就可以了
# 保存在文件夹中为后续调用。
#get_cookie()



#访问页面
if __name__ == '__main__':
    #把刚才获取的cookie文件用了使用
    use_cookie()
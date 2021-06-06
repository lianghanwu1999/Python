#TODO urllib 基础梳理

"""
urllib.request:
    urlopen : 打开url
    urlretrieve(url,file_name):打开并保存url内容

urllib.parse:
    quote(): url编码函数，将中文进行转化为%xxx(其他字符串形式或其他形式)
     unquote():url解码函数，将%xxx转化为指定字符
     urlencode(): 非法字符转码

response():
    read() :读取字节类型
    geturl() 获取请求url
    getheaders()
    getcode()
    readlines()

"""
"""
字符串 -> 二进制 ：encode()
二进制 -> 字符串 ：decode()
都：默认utf-8 类型
"""

import urllib.request
url = "http:// www.baidu.com/"
response = urllib.request.urlopen(url=url) #接收，响应 并打开url



"""
print(response)
print(response.geturl())   #//geturl()获取当前的网页的网址。
print(response.getheaders()) #//获取多个同名请求头对应的一组value值
print(response.getcode())   #//getcode()获取当前的网页的状态码，
                            # 200状态码表示网页正常，403表示不正常。

"""
# TODO print(resonse.read().decode())  #读取url内容

with open('baidu.html','w' ,encoding = 'utf8') as  file:
    file.write(response.read().decode())

"""
等同于上方
只不过上述用utf-8写入
在此用二进制写入 写入（有已有文件写入，没有文件创建文件在写入。）
图片用这个！
with open('baidu_1.httml','wb') as file:
    file.withe(response.read())    
    """
#TODO w 是写入模式
# r是读取模式
# wb 是二进制写入
# with open('a.jpg'.'wb')as f: 后面跟一段f.write()

#urlretrieve(url,file_name)
picture  = "https://timgsa.baidu.com/timg?image&quality=80&" \
         "size=b9999_10000&sec=1551421909555&di=9f9d69abb9fe596f493f9c6e3e52f08e&imgtype=0&" \
         "src=http%3A%2F%2Fgss0.baidu.com%2F9vo3dSag _xI4khGko9WTAnF6hhy%2Fzhidao%2Fpic%2Fitem%" \
         "2Fb151f8198618367a039b78422c738bd4b31ce51b.jpg"    #插入图片
"""
#创建写入文件的一条龙服务
#urllib.request.urlretrieve(picture,'ironMan.jpg')  // (参数，图片名.jpg)

"""

import urllib.parse

#url中若出现$ 空格 中文 等，就要对其进行编码
url = "http://www.baidu/index.html?name=钢铁侠&pwd=123456"
ret = urllib.parse.quote(url)
re = urllib.parse.unquote(url)
re_1 = urllib.parse.unquote(picture)
print(ret)
print(re)
print(re_1)

"""
urllib.parse.urlencode 的应用！

"""

url = 'http://www.baidu.com/index.html'
#构造 http://www.baidu.com/index.index.html?name=goudan&age=18&sex=nv&heught=180
name = '钢铁侠'
age = 18
sex = 'nv'
height = '180'

#建立字典，将值一一赋值进网页里面
data = {
    'name' : name ,
    'age' : age,
    'sex' : sex,
    'height' : height,
    'weight' : 180,
}
#具有非法字符串的自动转换功能
construct_url = urllib.parse.urlencode(data)  #将data 字典进行非法字符转换。
print(construct_url)
construct_url = url + '?' +construct_url   #看不懂操作
print(construct_url)


#example:植入搜索关键字
import urllib.parse
baidu = 'http://www.baidu.com/s?'
word = input('input the key you want: ')
_data = {
    'ie' : 'utf-8',
    'wd' : word
}
#非法字符串转换码
query_string = urllib.parse.urlencode(_data)
baidu += query_string   #查询字符串，一般是对http请求所带的数据进行解析
response = urllib.request.urlopen(baidu)
filename = word + '.html '
with open(filename,'wb')as file:
    file.write(response.read())


#伪装UA
#构造请求对象：urllib.request.Request(self,url,data=None,headers = {},....)
url = 'http://www.baidu.com/'
headers = {
    "User-Agent" :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}
#构造请求头
request = urllib.request.Request(url=url ,headers=headers)
#接收响应
response = urllib.request.urlopen(request)
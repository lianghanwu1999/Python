# TODO requests 使用和json 转化文本保存
from time import time
from threading import Thread

import requests

#继承Thread类创建自定义线程类
class DownloadHanlder(Thread): #TODO 首先是DownloadThread类，继承于HandlerThread，用于下载（可以直接调用）

    def __init__(self,url):
        super().__init__()
        self.url =url

    def run(self):
        filename = self.url[self.url.rfind('/')+1]
        resp = requests.get(self.url)
        with open('/User/Hao/'+ filename,'wb')as f:
            f.write(resp.content)

def main():
    #通过requests 模块的get 函数获取网络资源
    #下面的代码中使用了天行数据接口提供的网络API
    #要使用该数据接口需要在天行数据的网络上注册
    #然后用自己的key 替换掉下面代码中APIkey 即可
    resp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
    #将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:  #作者的key，本机没有
        url = mm_dict['picUrl']
        #通过多线程的方式实现图片下载
        DownloadHanlder(url).start()

if __name__ == '__main__':
    main()

from socket import socket,SOCK_STREAM,AF_INET   #创建Socket时，AF_INET指定使用IPv4协议，IPv6，就指定为AF_INET6
from datetime import datetime

def main():
    #1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET,type=SOCK_STREAM) #指定传输服务为ipv4地址，套接字为-TCP套接字
    #2.绑定IP地址和端口（端口用于区分不同的服务）
    #同一个时间在同一个端口上只能绑定一个服务否则报错
    server.bind(('192.168.1.2 ',6789))   #TODO ：[Errno 11001] getaddrinfo failed（报错原因：同一个时间在同一个端口上只能绑定一个服务）
    #3.开启监听-监听客户端连接到服务器
    #参数512 可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动开始监听。。。')
    while True:
        #4.通过循环接收客户端的连接方法并作出相应的处理（提供服务）
        #accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        #accept 方法返回一个元组其中的第一个元素是客户端地址（由ip地址和端口两部分组成）
        client,addr = server.accept()
        print(str(addr)+'连接到服务器。')
        #5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        #6.断开连接
        client.close()

if __name__ == '__main__':
    main()

#TODO 实现TCP客户端的功能，相较于实现服务器程序，实现客户端程序就简单多了
from socket import socket

def main():
    #1.创建套接字对象默认使用ipv4 和TCP 协议
    client = socket
    #2.连接到服务器（需要指定的ip地址和端口）
    client.connect(('127.0.0.1',6789))  #127.0.0.1 是本机地址。
    #3.从服务器接收数据
    print(client.recv(1024).decode('utf-8')) #设置端口范围，和字符编码
    #关闭服务器
    client.close()

if __name__ == '__main__':
    main()

#TODO  使用多线程技术处理多个用户请求的服务器
# 服务器端代码
from socket import socket ,SOCK_STREAM,AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread

def main():

    #自定义线程类
    class FileTransferHandler(Thread):
        def __init__(self,cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict ={}
            my_dict['filename'] ='guido.jpg'
            #jsom 是纯设计文本不能携带二进制数据
            #所以图片是二进制数据要处理成base64编码
            my_dict['filedata'] = data
            #通过dumps 函数将字典处理成Json字符串
            json_str = dumps(my_dict)
            #发送json 字符串
            self.cclient.send(json_str.encode('utf-8'))
            #关闭服务器
            self.cclient.close()
    #创建套接字对象并指定使用哪种传输服务
    server = socket()  #没有设置默认使用ipv4（AF_INET - IPv4地址） 和TCP 协议（SOCK_STREAM - TCP套接字）
    #2.绑定ip地址和端口（区分不同的服务）
    server.bind(('127.0.0.1',5566))
    #3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听。。。')
    with open('guido.jpg','rb') as f :
        #将二进制数据处理成base64 在解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client , addr ,= server.accept()
        #启动一个线程来处理客户端的请求
        FileExistsError(client).start()



if __name__ == '__main__':
    main()

from socket import socket
from json import loads
from base64 import b64decode


def main():
    client = socket()
    client.connect(('127.0.0.1', 5566))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024字节
    data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成JSON字符串并转换成字典
    # loads函数的作用就是将JSON字符串转成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('/Users/Hao/' + filename, 'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
    print('图片已保存.')


if __name__ == '__main__':
    main()


from socket import socket
from json import loads
from base64 import b64decode


def main():
    client = socket()
    client.connect(('127.0.0.1', 5566))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024字节
    data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成JSON字符串并转换成字典
    # loads函数的作用就是将JSON字符串转成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('/Users/Hao/' + filename, 'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
    print('图片已保存.')


if __name__ == '__main__':
    main()

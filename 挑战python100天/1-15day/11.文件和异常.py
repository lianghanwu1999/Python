#TODO 文本操作
"""
'r'	读取 （默认）
'w'	写入（会先截断之前的内容）
'x'	写入，如果文件已经存在会产生异常
'a'	追加，将内容写入到已有文件的末尾
'b'	二进制模式
't'	文本模式（默认）
'+'	更新（既可以读又可以写）
"""

#TODO  读取文本文件
#使用open函数指定路径的文件名，r为读取文件模式（默认也是‘r’）
#encoding参数指定编码（如果不指定，默认值是None，那么在读取文件时使用的是操作系统默认的编码

def main():
    f= open('致橡树.txt','r',encoding='utf-8')
    #读取文本
    print(f.read())
    #关闭文本
    f.close()

if __name__ == '__main__':
    main()

#TODO 异常处理
def main():
    f = None
    try :#可能出现的代码放在try中
        f =open('致橡树.txt','r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError: #可能出现异常的状况
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码！')
    except UnboundLocalError:
        print('读取文件时解码错误！')
    #最后无论程序是否正常都会被执行
    finally:  #TODO 总是执行代码块
        if f :
            f.close()

if __name__ == '__main__':
    main()

#通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
#使用for-in循环逐行读取或者用readlines方法，将文件按行读取到一个列表容器

import time

def main():
    #一次性读取整个文件内容
    with open('致橡树.txt','r',encoding='utf-8') as f:
        print(f.read())
    #with 关键词 可以自动释放文件资源

    #通过for-in 循环逐行读取
    with open('致橡树.txt','r',encoding='utf-8')as f:  # 相当于 with open f
        for line in f:
            print(line,end='')
            time.sleep(0.5)  #每隔0.5 秒读取一行
    print()

    #读取文件按行读取到列表中
    with open('致橡树.txt','r',encoding='utf-8') as f:
        lines = f.readline()
    print(lines)

if __name__ == '__main__':
    main()


#TODO 写入文件
#TODO 将1-9999之间的素数分别写入三个文件中（1-99之间的素数保存在a.txt中，
# 100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）

from math import sqrt

def is_prime(n):
    """判断素数的函数"""
    assert  n> 0
    for factor in range(2,int(sqrt(n))+1):
        if n % factor == 0:
            return False
        return True if n !=1 else False

def main():
    filenames = ('a.txt','b.txt','c.txt')
    fs_list = []
    try :
        for filename in filenames:
            fs_list.append(open(filename,'w',encoding='utf-8'))
        for number in range(1,10000):
            if is_prime(number):
                if number <  100:
                    fs_list[0].write(str(number) +'\n')
                elif number <1000:
                    fs_list[1].write(str(number)+ '\n')
                else:
                    fs_list[2].write(str(number) + '\n')

    except IOError as ex:
        print(ex)
        print('写文件时发生错误！')

    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成')

if __name__ == '__main__':
    main()

#TODO 读写二进制文件
#'b'	二进制模式
#'rb' 读取二进制文件
#’wb‘ 写入二进制文件

def main():
    try:
        with open('guido.jpg','rb') as fs1:
            data = fs1.read()
            print(type(data)) #<class 'bytes'>
        with open('吉多.jpg','wb')as fs2:
            fs2.write(data)    # #TODO  write写入（有已有文件写入，没有文件创建文件再写入。）
    except FileExistsError as e:
        print('指定的文件无法打开')
    except IOError as e:
        print('读写文件时出现错误。')
    finally:
        print('程序执行结束。')   # finally

if __name__ == '__main__':
    main()


#TODO 保存json 格式

import json

def main():
    mydict = {
        'name' : '汉武',
        'age' : 38,
        'qq' : 123456,
        'friends' :['王大锤','白元芳'],
        'cars' : [
            {'brand' :'BYD','max_speed':180},
            {'brand' :'Audi','max_speed':280},
            {'brand':'Benz','max_speed':320}
        ]
}
    """
    json模块主要有四个比较重要的函数，分别是：
    dump - 将Python对象按照JSON格式序列化到文件中
    dumps - 将Python对象处理成JSON格式的字符串
    load - 将文件中的JSON数据反序列化成对象
    loads - 将字符串的内容反序列化成Python对象

    """
    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)  #TODO  dump - 将Python对象按照JSON格式序列化到文件中
    except IOError as e:
        print(e)
    print('保存数据完成！')

if __name__ == '__main__':
    main()

#TODO 将字符串的内容反序列化成Python对象

import requests
import json

def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)   #将字符串的内容反序列化成Python对象
    for news in data_model['news_list']:
        print(news['title'])

if __name__ == '__main__':
    main()


#TODO  小结：
"""
1.文本处理：
'r'	读取 （默认）
'w'	写入（会先截断之前的内容）
'x'	写入，如果文件已经存在会产生异常
'a'	追加，将内容写入到已有文件的末尾
'b'	二进制模式   'wb' 二进制写入 ，'br' 二进制读取
't'	文本模式（默认）
'+'	更新（既可以读又可以写）

2.异常处理
try: 
    放入可以有异常代码
except  异常情况 （如：FileNotFoundError）
     print('输出情况')
Finally :   #最后无论程序是否正常都会被执行
      print()
      
3.保存json 文件
3.1 引入 模块 json  
3.2 引入函数
json模块主要有四个比较重要的函数，分别是：
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象

4.保存文件方面
with open('吉多.jpg','wb')as fs2:   #相当于 with open fs2:    #括号里面填入文件名，文件写入格式。
    fs2.write(data)     #TODO  write写入（有已有文件写入，没有文件创建文件再写入。）
    
"""

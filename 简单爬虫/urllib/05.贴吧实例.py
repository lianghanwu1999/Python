#TODO 此项目可以下载百度贴吧里每个吧内的所有内容的html文件。

#请求模块导入
from urllib.request import urlopen,Request
#解析模块
from urllib.parse import urlencode
#调用使用fake_useragent库伪装请求头
from fake_useragent import UserAgent


#请求方法
def get_html(url):
    #用户代理：
    headers = {
        "user_agent" :UserAgent().Chrome    #调用fake_useragent模块。
    }
    request = Request(url,headers=headers)
    #请求内容：
    response = urlopen(request)
    #读取内容：
    print(response.read().decode())
    #返回所要读取的值
    return response.read()


#保存方法
def save_html(filename,html_bytes):      #可以修改（）里面的值来变成新的项目
    with open(filename,"wb") as f:       #打开文件f
        f.write(html_bytes)              #写入并自动保存。

#调用方法
def main():
    comtent = input("请输入要下载的内容 ：")
    num = input("请输入要下载的页码：")
    base_url = "https://tieba.baidu.com/f?ie=utf-8&{}"
    for pn in range(int(num)):   #因百度贴吧的的页码的pn 值是随着页数而改变的，既要动态修改，遇到没有相关类型的项目时可以不再考虑。

        args = {
            "pn" : pn *50 ,      #百度贴吧切换每一页 固定值 pn 会增加 50
            "kw" : comtent       # 将内容设置为一个变量
        }
        filename = "第" + str(pn + 1) + "页.html"     #标注好每一页保存时的名称
        args = urlencode(args)                        #将get请求中特定编码进行转译
        print("正在下载" + filename)
        html_bytes = get_html(base_url.format(args))  #转译get请求，要求转成bytes格式。
        save_html(filename,html_bytes)


if __name__ == '__main__':

    main()

"""
    Requests 库：安装 pip install requests
    官方文档：
        http://cn.python-requests.org/zh_CN/latest/
    可以做什么？
        与urllib相似

    get 请求
        定制头部 ：requests.get(url=url,headers=headers,params=data)

    响应对象：（这里的r = request ）
        r.text 字符串形式查看响应
        r.content 字符类型查看响应
        r.encoding 查看或者设置编码类型
        r.encoding 查看或者设置编码类型
        r.status_code 查看响应状态
        r.headers 查看响应头部
        r.url 查看请求url
        r.json 查看json数据

    post请求
        定制头部post请求 ： requests.post(url=url ,headers = headers,data= data)






"""
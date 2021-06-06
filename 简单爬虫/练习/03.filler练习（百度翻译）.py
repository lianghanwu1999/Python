"""
code by python3.7,utf8
"""
"""
post:
    表单数据的处理：from_data =  urllib.parse.urlencode(form_data).encode()
    filler 抓包，带箭头小本表示post
    
    filler对json的常见查看
        请求部分：
        webForms:查看post 请求表单，用于构造post清单
        Raw : 查看头部信息，构造headers
        response部分：
        headers-Content-Encoding :参看response 的编码 ---先查就不会有下面的错误了
        JSON ： 查看JSON解析
    """
import urllib.request
import urllib.parse

post_url = 'https :// fanyi.baidu.com/sug'
word = 'baby'

#构建post表单数据
from_data = {
    'kw' : word,
}
"""
from_data = urllib.parse.urlencode(from_data)  #构建post清单
报错：POST data should be bytes
urlencode 结果是utf-8,但是post数据规定为字节类型
需要再使用encode转成字节型

"""
from_data = urllib.parse.urlencode(from_data).encode()

#发送请求

headers = {
'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
}

request = urllib.request.Request(url=post_url,headers=headers)
response = urllib.request.urlopen(request,data=from_data)
print(response.read(),decode())

#获取完整的百度翻译json
post_url = 'https://fanyi.baidu.com/v2transapi'
from_data = {
    'from' : 'en',
    'to' : 'zh',
    'query' : 'wolf',
    'transtype':	'realtime',
    'simple_means_flag':	'3',
    'sign':	'275695.55262',
    'token':	'd7627f387f6d0d573368943337783227',
}
headers ={
'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    'Host': 'fanyi.baidu.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '120',
    'Accept': '*/*',
    'Origin': 'https://fanyi.baidu.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://fanyi.baidu.com/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'BAIDUID=C609024C7FB6D201F3FDA13AB612DCCD:FG=1; '
              'BIDUPSID=C609024C7FB6D201F3FDA13AB612DCCD; PSTM=1548991277; '
              'BDUSS=WdmNU96am9Hc3hNc2J5Mn5DZWFsS3hEYmV4c0lGYWJIM1VEekFPdWxpY'
              'mI1WDFjQVFBQUFBJCQAAAAAAAAAAAEAAAAA0Kows~bK28j8tvu6xTg4AAAAAAAA'
              'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANtYVlzbWFZcS; '
              'delPer=0; PSINO=6; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; '
              'BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; '
              'H_PS_PSSID=1445_21103_18560_28585_28557_28519_20718; locale=zh; REALTIME_TRANS_SWITCH=1; '
              'FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03d'
              'c91cb9e8c025574=1551442945,1551442984; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1551442984; to_lang_often=%5B%7B%22value'
              '%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; '
              'from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',


}
"""
2.
UnicodeDecodeError : 'utf-8' codec can't decode byte 0x8b in position 1 :invalid start byte
完成1后编码错误

'Accpet-Encoding' : 'gzip',deflate ,'br' ,注意此条，zip是压缩格式
屏蔽该头信息就能到json ,浏览器和fiddler 自动解json，但是在py中能借助json在线解析
https：// www.json.cn /
"""
#提交post三部曲（urllib库的post请求）
request = urllib.request.Request(url=post_url,headers=headers) #构建请求对象：也是伪装headers
form_data =urllib.parse.urlencode(form_data).encode()         #构建post 清单
response = urllib.request.urlopen(request,data=from_data)     #获取url 链接
print(response.read().decode())

"""
1
{"error" : 997,"from" : "en" ,"to" : "zh","query" : "wolf"}
暴力构造post失败，正常情况下是error 是0
解决方法：将fiddler中 RAW 的全部信息拷贝到headers，如上
"""
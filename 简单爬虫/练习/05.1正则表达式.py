"""
    5.1正则表达式-爬取嗅图
    code utf-8
"""

import urllib.parse
import urllib.request
import re

def download_image(content,file):
    # pattern = re.compile(r'<div class = "thumb">.*?<img src="(.*?)" alt="(.*?)"/>.*?</div>',re.S)
    """
    re.S 可以使 . 具有匹配换行的功能
    正则中加入括号，表示匹配的目标字段，也是想要获取的信息

    pattern 为得的图片的url
    _pattern 为了得到图片想应的段子
    """
    pattern = re.compile(r'<div class = "thumb">.*?<img src = "(.*?)".*?</div>',re.S)
    _pattern= re.compile(r'<div class = "content".*?<span>(.*?)"</span>.*?</div>',re.S)



    pass
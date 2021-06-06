from selenium import webdriver
from time import sleep

# 浏览器选择（目前只有Chrome浏览器有插件）
driver =webdriver.Chrome()
# 其他浏览器选择：
# driver =webdriver.firefox()
# driver = webdriver.ie()
# driver = webdriver.opera()

# driver.get("www.baidu.com")

# driver.get()采取器:（获取目标位置）
driver.get("D:/桌面/web素材/注册A.html")
# 自动填写
driver.find_element_by_id("userA").send_keys("admin")  #id选择器

sleep(2)
driver.quit()


# TODO webdriver中的定位(定位单个元素)
"""
首先选择器（比较快）：

1.通过id定位：快，常用
dr.find_element_by_id("kw")

2.通过name定位:
dr.find_element_by_name("wd")

3.通过class name定位:类名定位
dr.find_element_by_class_name("s_ipt")

4.通过tag name定位:标签名定位
dr.find_element_by_tag_name("input")

在上述没有情况下可以使用以下万能定位选择器：

1.xpath定位：（万能，缺点慢）:
# XPath 使用路径表达式在 XML 文档中选取节点
基本语法：  @ 选取元素 ， * 匹配任何元素节点  ， // 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置
通过xpath定位，xpath定位有N种写法，这里列几个常用写法:
dr.find_element_by_xpath("//*[@id='kw']")   //选取所有任何元素节点，且这些元素拥有值为 kw 的 id 属性
dr.find_element_by_xpath("//*[@name='wd']")    
dr.find_element_by_xpath("//input[@class='s_ipt']")
dr.find_element_by_xpath("/html/body/form/span/input")
dr.find_element_by_xpath("//span[@class='soutu-btn']/input")
dr.find_element_by_xpath("//form[@id='form']/span/input")
dr.find_element_by_xpath("//input[@id='kw' and @name='wd']")

5.css选择器定位：（万能，可能找得到）==推荐(最快)
通过css定位，css定位有N种写法，这里列几个常用写法:
dr.find_element_by_css_selector("#kw")   //id定位选择器
dr.find_element_by_css_selector("[name=wd]")   //属性值选择器
dr.find_element_by_css_selector(".s_ipt")      // 类选择器
dr.find_element_by_css_selector("html > body > form > span > input")   //子类定位选择
dr.find_element_by_css_selector("span.soutu-btn> input#kw")
dr.find_element_by_css_selector("form#form > span > input")

6.文本连接定位（有超链接是定位文本）（最方便，但相对最慢）：

<a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a>
<a class="mnav" href="http://www.hao123.com" name="tj_trhao123">hao123</a>

通过link text定位: link_text 是：超链接载体的精确匹配（最慢）
dr.find_element_by_link_text("新闻")
dr.find_element_by_link_text("hao123")

通过link text定位:partial_link_text是对：超链接载体的模糊匹配（相对慢）

dr.find_element_by_partial_link_text("新")
dr.find_element_by_partial_link_text("hao")
dr.find_element_by_partial_link_text("123")

"""


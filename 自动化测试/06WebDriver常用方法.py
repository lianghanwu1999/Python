from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
"""
点击输入
clear()： 清除文本。
send_keys (value)： 模拟按键输入。
click()： 单击元素。
"""
# # 清除文本
# driver.find_element_by_id("kw").clear()
# # 模拟输入
# driver.find_element_by_id("kw").send_keys("selenium")
# # 模拟点击元素
# driver.find_element_by_id("su").click()
#
"""
提交：
submit()方法用于提交表单：具有自动回车键操作
"""
# # 元素定位
# search_text = driver.find_element_by_id('kw')
# # 元素输入
# search_text.send_keys('selenium')
# # 点击提交：submit()相当于click，应用范围远不及 click()广泛
# 搜索框输入关键字之后的“回车” 操作， 就可以通过该方法模拟
# search_text.submit()

"""
其他方法：
size:返回元素的尺寸
text：返回元素文本信息
get_attribute：返回元素的属性值
is_displayed()：返回元素的结果是否可见， 返回结果为 True 或 False
"""

# 获得输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)

# 返回百度页面底部备案信息
text = driver.find_element_by_id("s-bottom-layer-right").text
print(text)

# 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

# 返回元素的结果是否可见， 返回结果为 True 或 False
result = driver.find_element_by_id("kw").is_displayed()
print(result)

sleep(5)
driver.quit()
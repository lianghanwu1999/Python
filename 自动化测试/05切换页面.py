from selenium import webdriver
from time import sleep

driver =webdriver.Chrome()

#访问百度首页
first_url= 'http://www.baidu.com'
print("now access %s" %(first_url))
# 第一个页面
driver.get(first_url)

#访问新闻页面
second_url='http://news.baidu.com'
print("now access %s" %(second_url))
# 第二个页面
driver.get(second_url)

#返回（后退）到百度首页
print("back to  %s "%(first_url))
# 返回前一页面
driver.back()

#前进到新闻页
print("forward to  %s"%(second_url))
# 前进到后一个页面
driver.forward()

#刷新当前页面;必要时要F5手动
driver.refresh()

# 窗口停留：时间：秒
sleep(2)
# 全部窗口关闭
driver.quit()
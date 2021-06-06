from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime

driver = webdriver.Chrome()

# 设置隐式等待为10秒：将错误显示时间设置为10秒
driver.implicitly_wait(10)   #先设置时间，在进行检索定位S
driver.get("http://www.baidu.com")

"""
它并不针对页面上的某一元素进行等待。当脚本执行到某个元素定位时，如果元素可以定位，则继续执行；
如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到。
假设在第6秒定位到了元素则继续执行，若直到超出设置时长（10秒）还没有定位到元素，则抛出异常。
即是最长可以等待时间为设置的时长（10秒），超过了则会抛出异常
"""

try:
    # 显示一个字符串格式时间:开始时间
    print(ctime())
    # 一个错误表达式：让系统检索定位，如果定位到了继续执行，超过时长，抛出异常
    driver.find_element_by_id("kw22").send_keys('selenium')
except NoSuchElementException as e:
    # 打印异常
    print(e)
finally:
    # 显示一个字符串格式时间:结束时间
    print(ctime())
    driver.quit()

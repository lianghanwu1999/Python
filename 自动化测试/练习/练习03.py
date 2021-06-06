from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# # driver.get()采取器:
driver.get("D:/桌面/web素材/注册A.html")
# 自动填写
# 填写用户名
# id选择器
# driver.find_element_by_css_selector("#userA").send_keys("123")
# # 标签选择器
# driver.find_elements_by_css_selector("input")[1].send_keys("123")
# # 类选择器
# driver.find_element_by_css_selector(".telA").send_keys("123")
# 窗口最大化
driver.maximize_window()
# 停留2秒
sleep(2)
driver.find_element_by_css_selector("#userA").send_keys("123")
# 刷新
driver.refresh()
# 注册页面按钮点击
# click()按钮的点击
# 在没有id情况下，使用xpath()
# driver.find_element_by_xpath("//button[@type='submitA'][@value='注册A'][@title='加入会员A']").click()
sleep(10)
driver.quit()
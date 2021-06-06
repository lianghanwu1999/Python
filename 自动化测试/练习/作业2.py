from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# # driver.get()采取器:
driver.get("D:/桌面/web素材/注册A.html")
# 自动填写
# 填写用户名
driver.find_element_by_id("userA").send_keys("admin")
# 填写密码
driver.find_element_by_id("passwordA").send_keys("12345678")
# 填写电话号码
driver.find_element_by_id("telA").send_keys("12345678")
# 填写邮箱号
driver.find_element_by_id("emailA").send_keys("10086")

# 注册页面按钮点击
# click()按钮的点击
# 在没有id情况下，使用xpath()
driver.find_element_by_xpath("//button[@type='submitA'][@value='注册A'][@title='加入会员A']").click()
sleep(10)
driver.quit()
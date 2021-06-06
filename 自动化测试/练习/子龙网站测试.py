from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://data.lggnfx.com/user/login.html/")
driver.find_element_by_id('username').send_keys("1693428959@qq.com")
driver.find_element_by_id('psw').send_keys("1693428959")
# 点击搜索按钮:按钮id:su
# .click()被点击
# driver.find_element_by_id(By.id("su")).click()
driver.find_element_by_id("submit").click()
driver.find_element_by_id("perhead").click()
driver.find_element_by_css_selector("html > body > app > header > header-box > header-login > perinf")
# driver.find_element_by_xpath('//*[@id="su"]').click() # 点击百度一下按钮
# 页面停留时间
# sleep(10)
# driver.quit()
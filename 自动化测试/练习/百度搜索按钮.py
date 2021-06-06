from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id('kw').send_keys("黑马程序员")
# 点击搜索按钮:按钮id:su
# .click()被点击
# driver.find_element_by_id(By.id("su")).click()
driver.find_element_by_xpath('//*[@id="su"]').click() # 点击百度一下按钮
# 页面停留时间
sleep(10)
driver.quit()
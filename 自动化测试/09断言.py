# 拿实际结果与预期进行比较。这个比较的称之为断言
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

print("Before search =========")

# 打印当前页面title
title =driver.title
print(title)

#打印当前页面URL
now_url =driver.current_url
print(now_url)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(1)

print("After search================")

#再打印当前页面title
title = driver.title
print(title)

#打印当前页面URL
now_url=driver.current_url
print(now_url)

#获取结果数目
user = driver.find_element_by_class_name("nums").text
print(user)

driver.quit()
from selenium import webdriver
from time import sleep

#访问百度
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#设置浏览器窗口大小
driver.set_window_size(500,500)

#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

#通过javascript设置浏览器窗口的滚动条位置
js = "window.scrollTo(100,450);"
# 调用js代码
driver.execute_script(js)
sleep(3)

driver.quit()
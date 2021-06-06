from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

#截取当前窗口，并指定截图图片的保存位置(捕捉测试页面效果截图)
driver.get_screenshot_as_file("D:/桌面/01/001.jpg")

driver.quit()
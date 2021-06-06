from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 显示全屏
driver.maximize_window()

# 鼠标悬停设置链接
# driver.find_element_by_link_text("设置").click()  #精确搜索：比较慢
driver.find_element_by_id("s-usersetting-top").click()
sleep(1)

# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

#搜索结果显示条数
# sel = driver.find_element_by_xpath("//selcet[@id='nr']")
# 使用id定位，定位，并使用click选择按下
sel = driver.find_element_by_id("nr_3").click()
Select(sel).select_by_value('50')  #显示50条数  //选择显示

# 保存设置

# driver.find_element_by_link_text("保存设置").click()
# driver.find_element_by_id("prefpanelgo setting-btn c-btn c-btn-primary").click()
driver.find_element_by_class_name("prefpanelgo setting-btn c-btn c-btn-primary").click()
# sleep(2)
time.sleep(2)

driver.quit()
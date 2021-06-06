from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 浏览器全屏显示
driver.maximize_window()
# 鼠标悬停至“设置”连接
link =driver.find_element_by_partial_link_text('设置')
# 对定位到的元素执行鼠标悬停操作(百度页面悬停，显示下一级菜单)
ActionChains(driver).move_to_element(link).perform()

#打开搜索设置
driver.find_element_by_link_text("搜索设置").click()

# 保存设置
# driver.find_elements_by_class_name("prefpanelgo setting-btn c-btn c-btn-primary").click()
driver.find_element_by_link_text("保存设置").click()
time.sleep(2)

#接收警告框
driver.switch_to.alert.accept()

driver.quit()
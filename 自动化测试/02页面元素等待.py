from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# # driver.get()采取器:
driver.get("D:/桌面/web素材/注册实例.html")
# 隐形等待
# 延迟代码报错时间：秒
driver.implicitly_wait(5)
# 错误的信息（令其有报错信息）
driver.find_element_by_css_selector("#userA1").send_keys("123")
# 关闭close  ->只能关闭，启动的主窗口
sleep(20)
# driver.close()
#关闭又druver所有窗口（关闭的是driver驱动对象）
driver.quit()
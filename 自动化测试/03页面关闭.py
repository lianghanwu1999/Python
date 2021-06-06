from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# # driver.get()采取器:
driver.get("D:/桌面/web素材/注册实例.html")

#点击注册A页面
driver.find_element_by_link_text("注册A网页").click()
# 停留2秒
sleep(2)
#2.再点击注册B页面
driver.find_element_by_link_text("注册B网页").click()
# 停留窗口时间
sleep(2)

# 关闭close  ->只能关闭，启动的主窗口
# driver.close()
#关闭又druver所有窗口（关闭的是driver驱动对象）
driver.quit()
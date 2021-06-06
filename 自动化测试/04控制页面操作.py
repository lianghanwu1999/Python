from selenium import webdriver
from time import sleep

driver =webdriver.Chrome()
driver.get("http://m.baidu.com")
# 参数数字为像素点
print("设置浏览器宽480、高800显示")
driver.set_window_size(480, 800)
# 浏览器全屏显示
driver.maximize_window()

# 窗口停留：时间：秒
sleep(2)
# 关闭所有窗口
driver.quit()

# switch_to.window()方法，可以实现在不同的窗口之间切换
from selenium import webdriver
import time
from time import sleep


driver = webdriver.Chrome()
# 系统最大等待无精准操作时间
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

#获取百度搜索窗口句柄
sreach_windows = driver.current_window_handle

driver.find_element_by_partial_link_text('登录').click()
# 点击用户名登录
driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
# 自动输入用户账号
driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("admin")
# 自动输入用户密码
driver.find_element_by_name("password").send_keys("password")
# 点击登录提交
driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
# driver.find_element_by_partial_link_text('立即登录').click()
# sleep(2)

#获取当前所有打开的窗口句柄
all_handle = driver.window_handles


#进入注册窗口
# for handle in all_handle:
#     if handle != sreach_windows:
#         driver.switch_to.window(handle)
#         print("now register window")
#         driver.find_element_by_name("account").send_keys('username')
#         driver.find_element_by_name('password').send_keys('password')
#         time.sleep(2)

sleep(5)
driver.quit()


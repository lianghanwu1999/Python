from selenium import webdriver
from time import sleep

# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.cn")

# 定位到要悬停的元素
above = driver.find_element_by_link_text("设置")  #精确定位
# 对定位到的元素执行鼠标悬停操作（用于不用点击，鼠标悬停就可以显示下一级菜单的功能）
ActionChains(driver).move_to_element(above).perform()

"""
ActionChains 类提供了鼠标操作的常用方法：

perform()： 执行所有 ActionChains 中存储的行为；

context_click()： 右击；

double_click()： 双击；

drag_and_drop()： 拖动；

move_to_element()： 鼠标悬停。

"""
sleep(5)
driver.quit()
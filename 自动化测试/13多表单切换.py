from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.126.com")

# 默认可以直接取表单的id 或name属性
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_class_name("email").clear()
driver.find_element_by_class_name("email").send_keys("username")
driver.find_element_by_class_name("password").clear()
driver.find_element_by_class_name("password").send_keys("password")
driver.find_element_by_class_name("dologin").click()
# 跳回最外层的页面
driver.switch_to.default_content()

driver.quit()
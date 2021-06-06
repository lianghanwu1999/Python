from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 显式等待使WebdDriver等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常
element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "kw")))
element.send_keys('selenium')
# WebDriverWait(driver, 5, poll_frequency=0.5, ignored_exceptions=None)
driver.quit()


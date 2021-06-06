from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")
"""
操作cookie的方法：

get_cookies()： 获得所有cookie信息。

get_cookie(name)： 返回字典的key为“name”的cookie信息。

add_cookie(cookie_dict) ： 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值。

delete_cookie(name,optionsString)：删除cookie信息。“name”是要删除的cookie的名称，
“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。

delete_all_cookies()： 删除所有cookie信息。

"""
# 获取cooking信息
cookie = driver.get_cookies()

#将cookie信息打印
print(cookie)

# 向cookie的name和value添加会话信息
driver.add_cookie({'name':'key-aaaaaa','value':'value-bbbbbb'})

# 遍历cookie中的name 和value 信息并打印，当然还能添加信息
for cookie in driver.get_cookies():
    print("%s->%s" %(cookie["name"],cookie['value']))

driver.quit()
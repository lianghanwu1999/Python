from selenium import webdriver
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('upfile.html') #文件名
driver.get(file_path)

# 定位上传按钮，添加本地文件：添加本地文件位置
driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')

driver.quit()

"""
创建的代码文件如下:文件名：upfile.html
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<title>upload_file</title>
<link href="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" />
</head>
<body>
  <div class="row-fluid">
    <div class="span6 well">
    <h3>upload_file</h3>
      <input type="file" name="file" />
    </div>
  </div>
</body>
<script src="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.js"></scrip>
</html>

"""
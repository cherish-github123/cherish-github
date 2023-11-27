# 导入selenium
from selenium import webdriver
import time

# TODO 打开浏览器-chrome浏览器
# 打开chrome浏览器,返回浏览器驱动对象
driver = webdriver.Chrome()
time.sleep(2)
driver.get("https://music.qq.com")
print(driver.title)
# TODO 退出浏览器
time.sleep(5)
driver.quit()

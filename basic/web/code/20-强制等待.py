from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器窗口
driver.get("https://www.baidu.com/")
element=driver.find_element(By.ID,"kw")
time.sleep(3)   # 如果由于网络原因导致元素定位不到，则下面的代码会报错，强制让浏览器等待3秒后再运行
element.send_keys("天气预报")
time.sleep(2)
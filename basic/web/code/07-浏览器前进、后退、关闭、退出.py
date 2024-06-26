from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# 打开浏览器
driver = webdriver.Chrome()

# 请求百度
time.sleep(2)
driver.get('https://www.baidu.com')

# TODO 浏览器后退
# 先输入内容进行搜索，再后退
kw = driver.find_element(By.ID, 'kw')
kw.send_keys('天气预报')
time.sleep(2)
su = driver.find_element(By.ID, 'su')
su.click()
time.sleep(2)
driver.back()
# TODO 浏览器前进
time.sleep(2)
driver.forward()
# TODO 浏览器刷新
time.sleep(2)
driver.refresh()
# TODO 关闭浏览器当前窗口
driver.close()
# TODO 退出浏览器
driver.quit()






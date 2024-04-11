from selenium import webdriver
# import后面的By是by模块下面的一个类，类属性就是八种元素定位方式
from selenium.webdriver.common.by import By
import time

# 用selenium下面的webdriver来创建一个浏览器对象，并打开chrome浏览器
driver = webdriver.Chrome()    # 创建一个浏览器驱动对象driver
time.sleep(2)
driver.maximize_window()  # 最大化窗口，是浏览器驱动对象上面的方法



# 在浏览器中输入网址-www.baidu.com
driver.get('http://www.baidu.com')
time.sleep(2)

# 定位搜索框，在搜索框中输入"天气预报"
kw = driver.find_element(By.ID, 'kw')
kw.send_keys('天气预报')
time.sleep(2)

# 定位“百度一下”按钮，点击进行搜索
su = driver.find_element(By.ID, 'su')
su.click()
time.sleep(3)
print(driver.title)   # 获取浏览器窗口的标题

# 关闭浏览器
driver.quit()
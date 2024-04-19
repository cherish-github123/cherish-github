from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 1、打开Chrome，打开百度首页
driver = webdriver.Chrome()
time.sleep(2)

# TODO 请求百度
driver.get('https://www.baidu.com')
time.sleep(2)

# 2、搜索框输入 "天气预报"，点击百度一下
# TODO 元素定位 driver.find_element(定位方式, 定位的值)
kw = driver.find_element(By.ID, 'kw')
# TODO ------------通过修改元素的js改变边框的颜色，确认定位到元素------
driver.execute_script(
    "arguments[0].setAttribute('style',arguments[1]);",
    kw,
    "border:2px solid red;"
)
# find_element是webdriver驱动对象这个类上面的一个对象方法，上面已经用webdriver创建了driver对象,所以是用对象调用方法
# TODO 搜索框输入内容
kw.send_keys('天气预报')
time.sleep(2)

# 元素定位 - 百度一下
su = driver.find_element(By.ID, 'su')
su.click()


# 3、等待2秒
time.sleep(7)

# 4、TODO 打印页面标题
print(driver.title)

# 5、关闭Chrome浏览器
driver.quit()
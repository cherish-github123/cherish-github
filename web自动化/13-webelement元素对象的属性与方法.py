import time
import os
from selenium.webdriver.common.by import By
from selenium import webdriver

# 打开浏览器，访问百度
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
kw = driver.find_element(By.ID, 'kw')

# TODO 1 常用属性
# id标识，不是html标签属性那个id
print(kw.id)
# size, 标签在html页面中的宽高
print(kw.size)
# rect, 宽高和坐标
print(kw.rect)
# text  获取标签的文本内容
print(kw.text)   # input是单标签，所有没有文本
# tag_name 获取标签名
news = driver.find_element(By.LINK_TEXT, '新闻')
print(news.tag_name)

# TODO 2 常用方法
# 输入内容 webelement.send_keys(内容)
kw.send_keys('天气预报')
# 清空内容  webelement.clear()
kw.clear()
# 点击   webelement.click()
driver.find_element(By.ID, 'su').click()
# get_attribute() 获得标签属性值的方法
print(kw.get_attribute('outerHTML'))  # 获取标签的源码

"""
# TODO is_displayed()  判断元素是否可见
# 请求目标网址 - https://sahitest.com/demo/visible.htm
time.sleep(2)
driver.get('https://sahitest.com/demo/visible.htm')

div1 = driver.find_element(By.XPATH, '/html/body/div[3]')
print(div1.is_displayed())  # False
print(driver.find_element(By.ID, 'ud').is_displayed()) # True
"""


# TODO is_enabled()  判断元素是否可用
url = 'file://' + os.path.join(os.path.dirname(__file__), 'html/demo.html')
# 请求网址 - url
time.sleep(2)
driver.get(url)

# 定位第一个input
input1 = driver.find_element(By.XPATH, '//input[1]')
print(input1.is_enabled())  # True
# 定位第二个input
input2 = driver.find_element(By.XPATH, '//input[2]')
print(input2.is_enabled())  # False

# 退出浏览器
time.sleep(3)
driver.quit()

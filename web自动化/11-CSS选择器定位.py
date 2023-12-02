import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# print(__file__)                      # 获取当前脚本的路径
# print(os.path.dirname(__file__))     # 获取当前脚本的所在目录

# 打开浏览器， 请求目标网址-百度
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# TODO 1 使用id属性定位,用 # 表示id,定位id属性值为 kw 的标签
# kw=driver.find_element(By.CSS_SELECTOR,'#kw')
# print(kw.get_attribute("outerHTML"))
#
# # TODO 2 通过类属性定位 ,用 . 表示类属性，定位类属性值为 c-ion 的标签
# s_ipt=driver.find_element(By.CSS_SELECTOR,'.c-icon')
# print(s_ipt.get_attribute("outerHTML"))

# TODO 3 通过标签定位，定位页面所有的a标签
# a=driver.find_elements(By.CSS_SELECTOR,"a")
# pprint(a)
# print(len(a))
# print(a[0].get_attribute("outerHTML"))  # 获取第一个定位到的a标签、属性值

# TODO 4 通过name属性定位
# set = driver.find_element(By.CSS_SELECTOR,'[name="tj_settingicon"]')
# print(set.get_attribute("outerHTML"))

# TODO 5 通过 标签+属性 定位,获取id属性值为 s-usersetting-top 的span标签，百度首页上的设置
# setting=driver.find_element(By.CSS_SELECTOR,'span#s-usersetting-top')
# print(setting.text)

# TODO 6 通过层级关系定位
# todo 6.1 后代选择器： E1 E2
# inputs = driver.find_elements(By.CSS_SELECTOR, '#form input')  # 选取id属性值为form的后代input标签
# pprint(inputs)
# print(len(inputs))

# todo 6.2 子元素选择器: E1 > E2
# # form > input
# inputs = driver.find_elements(By.CSS_SELECTOR, '#form>input')  # 选取id属性值为form的子标签input
# pprint(inputs)
# print(len(inputs))
#
# todo 6.3 并集选择器: E1, E2, E3,
# elements = driver.find_elements(By.CSS_SELECTOR, '#u1, #head_wrapper, #form')  # 选择id属性值为u1,head-wrapper,form的标签
# pprint(elements)
# print(len(elements))

# todo 6.4  nth-child()  结构伪类选择器，索引获取
# input = driver.find_elements(By.CSS_SELECTOR, 'span input:nth-child(1)')  # 选取span的后代标签中的第一个input标签
# print(input[0].get_attribute('outerHTML'))

# 浏览器退出
time.sleep(2)
driver.quit()

"""
Xpath是在XML文档中查找信息的语言，可以在XML文档中对元素和属性进行遍历，HTML是标准的XML
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint

# 打开浏览器, 访问百度
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# TODO 1 通过元素标签名定位
inputs=driver.find_elements(By.XPATH,"//input")   # 相对路径，从匹配选择的当前节点选择文档中的所有input标签
pprint.pprint(inputs)
print(len(inputs))

# TODO 2 通过元素属性定位
tj_briicon=driver.find_element(By.XPATH,'//span[@class="title-content-title"]')
print(tj_briicon.text)    # 打印标签的文本内容

# TODO 3 contains 模糊匹配，通过属性值包含 百度 的value属性
baidu=driver.find_element(By.XPATH,'//*[contains(@value,"百度")]')
print(baidu.get_attribute("outerHTML"))   # 获取标签

# TODO 4 通过元素索引定位,定位id属性位s-top-left的div标签下面的第三个a标签:地图
ditu=driver.find_element(By.XPATH,'//div[@id="s-top-left"]/a[3]')
print(ditu.get_attribute("outerHTML"))

# TODO 5 通过逻辑运算符定位，通过and符号同时定位name=wd 和class=s_ipt的标签
element = driver.find_element(By.XPATH, '//*[@name="wd" and @class="s_ipt"]')
print(element.get_attribute("outerHTML"))

time.sleep(2)
driver.quit()


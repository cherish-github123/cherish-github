from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# TODO 1 简单操作：先获取到页面元素对象webelement，再用webelement定位下拉选项
# driver=webdriver.Chrome()
# driver.get("https://sahitest.com/demo/selectTest.htm")
# s1=driver.find_element(By.CSS_SELECTOR,"#s1")
# fax=s1.find_element(By.CSS_SELECTOR,"option[value='49']")
# time.sleep(2)
# fax.click()
# time.sleep(2)
# driver.quit()

# TODO 2 通过select类方式获取下拉框，先获取到下拉框，创建select类的实例，传入webelement对象
driver=webdriver.Chrome()
driver.get("https://sahitest.com/demo/selectTest.htm")
s1=driver.find_element(By.CSS_SELECTOR,"#s1")
select=Select(s1)
time.sleep(2)

# 通过索引、value值和文本内容定位下拉框选项
# todo 1 通过索引方式获取
select.select_by_index(2)
time.sleep(2)
# todo 2  通过value值获取
select.select_by_value('51')
time.sleep(2)
# todo 3 通过文本内容获取
select.select_by_visible_text("Business Phone")
time.sleep(2)
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

# 隐式等待，在查找页面元素时，webdriver将等待一定的时长，直到页面上加载到这个元素，如果时间完毕还是加载不到，抛出NoSuchElementException异常
driver.implicitly_wait(10)

driver.get("https://home.cnblogs.com/blog/")
my_blok=driver.find_element(By.LINK_TEXT,"我的博客")
my_blok.click()
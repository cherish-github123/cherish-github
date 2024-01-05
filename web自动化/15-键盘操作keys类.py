from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1.打开浏览器
class Test:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get(self):   # 访问百度
        self.driver.get("http://www.baidu.com")

    def locate(self):  # 定位到搜索框，输入内容,全选内容并进行复制,然后粘贴到360浏览器的输入框中
        kw=self.driver.find_element(By.ID,"kw")
        kw.send_keys("天气预报")
        kw.send_keys(Keys.CONTROL,"a")
        kw.send_keys(Keys.CONTROL,"c")
        self.driver.get("https://www.so.com")
        self.driver.find_element(By.ID,"input").send_keys(Keys.CONTROL,"v")

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    test=Test()
    test.get()
    test.locate()
    test.quit()

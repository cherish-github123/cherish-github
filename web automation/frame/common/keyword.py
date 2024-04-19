import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# 获取driver对象
def get_driver(browser='chrome'):
     # 打开浏览器，返回driver对象
     driver=None
     if browser == 'chrome':
         return webdriver.Chrome()
     elif browser == 'Firefox':
         return webdriver.Firefox()
     else:
         print('不支持的浏览器')

     return driver

# 封装
class KeyWord():
    # 实现selenium的二次封装，封装基本的元素定位方法，给page包下面的类继承使用
    def __init__(self, driver):
        # 打开浏览器，设置driver对象
        self.driver = driver
        self.driver.maximize_window()  # 浏览器窗口最大化

    def get(self, url):
        # 访问网址
        try:  # 异常捕获，如果没有异常，就访问网址，如果有异常，就返回无效网址
            self.driver.get(url)
        except Exception as e:
            print(e)
            print('无效网址')

    def find_element(self, locator, timeout=5):
        # 定位单个element对象
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located(locator), message="标签定位不到")
        except TimeoutException as e:
            print(e)

    def find_elements(self, locator, timeout=2):
        # 定位多个element对象
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_all_elements_located(locator), message="找不到元素")
        except Exception as e:
            print(e)
            return []  # 找不到元素就返回一个空列表

    def clear(self, locator):
        # 输入框清空内容
        element = self.find_element(locator)
        if element:
            element.clear()

    def get_attribute(self, locator, attr_name):  # attr_name是先要获取的属性，例如outerHTML
        # 获取元素属性
        element = self.find_element(locator)
        if element:
            return element.get_attribute(attr_name)

    def send_keys(self, locator, content):
        # 输入框输入内容
        element = self.find_element(locator)
        if element:
            element.send_keys(content)

    def click(self, locator):
        # 定位元素，并点击
        element = self.find_element(locator)
        if element:
            element.click()

    def implicitly_wait(self, seconds):
        # 隐式等待
        self.driver.implicitly_wait(seconds)

    def get_element_text(self, locator):
        # 获取标签文本
        element = self.find_element(locator)
        if element:
            return element.text

    def quit(self):
        # 退出浏览器
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    #  1. 调用函数，返回driver对象
    driver_obj = get_driver()
    #  2.访问网址
    base = KeyWord(driver_obj)
    base.get('https://www.baidu.com')

    #  3.搜索框输入天气预报
    time.sleep(2)
    kw = base.find_element((By.ID, 'kw'))
    # 4.输入框清空内容
    time.sleep(1)
    base.clear((By.ID, 'kw'))
    #  5.点击百度一下按钮
    time.sleep(2)
    base.click((By.ID, 'su'))
    # 6.获取属性值
    time.sleep(1)
    print(base.get_attribute((By.ID, 'kw'), 'outerHTML'))
    # 退出浏览器
    time.sleep(1)
    base.quit()
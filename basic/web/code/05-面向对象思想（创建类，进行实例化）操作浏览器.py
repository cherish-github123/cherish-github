from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class TestCase:
    def __init__(self):
        # 打开浏览器,创建浏览器驱动
        self.driver = webdriver.Chrome()

    def get_baidu(self, keyword):
        # 请求百度网址
        self.driver.get('https://www.baidu.com')
        time.sleep(2)
        # 搜索框中输入关键字
        self.driver.find_element('id', 'kw').send_keys(keyword)   # id=By.ID   #类名.属性名=属性值
        # 点击百度一下按钮
        self.driver.find_element('id', 'su').click()
        time.sleep(2)
        # 打印当前页面的标题
        print(self.driver.title)

    def quit(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    testcase = TestCase()
    testcase.get_baidu('天气预报')
    testcase.quit()

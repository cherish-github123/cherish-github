"""
封装常用操作，打开浏览器、元素定位、切换iframe等
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.wait=WebDriverWait(self.driver,timeout=10)


    def open_url(self,url):
        # 打开项目地址
        try:
            self.driver.get(url)
        except Exception as e:
            print("无效的网址")
            print(e)



    def locator_with_webdriverwait(self,method,value):
        """

        :param method: 定位元素的方式，By.ID/By.CLASS_NAME/By.XPATH等
        :param value: 定位方式对应的值
        :return:   返回定位到的元素
        """
        # 使用显示等待定位元素
        locator=(method,value)
        element=self.wait.until(EC.visibility_of_element_located(locator),message="没有定位到该元素")
        self.element_mark(element)
        return element


    def input_content(self,content):
        # 输入内容的方法，可以直接调用上面定位的方法，返回element后输入内容

        self.locator_with_webdriverwait(By.ID,"kw").send_keys(content)



    def element_mark(self,element):
        # 标记元素，标记边框为红色显示
        self.driver.execute_script(
            "arguments[0].setAttribute('style',arguments[1]);",
            element,
            "border:2px solid red"
        )












if __name__ == '__main__':
    base=Base()
    base.open_url("https://www.baidu.com")
    input_element=base.locator_with_webdriverwait(By.ID,"kw")
    base.input_content("python")
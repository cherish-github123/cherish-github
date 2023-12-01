"""
webdriver元素有两种定位方式：
1.find_element  定位单个元素，返回的是单个 webelement 对象
2.find_elements   定位多个元素，返回的是一个包含多个 webelement 对象的列表
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint
import time

class TestCase:
    def __init__(self):
        # 打开浏览器,返回驱动对象
        self.driver = webdriver.Chrome()
        # 访问百度
        self.driver.get('https://www.baidu.com')

    def id(self):
        # TODO 第一种：id定位元素
        kw = self.driver.find_element(By.ID, 'kw')
        # 获取标签属性 web_element.get_attribute('outerHTML')，outerHTML: 获取这个标签对象对应的html内容
        print(kw.get_attribute('outerHTML'))

    def class_name(self):
        # TODO 第二种：类名定位元素
        s_ipt = self.driver.find_element(By.CLASS_NAME, 's_ipt')
        print(s_ipt.get_attribute('outerHTML'))

    def link_text(self):
        # TODO 第三种：通过 a标签的文本定位元素，定位百度首页的“地图”
        map_obj = self.driver.find_element(By.LINK_TEXT, '地图')
        print(map_obj.get_attribute('outerHTML'))

    def partial_link_text(self):
        # TODO 第四种：通过 a标签的部分链接文本定位元素
        hao = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'hao')
        print(hao.get_attribute('outerHTML'))

    def name(self):
        # TODO 第五种：通过name属性定位元素
        wd = self.driver.find_element(By.NAME, 'wd')
        print(wd.get_attribute('outerHTML'))

    def tag_name(self):
        # TODO 第六种：通过标签名称(html标签名)定位元素
        form=self.driver.find_element(By.TAG_NAME, 'form')
        print(form.get_attribute('outerHTML'))

    def find_elements(self):
        list=self.driver.find_elements(By.TAG_NAME, 'input')  # 获取所有的input标签
        pprint.pprint(list)
        print(len(list))


    def quit(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.id()
    # case.class_name()
    # case.link_text()
    # case.partial_link_text()
    # case.name()
    # case.tag_name()
    case.find_elements()

    case.quit()


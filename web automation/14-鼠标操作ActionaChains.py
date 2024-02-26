import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import os


class TestCase:
    def __init__(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        # 请求目标网址
        self.driver.get('https://sahitest.com/demo/clicks.htm')

    def click(self):
        # 简单方式
        """
        time.sleep(2)
        ipt = self.driver.find_element(By.XPATH, '//input[@value="click me"]')
        ipt.click()
        """

        # ac对象方式
        # 创建ac对象
        ac = ActionChains(self.driver)
        ipt = self.driver.find_element(By.XPATH, '//input[@value="click me"]')
        ac.click(ipt).perform()

    def context_click(self):
        # 右击
        time.sleep(1)
        btn = self.driver.find_element(By.XPATH, '//input[@value="right click me"]')

        ac = ActionChains(self.driver)
        ac.context_click(btn).perform()

    def double_click(self):
        # 双击
        time.sleep(1)
        ac = ActionChains(self.driver)
        btn = self.driver.find_element(By.XPATH, '//input[@value="dbl click me"]')
        ac.double_click(btn).perform()

    def drag_and_drop(self):
        # 拖动
        self.driver.get('https://sahitest.com/demo/dragDropMooTools.htm')

        time.sleep(2)
        ac = ActionChains(self.driver)
        # 定位操作元素和目标元素
        source = self.driver.find_element(By.ID, 'dragger')
        target = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(7)')

        # 移动操作
        ac.drag_and_drop(source, target).perform()

    def move_to_element(self):
        # 访问目标网址
        self.driver.get('https://sahitest.com/demo/mouseover.htm')
        # 鼠标悬停
        time.sleep(2)
        ac = ActionChains(self.driver)
        btn = self.driver.find_element(By.CSS_SELECTOR, 'div > div')
        ac.move_to_element(btn).perform()

    def click_and_hold(self):
        # 按下鼠标
        # 访问目标网址
        # os.path.abspath(资源) : 获取资源的绝对路径

        url = 'file://' + os.path.join(os.path.abspath('html'), 'mouse_hold.html')
        self.driver.get(url)

        # 创建ac对象
        ac = ActionChains(self.driver)
        btn = self.driver.find_element(By.ID, 'btn1')
        ac.click_and_hold(btn).perform()

    def quit(self, num=2):
        time.sleep(num)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.click()
    # case.context_click()
    # case.double_click()
    # case.drag_and_drop()
    # case.move_to_element()
    case.click_and_hold()
    case.quit(10)

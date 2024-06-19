"""
显式等待针对某一个元素或者条件，结合webdriverwait和excepted_conditions类设置显示等待
webdriverwait ----设置超时时间、轮询间隔，结合until和until_not使用
excepted_conditions----条件函数，例如元素是否存在DOM树、是否可见等
         presence_of_element_located(locator)   判断元素是否在dom树中（是否存在于页面上）
         visibility_of_element_located(locator)   判断 元素是否可见
         visibility_of(webelement对象)          判断元素是否加载到页面并且可见
         title_is("内容")                  判断页面的标题是否为指定的字符串
         title_contains("内容")           判断页面标题模糊匹配给定的字符串
         text_to_be_present_in_element_value(locator,text)   判断某个元素的text文本是否包含预期的字符串


"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Select():
    def __init__(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.baidu.com/")
        global wait
        wait = WebDriverWait(driver, 10, 1)

    def fangwen_baidu(self):
        # 第一个参数是driver对象，第二个参数是最长超时时间，第三个参数是轮询的间隔时长（默认是0.5s）
        locator = (By.ID, "kw")
        # TODO 1
        kw = wait.until(EC.presence_of_element_located(locator), "元素在页面不存在，定位不到")
        kw.send_keys("成都天气预报")
        time.sleep(2)
        print("kw的值为：", kw)

    def select_baidu(self):
        try:
            locator = (By.ID, "kw1")
            # TODO 2
            kw = wait.until(EC.visibility_of_element_located(locator))
            # 如果元素可见，再进行下一步操作
            kw.send_keys("成都天气预报")
            time.sleep(2)
            print(kw.get_attribute("class"))
        except Exception as e:
            print("元素没有定位到，抛出异常信息：", e)

    def chaxun_baidu(self):
        kw = wait.until(EC.visibility_of(driver.find_element(By.ID, "kw")))
        print(driver.switch_to.active_element.get_attribute("class"))
        print(kw)

    def chaxun_baidu1(self):
        title = wait.until(EC.title_is("百度一下，你就知道"))
        print(title)  # 返回布尔值

    def chaxun_baidu2(self):
        title = wait.until(EC.title_contains("百度一下"))
        print(title)  # 返回布尔值

    def chaxun_baidu3(self):
        locator = (By.ID, "su")
        title = wait.until(EC.text_to_be_present_in_element_value(locator, "百度一下"))
        print(title)  # 返回布尔值


select = Select()
# select.select_baidu()
# select.chaxun_baidu()
# select.chaxun_baidu1()
# select.chaxun_baidu2()
select.chaxun_baidu3()
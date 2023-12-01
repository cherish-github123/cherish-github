import time

from selenium import webdriver

# 创建options对象,Options是chrome.options模块下面的一个类

options = webdriver.ChromeOptions()
# 为options对象添加手机配置
mobileEmulation = {"deviceName": 'iPhone 6'}
options.add_experimental_option('mobileEmulation', mobileEmulation)
# add_experimental是Options类上面的一个方法


# 打开浏览器,添加配置项
driver = webdriver.Chrome(options=options)
driver.get('https://www.baidu.com')
print(driver.get_window_size())   # 获取浏览器窗口大小
time.sleep(3)

# 退出浏览器
driver.quit()
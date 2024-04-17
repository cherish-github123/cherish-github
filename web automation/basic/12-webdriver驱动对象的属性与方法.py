import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器，返回webdriver对象
# driver: Webdriver的实例对象
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# print(driver)

# 打开新闻页面
# 定位新闻标签,打开一个新的窗口
time.sleep(1)
driver.find_element(By.LINK_TEXT, '新闻').click()

# TODO 1 ----------------常用属性------------------
# 浏览器名称
print(driver.name)
# 当前url
print(driver.current_url)
# 当前页面标题
print(driver.title)
# 获取网页源码
print(driver.page_source)

# 当前浏览器的所有窗口句柄
print(driver.window_handles)     # 百度首页通过“新闻”打开了两个窗口
# 获取当前窗口句柄
print(driver.current_window_handle)    # 鼠标停留的窗口还是百度首页的窗口

# TODO 2 --------------------常用方法------------------
# 浏览器后退
# driver.back()
# # 浏览器前进
# driver.forward()
# # 浏览器刷新
# driver.refresh()
# # 关闭当前窗口
# driver.close()
# # 退出浏览器
# driver.quit()
# # 最大化浏览器窗口
# driver.maximize_window()

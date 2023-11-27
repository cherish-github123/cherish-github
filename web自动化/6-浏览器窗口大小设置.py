from selenium import webdriver
import time

# 打开浏览器
driver = webdriver.Chrome()
time.sleep(2)

# 访问网址
driver.get('https://www.baidu.com')
# TODO 浏览器最大化
driver.maximize_window()
time.sleep(2)

# TODO 浏览器窗口大小自定义 480 * 800
driver.set_window_size(480, 800)
time.sleep(2)

# TODO 浏览器窗口最小化
driver.minimize_window()
time.sleep(2)

# 退出浏览器
driver.quit()
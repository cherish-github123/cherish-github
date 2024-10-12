import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element(By.LINK_TEXT,"网盘").click()
time.sleep(2)


windows_handles=driver.window_handles
print(windows_handles)
print(driver.current_window_handle)
driver.switch_to.window(windows_handles[1])
print(driver.current_window_handle)
print(driver.title)          # 切换到新窗口后，打印的标题是新窗口的标题

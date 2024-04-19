"""
alert警告框/用户确认

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

import time
full_path=r"E:\Git-project\cherish-github\web automation\file\Testing Alerts.html"
print(full_path)
driver=webdriver.Chrome()
driver.get(full_path)
time.sleep(3)
# TODO  -----------------------------------------alert弹窗---------------------
# driver.find_element(By.LINK_TEXT,"click me").click()
# # 切换到弹窗
# alert=driver.switch_to.alert
# # 获取弹窗的文本信息
# print(alert.text)
# # 点击确认按钮
# time.sleep(2)
# alert.accept()

# TODO  -----------------------------------------confirm弹窗---------------------
# driver.find_element(By.LINK_TEXT,"test confirm").click()
# confirm=driver.switch_to.alert
# print(confirm.text)
# time.sleep(2)
# 弹窗确认
# confirm.accept()
# 弹窗取消
# confirm.dismiss()


# TODO  -----------------------------------------prompt弹窗---------------------
driver.find_element(By.LINK_TEXT, "prompts happen").click()
prompt=driver.switch_to.alert
print(prompt.text)
time.sleep(2)
prompt.send_keys("fdheygf")
prompt.accept()
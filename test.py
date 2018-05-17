# coding=utf-8
from selenium import webdriver
import time

# 访问百度
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 获取百度搜索窗口句柄
search_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()
# 获取打开所有窗口句柄
all_handles = driver.window_handles
# 进入注册窗口
for handle in all_handles:
    if handle != search_windows:
        driver.switch_to_window(handle)
        print("now regester window")
        driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys('namejianjain')
        time.sleep(3)
for handle in all_handles:
    if handle == search_windows:
        driver.switch_to_window(handle)
        print("now search window")
        time.sleep(3)
        driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click()
        time.sleep(3)
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
        time.sleep(5)

driver.close()
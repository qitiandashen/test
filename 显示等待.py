# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver =webdriver.Chrome()
# 设置隐士等待
driver.implicitly_wait(10)
driver.get('http://member.fxqifu.com')
driver.maximize_window()
try:

    element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,'登录')))
    print(element)
finally:
    driver.quit()




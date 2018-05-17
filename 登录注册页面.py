from selenium import webdriver
import time
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://member.fxqifu.com/")
#获得当前页面的句柄
sreach_windows=driver.current_window_handle
print(sreach_windows)
#最大页面
driver.maximize_window()
#登录页面
driver.find_element_by_link_text('登录').click()
driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[1]').clear()
driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[1]').send_keys('18992582320')
driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[2]').clear()
driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[2]').send_keys("11111111")
driver.find_element_by_id('dologin').click()
#获得所有句柄
windows=driver.window_handles
#进入企业登录页面
driver.switch_to.window(windows[-1])
driver.find_element_by_xpath('//*[@id="app"]/div[3]/select/option[1]').click()
driver.find_element_by_xpath('//*[@id="login"]').click()
# 打印企业的title
title=driver.title
print(title)
# 打印企业的当前网址
url=driver.current_url
print(url)
# 打印企业的名称
name_c=driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/nav/ul/li[4]/div/label').text
print(name_c)
time.sleep(3)
# 进行企业的切换
above=driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/nav/ul/li[4]/div/label')
ActionChains(driver).move_to_element(above).perform()
driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/nav/ul/li[4]/ul/li[1]/a/label').click()
# 进行后退操作
driver.back()
# 进入应用
driver.find_element_by_xpath('//*[@id="side-menu"]/li[2]/a/span').click()
time.sleep(3)
# 设置显示等待
element=WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div[1]/div[1]/div[1]/div[1]'))
                                           )
print(element)
# 打印当前的url
url_1=driver.current_url
print(url_1)








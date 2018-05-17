#3.0会员登录
#coding == UTF-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.implicitly_wait(10)
#获得飞象企服的登录窗口句柄

driver.get("https://member.fxqifu.com/")
driver.maximize_window()
sreach_windows = driver.current_window_handle
print(sreach_windows)
driver.find_element_by_link_text('登录').click()
sreach_windows1=driver.current_window_handle
print(sreach_windows1)
all_handles=driver.window_handles

for handle in all_handles:
    if handle !=sreach_windows:
        driver.switch_to.window(handle)
print("登录公司")
time.sleep(5)

driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[1]').clear()
driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[1]').send_keys('18992582320')
driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[2]').clear()
driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[2]').send_keys("11111111")
driver.find_element_by_id('dologin').click()
time.sleep(5)
driver.quit()










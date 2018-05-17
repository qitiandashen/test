from selenium import webdriver
from public import login

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://member.fxqifu.com')
# 调用登录模块
login().user_login(driver)
# 进行应用操作
driver.find_element_by_xpath('//*[@id="side-menu"]/li[2]/a/span').click()
# 调用退出登录
login().user_logout(driver)
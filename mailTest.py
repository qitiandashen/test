from selenium import webdriver
from public import login
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.126.com")
#调用登录模块
login().user_login(driver)
#调用退出登录
login().user_logout(driver)
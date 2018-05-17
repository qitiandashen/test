from  selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# driver=webdriver.Chrome()
# 初始化配置
# 执行登录
def handlelogin():
    driver=webdriver.Chrome()
    usename='18992582320'
    password='11111111'
    url='https://member.fxqifu.com'
    driver.maximize_window()
    driver.get(url)
    cookie1=driver.get_cookies()
    print(cookie1)
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/a[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[1]').send_keys(usename)
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[2]').send_keys(password)
    cookie2=driver.get_cookies()
    print(cookie2)

    if cookie2==cookie1:
        print('登录失败了')
        time.sleep(3)
    else:
        element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="login"]')))
        print(element)






from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
# 登录
def login():
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/a[1]').click()
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[1]').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[1]').send_keys('18992582320')
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[2]').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[2]').send_keys('11111111')
    driver.find_element_by_xpath('//*[@id="dologin"]').click()
    """获得所有句柄"""
    windows=driver.window_handles
    """进入选择企业页面"""
    driver.switch_to.window(windows[-1])
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/select/option[1]').click()
    driver.find_element_by_xpath('//*[@id="login"]').click()
    """打印企业title"""
    title=driver.title
    print(title)
def logout():
    above = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/nav/ul/li[4]/div/label')
    ActionChains(driver).move_to_element(above).perform()
    driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/nav/ul/li[4]/ul/li[1]/a/label').click()
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://member.fxqifu.com')
# 调用登录模块
 login()
# 进入应用
driver.find_element_by_xpath('//*[@id="side-menu"]/li[2]/a/span').click()
logout()







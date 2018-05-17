class login():
    """登录"""
    def user_login(self,driver,username,password):
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/a[1]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[1]').clear()
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[1]').send_keys(username)
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[2]').clear()
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/input[2]').send_keys(password)
        driver.find_element_by_xpath('//*[@id="dologin"]').click()
        """获得所有句柄"""
        windows = driver.window_handles
        """进入选择企业页面"""
        driver.switch_to.window(windows[-1])
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/select/option[1]').click()
        driver.find_element_by_xpath('//*[@id="login"]').click()
    """退出"""
    def user_logout(self,driver):
        above = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/nav/ul/li[4]/div/label')
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/nav/ul/li[4]/ul/li[1]/a/label').click()
        driver.quit()

for handel in all_handles:
    if handel == sreach_windows:
        driver.switch_to.window(handle)
        print("now register member")
        driver.find_element_by_link_text("注册").click()
        driver.find_element_by_xpath("//input[@placeholder='请填写手机号']").send_keys("18667028576")

        driver.find_element_by_xpath("//button[@class='play']").click()
        time.sleep(10)
        print("please input secret")
        driver.find_element_by_xpath("//input[@placeholder='请填写验证码']").send_keys("")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("lk123456")
        driver.find_element_by_id("Button").click()





driver.find_element_by_id("login").click()
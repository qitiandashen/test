from selenium import webdriver
from public import login
class loginTest():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://member.fxqifu.com')
        self.driver.maximize_window()
    """刘慷账号登录"""
    def test_liukang_login(self):
        username='18992582320'
        password='11111111'
        login().user_login(self.driver,username,password)
        self.driver.quit()

    """刘小账号登录"""
    def test_liuxiao_login(self):
        username='18667028576'
        password='lk123456'
        login().user_login(self.driver,username,password)
        self.driver.quit()
loginTest().test_liukang_login()
loginTest().test_liuxiao_login()

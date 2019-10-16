from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from pages.login_pge import Login8
import time
import ddt   #调用ddt
import xlrd ##调用excel 数据读取模块
from selenium.webdriver.support.wait import WebDriverWait
testdates = [
    {"user":"test02","password":"test02#","asser":True},
    {"user":"test021","password":"test02#","asser":False}
] ###参数化

@ddt.ddt

class Login_pages_test(unittest.TestCase,Login8):
    @classmethod
    def setUpClass(cls) -> None:
        driver= webdriver.Chrome()
        cls.driver = driver
        cls.loginpa = Login8(cls.driver)
        cls.driver.get("http://118.31.187.124:81/zentao/user-login.html")
        time.sleep(3)
    def tearDown(self) -> None:
        time.sleep(4)
        self.driver.delete_all_cookies()
        self.driver.refresh()
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
    def login_case(self,user,password,asser):        ###写一个登陆类完成参数化
        self.input_user(user)
        self.input_password(password)
        self.click_login_button()

        result = self.get_login_name()
        self.assertIs(result, asser)

    @ddt.data(*testdates)   ### *传了三个字典过来
    def test_01(self,data):
       # data1 = testdates[0]
        self.login_case(data["user"],data["password"],data["asser"])

    # def test_02(self):
    #     data1 = testdates[1]
    #     self.login_case(data1["user"],data1["password"],data1["asser"])

if __name__ =="__main__":
    unittest.main()

    # lo1.test_01()
    # driver = webdriver.Chrome()
    # lo1 = Login8(driver)
    # driver.get("http://118.31.187.124:81/zentao/user-login.html")
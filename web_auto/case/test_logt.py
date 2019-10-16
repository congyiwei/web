from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from pages.login_pge import Login8
import time
from selenium.webdriver.support.wait import WebDriverWait

class Login_pages_test(unittest.TestCase,Login8):
    @classmethod
    def setUpClass(cls) -> None:
        driver= webdriver.Chrome()
        cls.driver = driver
        cls.loginpa = Login8(cls.driver)
        cls.driver.get("http://118.31.187.124:81/zentao/user-login.html")
        time.sleep(3)
    def tearDown(self) -> None:
        # self.driver.delete_all_cookies()
        self.driver.refresh()
    def test_06(self):
        self.input_user("test02")
        self.input_password("test02#")
        self.click_login_button()
        time.sleep(2)
        result = self.get_login_name()

        self.assertIs(result,True)
        print(result)

        def test_07(self):
            self.input_user("test021")
            self.input_password("test02#")
            self.click_login_button()
            time.sleep(2)
            result = self.get_login_name()

            self.assertIs(result, False)
            print(result)


if __name__ =="__main__":
    unittest.main()

    # lo1.test_01()
    # driver = webdriver.Chrome()
    # lo1 = Login8(driver)
    # driver.get("http://118.31.187.124:81/zentao/user-login.html")
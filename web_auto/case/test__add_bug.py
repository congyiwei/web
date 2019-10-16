import unittest
from pages.login_pge import Login8
from pages.add_bug import Add_bug_new
from selenium import webdriver
import time
my_dipan = "http://118.31.187.124:81/zentao/my/"

class Add_bug_test(unittest.TestCase,Add_bug_new):
        @classmethod
        def setUpClass(cls) -> None:
            cls.driver = webdriver.Chrome()
            cls.bug = Add_bug_new(cls.driver)
            a = Login8(cls.driver)
            a.login()

            time.sleep(5)
        def test_add_bug(self):

            title = "测试流程"
            self.bug.add_Bug(title)

            result =self.bug.is_add_bug_success(title)
            print(result)
            self.assertTrue(result)
            self.assertTrue(result)

        def setUp(self) -> None:
            self.driver.get(my_dipan)

        @classmethod
        def tearDownClass(cls) ->  None:
            cls.driver.quit()

if __name__=="——__main__":
    unittest.main()
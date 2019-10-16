from selenium import webdriver
from selenium.webdriver.common.by import By
from common.c2 import Lo
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#login_url ="http://118.31.187.124:81/zentao/user-login.html"

class Login8(Lo):
    loc1 = (By.ID, "account")
    loc2 = (By.NAME, "password")
    loc3 = (By.ID, "submit")
    #定位登陆
    #loc_get_user = (By.XPATH, "//*[@id=''']/li/a/span[1]")

    loc_get_user = (By.ID, "block40")
    def input_user(self,text):
        self.sendKeys(self.loc1,text)
    def input_password(self,password):
        self.sendKeys(self.loc2,password)
    def click_login_button(self):
        self.cliCK(self.loc3)

        #print(user)
    def login(self, user="test02", password="test02#"):
        ##登陆流程

        self.driver.get("http://118.31.187.124:81/zentao/user-login.html")
        self.input_user(user)
        self.input_password(password)
        self.click_login_button()
    def get_login_name(self):
        user = self.Isdisplayed(self.loc_get_user)
        return user
        #print(user)
    def get_login_result(self,text):
        result = self.is_text_in_element(self.loc_get_user,text)
        return result                                       #################判断值和预期结果
if __name__ =="__main__":
    driver=webdriver.Chrome()
    login_page = Login8(driver)
    login_page.login()
#     #driver.get("http://118.31.187.124:81/zentao/user-login-L3plbnRhby8=.html")
#     login_page.input_user("test02")
#     login_page.input_password("test02#")
#     login_page.click_login_button()
#     login_page.get_login_name()

    login_page.get_login_name()
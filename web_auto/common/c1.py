from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from common.c2 import Lo
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Bug_new(Lo):
    #定位登陆
    loc1 = (By.ID, "account")
    loc2 = (By.NAME, "password")
    loc3 = (By.ID, "submit")
    #定位bug
    loc_ceshi = (By.XPATH,"//*[@id='navbar']/ul/li[4]/a")
    loc_Bug = (By.XPATH,"//*[@id='subNavbar']/ul/li[1]/a")
    loc_addBug = (By.XPATH,"//*[@id='mainMenu']/div[3]/a[3]")
    loc_xiangmu = (By.XPATH,"//*[@id='project_chosen']/a")
    loc_xiangmu1 = (By.LINK_TEXT,"Pyc2.0")
    loc_mokuai = (By.XPATH,"//*[@id='module_chosen']/a")
    loc_mokuai1 = (By.LINK_TEXT,"/注册模块")
    loc_banben = (By.XPATH,"//*[@id='openedBuild_chosen']/ul")
    loc_banben1 = (By.XPATH,"//*[@id='openedBuild_chosen']/div/ul/li")
    loc_date = (By.ID,"deadline")
    loc_date1 = (By.LINK_TEXT,"13")
    loc_zhipai = (By.ID,"assignedTo_chosen")
    loc_zhipai1 = (By.XPATH,"//*[@id='assignedTo_chosen']/a/span")
    loc_title = (By.ID,"title")
    #需要切换frame
    loc_body = (By.CLASS_NAME,"article-content")
    loc_baocun =(By.ID,"submit")
    loc_queren = (By.XPATH,"//*[@id='bugList']/tbody/tr[1]/td[3]/a")

    # def __init__(self,driver:webdriver.Chrome()):
    #     self.driver = driver
    #     self.lo = Lo(self.driver)



    def add_Bug(self,title):
        self.cliCK(self.loc_ceshi)
        self.cliCK(self.loc_Bug)
        self.cliCK(self.loc_addBug)
        # self.cliCK(self.loc_xiangmu)
        # self.cliCK(self.loc_xiangmu1)
        # self.cliCK(self.loc_mokuai)
        # self.cliCK(self.loc_mokuai1)
        self.cliCK(self.loc_banben)
        self.cliCK(self.loc_banben1)
        # self.cliCK(self.loc_date)
        # self.cliCK(self.loc_date1)
        # self.cliCK(self.loc_zhipai)
        # self.cliCK(self.loc_zhipai1)
        self.sendKeys(self.loc_title,title)
        body = '''
        步骤1
        步骤2
        步骤3。。
        
        预期结果。。。
        。。。
        实际结果。。。
        。。。
               '''
        self.driver : webdriver.Chrome
        self.driver.switch_to_frame(0)
        self.sendKeys(self.loc_body,body)
        self.driver.switch_to_default_content()
        self.cliCK(self.loc_baocun)






if __name__=="__main__":
    driver = webdriver.Chrome()
    driver.get("http://118.31.187.124:81/zentao/user-login-L3plbnRhby8=.html")
    bug = Bug_new(driver)
    bug.Login()
    title = "测试流程"
    bug.add_Bug(title)
    result = bug.is_text_in_element(title)
    print(result)









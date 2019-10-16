###############二次封装
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait           ###新的等待时间调用的类
import time
from selenium.webdriver.common.by import By           ###########新的封装方法
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
# driver.find_element(By.ID,"account")
# driver.find_element(By.NAME,"password")  ##根据 by方法来的
#locator = (By,"value")          ###使用* 将locator 中的两个值 当成一个值传入到函数中
from selenium.webdriver.common.action_chains import ActionChains ###鼠标悬停
class Lo():
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
       # self.timeout = 10
    def findElement(self,locator):
        ele = WebDriverWait(self.driver,10).until(lambda x: x.find_element(*locator))    ####30是默认超时时间   默认每间隔0.5秒检查一次元素
                  ####30是默认超时时间   默认每间隔0.5秒检查一次元素
        return ele
#element = WebDriverWait(driver, ,timeout).until(lambda x: x.find_element_by_id("kw"))
  ##返回的是element 元素对象                 #x 是从dirver传过来的 就是dirver
    def sendKeys(self,locator,text):
        ele =self.findElement(locator)
        ele.send_keys(text)
    def cliCK(self,locator):
        ele =self.findElement(locator)
        ele.click()
    def Select(self,locator):                    #############查找复选框 单选框 是否被选中
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r
    def Isdisplayed(self,locator):           ###########查找元素是否存在
        try:
            ele = self.findElement(locator)
            return True
        except:
            return False
    def is_text_in_element(self,locator,_text):
        try:
            result = WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    def clear(self,locator):
        ele = self.findElement(locator)
        ele.clear()
    def get_text(self,locator):
        #获取文本
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("获取text失败，返回''")
            return ""
    # def is_aert_exist(self):
    #     try:
    #         time.sleep(2)
    #         alert = self.driver.switch_to_alert
    #         text =alert.text
    #         alert.accept()
    #         return text
    #     except:
    #         return ""
    def move_to_element(self,locator):
        ###鼠标悬停
        driver: webdriver.Chrome
        ele = self.findElement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def select_by_index(self,locator,index=0):      ##封装select方法
        ##通过索引 index是索引第几个 从0开始默认选第一个
        ele =self.findElement(locator)    ##定位到select这个元素
        Select(ele).select_by_index(index)
        ele.click()
    def select_by_value(self,locator,value):
        ##通过value属性定位
        ele = self.findElement(locator)
        Select(ele).select_by_value(locator)
    def select_by_text(self,locator,text):
        ##通过文本值定位
        ele =self.findElement(locator)
        Select(ele).select_by_visible_text(text)

    ###########  js操作右侧滚动条
    def js_seroll_end(self):
        #滚动到底部
        js_heig = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js_heig)

    def js_fours(self,locator):
###聚焦元素 （滚动滚动条）
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)
    def js_scroll_top(self):
#回到顶部
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)



if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://118.31.187.124:81/zentao/user-login.html")
    lo = Lo(driver)
    loc1=(By.ID,"account")
    loc2=(By.NAME,"password")
    loc3=(By.ID,"submit")
    lo.sendKeys(loc1,"test02")
    lo.sendKeys(loc2,"test02#")
    lo.cliCK(loc3)



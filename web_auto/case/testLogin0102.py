#1功能用例
#自动化用例
#
#unittest
#脚本实现
#assert断言
#
#测试执行 __name__ 和__main__
#python 单元测试框架  保证代码是干净的 是通过的
#python 单元测试框架  unittest     pytest
#自动化用例一定要详细                        期望结果
#用例怎么写：   1打开浏览器
                # 2打开网址                 登陆成功后 页面有XXX存在
#               3输入账号 xx                           判断登陆成功的标准有多个
                # 4输入密码 xxx
                # 5点击登陆
###############################################错误用例就写输入错的帐号密码等  判断页面xx不存在

# 一个功能点 输入项不同 可以写一个模块  比如登陆
#        编号    前置条件           操作步骤          测试输入    检查点               后置条件
#        01                        用户名输入框       admin       页面包含用
# 登陆           打开浏览器          密码输入框        123456     户名admin文本       退出登录
#                 打开网址xxx         登陆按钮         click
#                                 用户名输入框         admin1      页面不包含用       关闭浏览器
#       02                          密码输入框        111111       户名admin文本    （后置是为了不影响下一个用例执行）
#                                     登陆按钮        click

#################################################################################################################################
#每条用例设计必须是独立的 单独拿出来可以运行 不依赖其他用例
#一个功能点的相同操作（只是输入参数不一样 ），可以归为一个类
#一个类里面输入不同参数的操作 可以为一个测试点
#每个用例都有（非必须）前置条件  （如果没有可以写pass）
#每个用例都有（非必须）后置条件  （如果没有可以写pass）
#每个testcase 都必须有断言（Assert）

from  selenium import webdriver
import time
import unittest   #########导入unittest方法

class LoginTest(unittest.TestCase):

    # def setUp(self) -> None:             #每个用例执行前都执行一次
    #     self.driver = webdriver.Chrome()      #将drive变成全局变量
    #     self.driver.get("http://118.31.187.124:81/zentao/user-login-L3plbnRhby8=.html")
    def tearDown(self) -> None:          #每个用例结束后都执行一次
         self.driver.delete_all_cookies()  #因为登陆后存在cookies  我们在这里给他清除掉 就自动退出登录了
         self.driver.refresh()        #清空 cookies 之后 刷新页面
    @classmethod                    #classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
    def setUpClass(cls) -> None:        #所有用例前只执行一次
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://118.31.187.124:81/zentao/user-login-L3plbnRhby8=.html")
        #     pass
    # def tearDownClass(cls) -> None:         #所有用例结束后只执行一次
    #     pass
    def login(self,user,password):
        self.driver.find_element_by_id("account").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id("submit").click()
    def test_01(self):
        time.sleep(2)
        self.login("test02","test02#")
        #判断是否登录成功
        time.sleep(2)
        t=self.driver.find_element_by_class_name("user-name").text
       # print(t)
        self.assertTrue(t =='test02')     #断言返回结果

    def test_02(self):
        time.sleep(2)
        self.login("test02","test2#")
        a = self.driver.switch_to.alert       # 进入alert模式
        text =a.text
        # 判断是否登录成功

        #e = self.driver.find_element_by_class_name("user-name").text
        self.assertIn(text,"登录失败，请检查您的用户名或密码是否填写正确。") #断言失败截图
        a.accept()
        # print(t)








if __name__=="__main__":      #如果模块是直接被执行 __name__的值位__main__   如果模块被导入__name的值为模块名字
    unittest.main()               #加了这一条保证了 以后在其他模块中调用这个模块里面的函数时 不会去执行脚本
#######################################断言
        # self.assertEqual(a,b)  #判断a==b
        # self.assertNotEqual(a,b)  #判断 a !=b
        # self.assertTrue(a == b) #判断布尔值 x is True
        # self.assertFalse(a == b)# 判断 x is False
        # self.assertIsNone(x) #判断是否为空 x is none
        # self.assertIsNotNone(x)# 判断 x is not  none
        # self.assertIn(a,b)  #判断 a 在b 里面
        # self.assertNotIn(a,b) #判断a 不在b 里面

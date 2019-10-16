##发送文本 .val()
##点击 .click()   语法$  这里是css selector语法

from selenium import  webdriver
import time

driver = webdriver.Chrome()
driver.get("http://118.31.187.124:81/zentao/user-login-L3plbnRhby9idWctY3JlYXRlLTEtMC1tb2R1bGVJRD0wLmh0bWw=.html")
#输入帐号
username = "$('#account').val('test02')"
driver.execute_script(username)

# clear = "$('#account').val('')"      ###清空文本
# driver.execute_script(clear)
##输入密码
psw = "$('.table > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)').val('test02#')"
driver.execute_script(psw)

button = "$('#submit').click()"
driver.execute_script(button)


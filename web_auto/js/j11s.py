from selenium import webdriver
driver = webdriver.Chrome()
##富文本
from pages.login_pge import Login8
###js语法
# document.getElementsByClassName("class属性")[0].contentWindow.document.body.innerHtml="hello word"       ##定位iframe  点后面的是进入iframe
                            #定位iframe            #切换到ifram                    #定位富文本标签      ##输入内容
a = Login8(driver)
a.login()

##打开编辑页面

driver.get("http://118.31.187.124:81/zentao/bug-create-1-0-moduleID=0.html")
body = "hello word"
js = 'document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML="%s"'%body
driver.execute_script(js)                                                               ##%s 就是helloword 因为getaway参数化了所以需要使用

#driver.quit()

#document.getElementById("iframe的id").contentWindow.document.getElementById("元素的id")    ####通用方法
#############################定位其他的元素   id等
#document.getElementById("元素的id").value= "test02"   ###定位元素并输入内容
#document.getElementsByName("元素的id")[0].value= "test02"  ###name定位只有elements 方法  因为是复数所以要用下标来取值
#document.getElementById("元素的id").click()  点击元素    多行使用；分号隔开

#document.getElementsByTagName("tag")[0].click()   获取的是多个 通过标签名选取元素
# document.getElementsByClassName("ke-edit-iframe")[0]   获取的是多个 通过class name选取元素
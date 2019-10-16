from selenium import webdriver
import time

driver =webdriver.Chrome()
driver.get("https://www.12306.cn/index/")
time.sleep(5)
# e1 = '''document.getElementById("train_date").removeAttribute("readonly");    ##去除readonly的属性值 因为如果有这个值会无法输入
#     document.getElementById("train_date").value= "2019-05-22"'''  ##通过修改value值来修改日期框中的内容
# driver.execute_script(e1)
# time.sleep(5)
#
# driver.quit()
##########################多行用 ''' 三引号  两个js语句直接用分号隔开   因为这个例子这里没有readonly属性 所以报错 去除第一句可正常运行
#################################第二种方法  先清空 再输入 但是要清空readonly值
# time.sleep(5)
# e = 'document.getElementById("train_date").removeAttribute("readonly")'
# driver.execute_script(e)
# time.sleep(3)
# driver.find_element("id","train_date").clear()
# driver.find_element("id","train_date").send_keys("2019-01-1")
# time.sleep(5)
# driver.quit()
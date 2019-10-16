#####用 discover  方法 搜索所有test用例
import  unittest
import HTMLTestRunner_cn
casePath = "D:\\PyCharm 2019.2.3\\web_auto1\\case"       ##用例的路径
rule = "test*.py"         #匹配规则
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
reportPath ="D:\\PyCharm 2019.2.3\\web_auto1\\report\\"+"report.html"         #放报告的路径
fp = open(reportPath,"wb")      #打开这个路径  wb必须要我也不知道为什么
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="报告的title",description="Login报告")

runner.run(discover) #运行
fp.close()

####################open 读文件
# f = open("电脑绝对路径","r")  r是读的意思
# fp1 = f.read()
# f.close()
# f1 = open("电脑绝对路径","w")  w是写入的意思
# f1.write("")
# f1.close()
# f1 = open("电脑绝对路径","a") a是追加写入的意思

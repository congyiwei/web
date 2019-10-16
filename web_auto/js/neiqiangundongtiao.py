 ##先定位div的位置  滚动条所在的那个框的位置
 ##再通过 scrollTop  和 scrollLeft 方法控制进度

############在这里 10000代表移动岛底部  0代表在开头  Top是上下滚动
js = 'document.getElementByid("su").scrollTop=10000'


#########横向滚动  在这里获取的class那么是多个值  取list的第一个对象
js = 'document.getElementByClassName("sususu")[0].scrollLeft=10000'

##############有时候click事件会失效 比如点击百度设置的保存设置按钮
###########1 先点击父元素，找回焦点   用js去执行点击保存设置事件
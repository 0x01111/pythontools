# -*- coding: UTF-8 -*-

# 中文英文字符串，分成单字

s = u'字符串'
L= []
for ch in s:
	L.append(ch)

print L
text='魏和河'
text = unicode(text, 'utf-8')
for i in text:
    print i

x = '下面通过Python将文本中的中文部分提取出来进行需要的处理'
text = unicode(x, 'utf-8')
for i in text:
    print i



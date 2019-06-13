#coding=utf-8

import re
import sys
reload(sys)
sys.setdefaultencoding("utf8")

def translate(str):
    line = str.strip().decode('utf-8', 'ignore')  # 处理前进行相关的处理，包括转换成Unicode等
    p2 = re.compile(ur'[^\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
    zh = p2.split(line)
    p3 = re.compile(ur'[\u4e00-\u9fa5]')
    en = p3.split(line)
    zh_en = zh + en
    return zh_en
str = "line = str.strip().decode('utf-8', 'ignore')  # 处理前进行相关的处理，包括转换成Unicode等"

res = translate(str)

print str
print ','.join(res)

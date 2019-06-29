#!/usr/bin/env python
# coding=utf-8
import os
import sys
import string
import json
import datetime

time_stamp = datetime.datetime.now()  + datetime.timedelta(days=2)

time_stamp = datetime.date(2018, 12, 30)

num2chn = {1:"一", 2:"二",3:"三",4:"四",5:"五",6:"六",0:"日"}


def printDay(delta):
    date = time_stamp + datetime.timedelta(days=delta)
    str = "# 周"
    w = date.strftime('%w')
    d = date.strftime('%m.%d')
    str = str + num2chn[int(w)] + " " + d
    str = str + "\n" + "工作： " + "\n\n" + "\t1.x" + "\n" + "\t2.x\n"
    return str

def printWeek(delta):
    start = (time_stamp + datetime.timedelta(days=delta-7)).strftime("%m.%d")
    end = (time_stamp + datetime.timedelta(days=delta)).strftime("%m.%d")
    W = (time_stamp + datetime.timedelta(days=delta)).strftime('%W')
    y = (time_stamp + datetime.timedelta(days=i)).strftime("%Y")
    str = "" ##"### " + y + " 第" + W  + "周." + start + "-"+ end
    str = str + "\n### 【本周计划】" + "\n### 【本周总结】" + "\n### 【下周计划】"
    return str

str = ""
for i in range(1,366):
    str =  str + printDay(i) + "\n"
    if i%7 == 0:
        str += printWeek(i) + "\n" + "\n"
        print str
        start = (time_stamp + datetime.timedelta(days=i - 7)).strftime("%m.%d")
        end = (time_stamp + datetime.timedelta(days=i)).strftime("%m.%d")
        W = (time_stamp + datetime.timedelta(days=i)).strftime('%W')
        y = (time_stamp + datetime.timedelta(days=i)).strftime("%Y")
        file_name = y + " 第" + W  + "周."+start + "-" + end + ".md"
        file_name  = "/Users/youdao/" + file_name

        f = open(file_name, "w")
        f.write("%s\n" % (str))
        f.close()
        str = ""




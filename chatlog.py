#coding=utf8
import os
import random
import time

#print time.time()

print time.strftime("%Y/%m/%d %H:%M:%S")
print time.strftime("%M")
flag = True
while True:
    if flag & (int(time.strftime("%M")) == 9):
        strdate = time.strftime("%Y/%m/%d %H:%M:%S")
        print (u'当前时间：%s' % strdate)
        flag = False
        time.sleep(0.1)


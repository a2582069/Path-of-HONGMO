#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
@author hongmo

%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''
import urllib2
import re
import requests
import threading
import time
#预处理
usr_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = {'User-Agent':usr_agent}
gz = 'online":(\w*),'
gzx = 'href="/(\w*)"'
patten = re.compile(gz)
pattenx = re.compile(gzx)
url = 'http://open.douyucdn.cn/api/RoomApi/room/{}'
urlx = 'https://www.douyu.com/directory/all?page={}&isAjax=1'
urlex = [urlx.format(xx)for xx in range(1,10)]

#多线程操作

def plus_it(number,ren):
    request = urllib2.Request(url=urlex[number],headers=headers)
    response = urllib2.urlopen(request)
    content = response.read()
    items = re.findall(pattenx,content)
    for item in items:
        urlxx = url.format(item)
        html = requests.get(urlxx, headers=headers).text
        ansx = re.findall(patten,html)
        if ansx:
            ren = ren+int(ansx[0])
    print "第"+str(number)+"页有："+str(ren)+"人"

def gettime():
    m = time.strftime("%M", time.localtime())
    s = time.strftime("%S", time.localtime())
    x = int(m)*60+int(s)
    return x
if __name__ == "__main__":
    renx = [0,0,0,0,0,0,0,0,0,0,0,0]
    t = gettime()
    for i in range(0,9):
        t1 = threading.Thread(target=plus_it,args=(i,renx[i]))
        t1.start()
    t = gettime() - t
    print t
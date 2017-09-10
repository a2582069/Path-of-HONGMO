#!/usr/bin/env python
#coding:utf-8
'''
@author hongmo
'''

import urllib
import urllib2
import re
url = 'https://www.qiushibaike.com/textnew/page/3/'
for i in range(0,9):
    a = url
    strinfo = re.compile('3')
    b = strinfo.sub(str(i), a)
    print b
    usr_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    headers = {'User-Agent':usr_agent}
    request = urllib2.Request(url=b,headers=headers)
    response = urllib2.urlopen(request)
    content = response.read()
    gz = '<div class="content">\n*<span>(.*)</span>\n(.*)\n*</div>'
    patten = re.compile(gz)
    items = re.findall(patten,content)
    e = 1
    for item in items:
        print e
        e = e + 1
        print item[0]

#!/usr/bin/env python
#coding:utf-8
'''
@author hongmo
'''

import urllib
import urllib2
import re
url = 'http://www.txt53.com/read/41206_1.html'
url2 = 'http://www.txt53.com/html/xuanhuan/list_21_1.html'
gz = '<div id="view_content_txt">([\s\S]*)<div class="view_page">'
gz1 = '<ul>\n.*<li class="qq_a">(.*)</li>\n.*<li class="qq_l">(.*)</li>\n.*<li class="qq_m">(.*)</li>\n.*<li class="qq_r">(.*)</li>\n.*<li class="qq_g"><a href="(.*)">.*</a></li>\n.*<li class="qq_j">([\s\S]*)<li class="qq_z">.*html">(.*)</a>.*\n*.*</ul>'
gzt = '<li class="qq_g"><a href="(.*)">《(.*)》TXT下载</a></li>'
patten = re.compile(gz)
patten1 = re.compile(gzt)
usr_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = {'User-Agent': usr_agent}
e = 1
for page in range(1,348):
    url3 = url2[:43] + str(page) + url2[44:]
    print url3
    request = urllib2.Request(url=url3,headers=headers)
    response = urllib2.urlopen(request)
    content = response.read()
    items = re.findall(patten1,content)

    for item in items:
       print e
       e = e + 1
       print item[1]
       print item[0]
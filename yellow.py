#!/usr/bin/env python
#coding:utf-8
'''
@author hongmo
2017
9
2
'''

from urllib import urlretrieve
import urllib2
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


usr_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = {'User-Agent': usr_agent}

# request header and user_agent confirm


url0 = 'http://qq1110.com/art-detail-id-{}-pg-.html'
#{} -> ID
url1 = 'http://qq1110.com/art-type-id-9-pg-{}.html'
#{} -> pageNum
url2 = 'http://qq1110.com/art-type-id-1-pg-{}.html'
#{112} -> pageNum
url3 = 'http://qq1110.com/art-detail-id-{}-pg-.html'
#{} -> ID

gz0 = 'detail-id-(.*)-pg.*>【(.*)】'
gz1 = '0000ff><BR>.*\n*.*字数：\d*.*'
gz2 = 'id-(\w*)-pg-.html">\n(.*)</a>'
gz3 = 'src="([^ "]*.jpg)'
patten0 = re.compile(gz0)
patten1 = re.compile(gz1)
patten2 = re.compile(gz2)
patten3 = re.compile(gz3)

# re

def get_content(url):
    request = urllib2.Request(url=url,headers=headers)
    response = urllib2.urlopen(request)
    content = response.read()
    return content


def txt_write(name,content):
    filee = 'C:\\Users\\hm\\Desktop\\xiaoshuo\\{}.txt'
    filename = filee.format(name)
    f = open(filename.decode('utf-8'),'w')
    f.write(content)
    f.close()

def tp_write(name,content):
    filee = 'C:\\Users\\hm\\Desktop\\tp\\{}.jpg'
    filename = filee.format(name)
    f = open(filename.decode('utf-8'),'w+b')
    f.write(content)
    f.close()


def get_xs():
    urlx = [url1.format(xx)for xx in range(1,143)]
    num = 1
    for urlex in urlx:
        items = re.findall(patten0, get_content(urlex))
        for item in items:
            items0 = re.findall(patten1, get_content(url0.format(item[0])))
            num = num + 1
            try:
                print "num. " + str(num) + " xs"
                txt_write(str(num) + item[1], items0[0])
            except:
                print "error and next is"

def get_tp():
    urlx = [url2.format(xx)for xx in range(1,112)]
    num = 1
    pnum = 1
    for urlex in urlx:
        items = re.findall(patten2, get_content(urlex))
        for item in items:
            cont = get_content(url3.format(item[0]))
            print item[0]
            contx = re.findall(gz3,cont)
            for conto in contx:
                print conto
                try:
                    request = urllib2.Request(url=conto, headers=headers)
                    response = urllib2.urlopen(request)
                    content = response.read()
                    tp_write(item[1]+str(pnum), content)
                except:
                    print 'error'
                pnum = pnum + 1
            pnum = 1



if __name__ == '__main__':

    #get_xs()
    get_tp()
    #




#!/usr/bin/env python
# -*-coding:utf-8-*-
'''

make by homgmo
version v0.1
2017/8/14

'''
import ssl
import urllib2
from json import loads
ssl._create_default_https_context = ssl._create_unverified_context

login = 'https://kyfw.12306.cn/otn/login/init'




def getList():
    html = urllib2.urlopen('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-08-14&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT').read()
    dict = loads(html)
    return dict['data']['result']

if __name__ == '__main__':
    for i in getList():
        temp_list = i.split('|')
        for e in temp_list:
            print e
        break
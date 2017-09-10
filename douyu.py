#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
@author hongmo

%y ��λ������ݱ�ʾ��00-99��
%Y ��λ������ݱ�ʾ��000-9999��
%m �·ݣ�01-12��
%d �����е�һ�죨0-31��
%H 24Сʱ��Сʱ����0-23��
%I 12Сʱ��Сʱ����01-12��
%M ��������00=59��
%S �루00-59��
%a ���ؼ���������
%A ����������������
%b ���ؼ򻯵��·�����
%B �����������·�����
%c ������Ӧ�����ڱ�ʾ��ʱ���ʾ
%j ���ڵ�һ�죨001-366��
%p ����A.M.��P.M.�ĵȼ۷�
%U һ���е���������00-53��������Ϊ���ڵĿ�ʼ
%w ���ڣ�0-6����������Ϊ���ڵĿ�ʼ
%W һ���е���������00-53������һΪ���ڵĿ�ʼ
%x ������Ӧ�����ڱ�ʾ
%X ������Ӧ��ʱ���ʾ
%Z ��ǰʱ��������
%% %�ű���
'''
import urllib2
import re
import requests
import threading
import time
#Ԥ����
usr_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = {'User-Agent':usr_agent}
gz = 'online":(\w*),'
gzx = 'href="/(\w*)"'
patten = re.compile(gz)
pattenx = re.compile(gzx)
url = 'http://open.douyucdn.cn/api/RoomApi/room/{}'
urlx = 'https://www.douyu.com/directory/all?page={}&isAjax=1'
urlex = [urlx.format(xx)for xx in range(1,10)]

#���̲߳���

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
    print "��"+str(number)+"ҳ�У�"+str(ren)+"��"

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
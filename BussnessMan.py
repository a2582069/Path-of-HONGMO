#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
@author hongmo
'''
tonghuo = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

huilv1 = [2 ,12,1 ,11,10,6 ,7 ,14,17,3 ,15]
huilv2 = [12,1 ,11,10,7 ,7 ,14,17,3 ,15,16]
huilv3 = [1 ,2 ,4 ,1 ,4 ,3 ,2 ,4 ,4 ,7 ,3 ]

dashi1 = [14 ,7  ,10 ,1  ,12 ,2  ,8  ,12]
dashi2 = [17 ,14 ,7  ,11 ,1  ,12 ,7  ,1 ]
dashi3 = [3.2,1.6,3.2,3.2,1.6,0.8,2.4,1.6]


# 2 -> 1        x / 3 = y

tonghuo_name = ['����ʯ','���ʯ','�ɱ�ʯ',
                'ĥ��ʯ','����Ƭ','��ɫʯ',
                '����ʯ','����ʯ','��ʥʯ',
                '����ʯ','����ʯ','���ʯ',
                '����ʯ','����ʯ','���;�',
                '��ʶ��','����ʯ']


pressure0 = [0.25,1,3,8,8,64,64,32]
pressure1 = [0.25,0.8,]
pressure2 = []
def chu(c,b):
    if (c/b) > 0:
        if (c/b%1) > 0:
            return c/b - (c/b%1)
        else:
            return c/b
    else:
        return -1


def exchange_1(tonghuo,a,geshu):
    if geshu == 0:
        return 0

#ee = 0
#for uu in tonghuo_name:
   # print str(uu) + ":" + str(tonghuo[ee])
   # ee = ee + 1

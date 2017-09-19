#!/usr/bin/env python
# coding:utf-8
'''
@author hongmo
'''

from Tkinter import *
import requests
import datetime
import threading
import time
html = 'http://www.dd373.com/s/49pbxm-0-0-0-0-0-{}-0-0-0-0-su-0-512-0.html'
htm = [
'f25596',
't3avtw',
'sqsr19',
'gscbm2',
'ukt4je',
'7tc0uu',
'c0tvxw',
'1r08bv',
'bk757e',
'3j8k7e',
'rfre7m',
'xd80r6',
'f1kmbb',
'f69b9c',
'ubhcwh',
'5mhjef',
'fnm1qf',
'ncr2rs',
'g9x8rm',
'eqaqwg',
'2vxgnm',
'9t3pgk',
'6rqkrf',
'24kv9p',
't2m8c2',
]
th_ex0 = [0,0,  8,3,2,  1,  32,0,  64,0,64,8,0,0,0,0,0]
th_ex1 = [0,0,6.4,0,0,0.8,25.6,0,51.2,0,00,0,0,0,0,0,0]
htm_name=[
'崇高',
'混沌',
'连接',
'幻色',
'工匠',
'改造',
'重铸',
'神圣',
'点金',
'制图',
'后悔',
'机会',
'银币',
'富豪',
'瓦尔',
'棱镜',
'魔镜',
'高点',
'箱石',
'远古',
'先驱',
'剥离',
'平行',
'镜片',
'六分',
]
htm_name_en=[
'cg',
'hd',
'lj',
'hs',
'gj',
'gz',
'cz',
'ss',
'dj',
'zt',
'hh',
'jh',
'yb',
'fh',
'we',
'lj',
'mj',
'gd',
'xs',
'yg',
'xq',
'bl',
'px',
'jp',
'lf',
]
html_list = [html.format(ht)for ht in htm]

usr_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = {'User-Agent':usr_agent}
gz = '<p>([\d|.]*).[^span]*</p>'
gzx = 'href="/(\w*)"'
pattern = re.compile(gz)
patternx = re.compile(gzx)

def get_price(html,n):
    content = requests.get(url=html, headers=headers).text
    contentx = re.findall(pattern, content)
    #print content
    print 'get' + str(n) + 'price' + '\n'

    i = 0
    e = 0
    for index in contentx:
        i = i + 1
        #print i
        #print '\n'
        if index != '':
            e = e + float(index)
        else:
            i = i - 1
        if i == 2:
            e = e / i
            return e
    #print e


mwindow = Tk()
mwindow.geometry('600x1000')
frm1 = Frame(mwindow,bg = 'yellow',height = 300)
frm2 = Frame(mwindow,bg = 'green',height = 300)
frm3 = Frame(mwindow,bg = 'blue',height = 200)
frm4 = Frame(mwindow,height = 300)
frm5 = Frame(mwindow,height = 300)
frm6 = Frame(mwindow,height = 300)
def cmd1():
    numj = 0
    threads = []
    for enti in enty_list:
        enti.delete(0,100)
        enti.insert(0,str(get_price(html_list[numj],numj)))
        numj = numj+1
        time.sleep(3)
    time.sleep(60)

    nowtime = datetime.datetime.now()
    nowtime.strftime('%Y-%m-%d %H %M %S')
    nowtimex = str(nowtime)[0:19] + '\n'
    textrm.insert(1.0,nowtimex)
def cmd2():
    i = 0
    if entz1.get()!= '':
        i = i + float(entz1.get()) * float(enty1.get())
        entyy1.delete(0, 100)
        entyy1.insert(1, str(float(entz1.get()) * float(enty1.get())))
        print i
    if entz2.get()!= '':
        i = i + float(entz2.get()) * float(enty2.get())
        entyy2.delete(0, 100)
        entyy2.insert(1, str(float(entz2.get()) * float(enty2.get())))
        print i
    if entz3.get()!= '':
        i = i + float(entz3.get()) * float(enty3.get())
        entyy3.delete(0, 100)
        entyy3.insert(1, str(float(entz3.get()) * float(enty3.get())))
        print i
    if entz4.get()!= '':
        i = i + float(entz4.get()) * float(enty4.get())
        entyy4.delete(0, 100)
        entyy4.insert(1, str(float(entz4.get()) * float(enty4.get())))
        print i
    if entz5.get()!= '':
        i = i + float(entz5.get()) * float(enty5.get())
        entyy5.delete(0, 100)
        entyy5.insert(1, str(float(entz5.get()) * float(enty5.get())))
        print i
    if entz6.get()!= '':
        i = i + float(entz6.get()) * float(enty6.get())
        entyy6.delete(0, 100)
        entyy6.insert(1, str(float(entz6.get()) * float(enty6.get())))
        print i
    if entz7.get()!= '':
        i = i + float(entz7.get()) * float(enty7.get())
        entyy7.delete(0, 100)
        entyy7.insert(1, str(float(entz7.get()) * float(enty7.get())))
        print i
    if entz8.get()!= '':
        i = i + float(entz8.get()) * float(enty8.get())
        entyy8.delete(0, 100)
        entyy8.insert(1, str(float(entz8.get()) * float(enty8.get())))
        print i
    if entz9.get()!= '':
        i = i + float(entz9.get()) * float(enty9.get())
        entyy9.delete(0, 100)
        entyy9.insert(1, str(float(entz9.get()) * float(enty9.get())))
        print i
    if entz9.get()!= '':
        i = i + float(entz9.get()) * float(enty9.get())
        entyy9.delete(0, 100)
        entyy9.insert(1, str(float(entz9.get()) * float(enty9.get())))
        print i
    if entz10.get()!= '':
        i = i + float(entz10.get()) * float(enty10.get())
        entyy10.delete(0, 100)
        entyy10.insert(1, str(float(entz10.get()) * float(enty10.get())))
        print i
    if entz11.get()!= '':
        i = i + float(entz11.get()) * float(enty11.get())
        entyy11.delete(0, 100)
        entyy11.insert(1, str(float(entz11.get()) * float(enty11.get())))
        print i
    if entz12.get()!= '':
        i = i + float(entz12.get()) * float(enty12.get())
        entyy12.delete(0, 100)
        entyy12.insert(1, str(float(entz12.get()) * float(enty12.get())))
        print i
    if entz13.get()!= '':
        i = i + float(entz13.get()) * float(enty13.get())
        entyy13.delete(0, 100)
        entyy13.insert(1, str(float(entz13.get()) * float(enty13.get())))
        print i
    if entz14.get()!= '':
        i = i + float(entz14.get()) * float(enty14.get())
        entyy14.delete(0, 100)
        entyy14.insert(1, str(float(entz14.get()) * float(enty14.get())))
        print i
    if entz15.get()!= '':
        i = i + float(entz15.get()) * float(enty15.get())
        entyy15.delete(0, 100)
        entyy15.insert(1, str(float(entz15.get()) * float(enty15.get())))
        print i
    if entz16.get()!= '':
        i = i + float(entz16.get()) * float(enty16.get())
        entyy16.delete(0, 100)
        entyy16.insert(1, str(float(entz16.get()) * float(enty16.get())))
        print i
    if entz17.get()!= '':
        i = i + float(entz17.get()) * float(enty17.get())
        entyy17.delete(0, 100)
        entyy17.insert(1, str(float(entz17.get()) * float(enty17.get())))
        print i
    if entz18.get()!= '':
        i = i + float(entz18.get()) * float(enty18.get())
        entyy18.delete(0, 100)
        entyy18.insert(1, str(float(entz18.get()) * float(enty18.get())))
        print i
    if entz19.get()!= '':
        i = i + float(entz19.get()) * float(enty19.get())
        entyy19.delete(0, 100)
        entyy19.insert(1, str(float(entz19.get()) * float(enty19.get())))
        print i
    if entz20.get()!= '':
        i = i + float(entz20.get()) * float(enty20.get())
        entyy20.delete(0, 100)
        entyy20.insert(1, str(float(entz20.get()) * float(enty20.get())))
        print i
    if entz21.get()!= '':
        i = i + float(entz21.get()) * float(enty21.get())
        entyy21.delete(0, 100)
        entyy21.insert(1, str(float(entz21.get()) * float(enty21.get())))
        print i
    if entz22.get()!= '':
        i = i + float(entz22.get()) * float(enty22.get())
        entyy22.delete(0, 100)
        entyy22.insert(1, str(float(entz22.get()) * float(enty22.get())))
        print i
    if entz23.get()!= '':
        i = i + float(entz23.get()) * float(enty23.get())
        entyy23.delete(0, 100)
        entyy23.insert(1, str(float(entz23.get()) * float(enty23.get())))
        print i
    if entz24.get()!= '':
        i = i + float(entz24.get()) * float(enty24.get())
        entyy24.delete(0, 100)
        entyy24.insert(1, str(float(entz24.get()) * float(enty24.get())))
        print i
    if entz25.get()!= '':
        i = i + float(entz25.get()) * float(enty25.get())
        entyy25.delete(0, 100)
        entyy25.insert(1, str(float(entz25.get()) * float(enty25.get())))
        print i
    entex.delete(0,100)
    entex.insert(1,str(i))

def cmd3():
    i = 0
    for name in htm_name_en:
        filename = str(i)+name
        path = 'C:\Users\cg\Desktop\shangren\{}.txt'
        path = path.format(filename)
        #print name
        #print path
        nowtime = datetime.datetime.now()
        nowtime.strftime('%Y-%m-%d %H %M %S')
        nowtimex = str(nowtime)[0:19]
        fp = open(path , 'a')
        fp.write(str(nowtimex) + '    ')
        content = enty_list[i].get()
        fp.write(content)
        print enty_list[i].get()
        fp.write('\n')
        fp.close()
        i = i + 1
def cmd4():
    while(True):
        cmd1()
        cmd3()
entz1 = Entry(frm1,width = 7)
entz2 = Entry(frm1,width = 7)
entz3 = Entry(frm1,width = 7)
entz4 = Entry(frm1,width = 7)
entz5 = Entry(frm1,width = 7)
entz6 = Entry(frm1,width = 7)
entz7 = Entry(frm1,width = 7)
entz8 = Entry(frm1,width = 7)
entz9 = Entry(frm1,width = 7)
entz10 = Entry(frm1,width = 7)
entz11 = Entry(frm1,width = 7)
entz12 = Entry(frm1,width = 7)
entz13 = Entry(frm1,width = 7)
entz14 = Entry(frm1,width = 7)
entz15 = Entry(frm1,width = 7)
entz16 = Entry(frm1,width = 7)
entz17 = Entry(frm1,width = 7)
entz18 = Entry(frm1,width = 7)
entz19 = Entry(frm1,width = 7)
entz20 = Entry(frm1,width = 7)
entz21 = Entry(frm1,width = 7)
entz22 = Entry(frm1,width = 7)
entz23 = Entry(frm1,width = 7)
entz24 = Entry(frm1,width = 7)
entz25 = Entry(frm1,width = 7)

enty1 = Entry(frm2,width = 7)
enty2 = Entry(frm2,width = 7)
enty3 = Entry(frm2,width = 7)
enty4 = Entry(frm2,width = 7)
enty5 = Entry(frm2,width = 7)
enty6 = Entry(frm2,width = 7)
enty7 = Entry(frm2,width = 7)
enty8 = Entry(frm2,width = 7)
enty9 = Entry(frm2,width = 7)
enty10 = Entry(frm2,width = 7)
enty11 = Entry(frm2,width = 7)
enty12 = Entry(frm2,width = 7)
enty13 = Entry(frm2,width = 7)
enty14 = Entry(frm2,width = 7)
enty15 = Entry(frm2,width = 7)
enty16 = Entry(frm2,width = 7)
enty17 = Entry(frm2,width = 7)
enty18 = Entry(frm2,width = 7)
enty19 = Entry(frm2,width = 7)
enty20 = Entry(frm2,width = 7)
enty21 = Entry(frm2,width = 7)
enty22 = Entry(frm2,width = 7)
enty23 = Entry(frm2,width = 7)
enty24 = Entry(frm2,width = 7)
enty25 = Entry(frm2,width = 7)

entyy1 = Entry(frm5,width = 7)
entyy2 = Entry(frm5,width = 7)
entyy3 = Entry(frm5,width = 7)
entyy4 = Entry(frm5,width = 7)
entyy5 = Entry(frm5,width = 7)
entyy6 = Entry(frm5,width = 7)
entyy7 = Entry(frm5,width = 7)
entyy8 = Entry(frm5,width = 7)
entyy9 = Entry(frm5,width = 7)
entyy10 = Entry(frm5,width = 7)
entyy11 = Entry(frm5,width = 7)
entyy12 = Entry(frm5,width = 7)
entyy13 = Entry(frm5,width = 7)
entyy14 = Entry(frm5,width = 7)
entyy15 = Entry(frm5,width = 7)
entyy16 = Entry(frm5,width = 7)
entyy17 = Entry(frm5,width = 7)
entyy18 = Entry(frm5,width = 7)
entyy19 = Entry(frm5,width = 7)
entyy20 = Entry(frm5,width = 7)
entyy21 = Entry(frm5,width = 7)
entyy22 = Entry(frm5,width = 7)
entyy23 = Entry(frm5,width = 7)
entyy24 = Entry(frm5,width = 7)
entyy25 = Entry(frm5,width = 7)

lab1 = Label(frm4,text = htm_name[0])
lab2 = Label(frm4,text = htm_name[1])
lab3 = Label(frm4,text = htm_name[2])
lab4 = Label(frm4,text = htm_name[3])
lab5 = Label(frm4,text = htm_name[4])
lab6 = Label(frm4,text = htm_name[5])
lab7 = Label(frm4,text = htm_name[6])
lab8 = Label(frm4,text = htm_name[7])
lab9 = Label(frm4,text = htm_name[8])
lab10 = Label(frm4,text = htm_name[9])
lab11 = Label(frm4,text = htm_name[10])
lab12 = Label(frm4,text = htm_name[11])
lab13 = Label(frm4,text = htm_name[12])
lab14 = Label(frm4,text = htm_name[13])
lab15 = Label(frm4,text = htm_name[14])
lab16 = Label(frm4,text = htm_name[15])
lab17 = Label(frm4,text = htm_name[16])
lab18 = Label(frm4,text = htm_name[17])
lab19 = Label(frm4,text = htm_name[18])
lab20 = Label(frm4,text = htm_name[19])
lab21 = Label(frm4,text = htm_name[20])
lab22 = Label(frm4,text = htm_name[21])
lab23 = Label(frm4,text = htm_name[22])
lab24 = Label(frm4,text = htm_name[23])
lab25 = Label(frm4,text = htm_name[24])

enty_list = [
        enty1,
        enty2,
        enty3,
        enty4,
        enty5,
        enty6,
        enty7,
        enty8,
        enty9,
        enty10,
        enty11,
        enty12,
        enty13,
        enty14,
        enty15,
        enty16,
        enty17,
        enty18,
        enty19,
        enty20,
        enty21,
        enty22,
        enty23,
        enty24,
        enty25,
    ]
entz_list = [

        entz1,
        entz2,
        entz3,
        entz4,
        entz5,
        entz6,
        entz7,
        entz8,
        entz9,
        entz10,
        entz11,
        entz12,
        entz13,
        entz14,
        entz15,
        entz16,
        entz17,
        entz18,
        entz19,
        entz20,
        entz21,
        entz22,
        entz23,
        entz24,
        entz25,
    ]
entyy_list = [
        entyy1,
        entyy2,
        entyy3,
        entyy4,
        entyy5,
        entyy6,
        entyy7,
        entyy8,
        entyy9,
        entyy10,
        entyy11,
        entyy12,
        entyy13,
        entyy14,
        entyy15,
        entyy16,
        entyy17,
        entyy18,
        entyy19,
        entyy20,
        entyy21,
        entyy22,
        entyy23,
        entyy24,
        entyy25,
    ]
entex = Entry(frm3,text = '9',width = 10)
button1 = Button(frm3,text = '刷新',command = cmd1,height = 1)
button2 = Button(frm3,text = '计算',command = cmd2,height = 1)
button3 = Button(frm3,text = '持续性保存',command = cmd4,height = 1)
button4 = Button(frm3,text = '保存',command = cmd3,height = 1)

entz1 .place(x = 10,y = 20)
entz2 .place(x = 10,y = 50)
entz3 .place(x = 10,y = 80)
entz4 .place(x = 10,y = 110)
entz5 .place(x = 10,y = 140)
entz6 .place(x = 10,y = 170)
entz7 .place(x = 10,y = 200)
entz8 .place(x = 10,y = 230)
entz9 .place(x = 10,y = 260)
entz10.place(x = 10,y = 290)
entz11.place(x = 10,y = 320)
entz12.place(x = 10,y = 350)
entz13.place(x = 10,y = 380)
entz14.place(x = 10,y = 410)
entz15.place(x = 10,y = 440)
entz16.place(x = 10,y = 470)
entz17.place(x = 10,y = 500)
entz18.place(x = 10,y = 530)
entz19.place(x = 10,y = 560)
entz20.place(x = 10,y = 590)
entz21.place(x = 10,y = 620)
entz22.place(x = 10,y = 650)
entz23.place(x = 10,y = 680)
entz24.place(x = 10,y = 710)
entz25.place(x = 10,y = 740)

enty1 .place(x = 10,y = 20)
enty2 .place(x = 10,y = 50)
enty3 .place(x = 10,y = 80)
enty4 .place(x = 10,y = 110)
enty5 .place(x = 10,y = 140)
enty6 .place(x = 10,y = 170)
enty7 .place(x = 10,y = 200)
enty8 .place(x = 10,y = 230)
enty9 .place(x = 10,y = 260)
enty10.place(x = 10,y = 290)
enty11.place(x = 10,y = 320)
enty12.place(x = 10,y = 350)
enty13.place(x = 10,y = 380)
enty14.place(x = 10,y = 410)
enty15.place(x = 10,y = 440)
enty16.place(x = 10,y = 470)
enty17.place(x = 10,y = 500)
enty18.place(x = 10,y = 530)
enty19.place(x = 10,y = 560)
enty20.place(x = 10,y = 590)
enty21.place(x = 10,y = 620)
enty22.place(x = 10,y = 650)
enty23.place(x = 10,y = 680)
enty24.place(x = 10,y = 710)
enty25.place(x = 10,y = 740)

entyy1 .place(x = 10,y = 20)
entyy2 .place(x = 10,y = 50)
entyy3 .place(x = 10,y = 80)
entyy4 .place(x = 10,y = 110)
entyy5 .place(x = 10,y = 140)
entyy6 .place(x = 10,y = 170)
entyy7 .place(x = 10,y = 200)
entyy8 .place(x = 10,y = 230)
entyy9 .place(x = 10,y = 260)
entyy10.place(x = 10,y = 290)
entyy11.place(x = 10,y = 320)
entyy12.place(x = 10,y = 350)
entyy13.place(x = 10,y = 380)
entyy14.place(x = 10,y = 410)
entyy15.place(x = 10,y = 440)
entyy16.place(x = 10,y = 470)
entyy17.place(x = 10,y = 500)
entyy18.place(x = 10,y = 530)
entyy19.place(x = 10,y = 560)
entyy20.place(x = 10,y = 590)
entyy21.place(x = 10,y = 620)
entyy22.place(x = 10,y = 650)
entyy23.place(x = 10,y = 680)
entyy24.place(x = 10,y = 710)
entyy25.place(x = 10,y = 740)

lab1 .place(x = 10,y = 20)
lab2 .place(x = 10,y = 50)
lab3 .place(x = 10,y = 80)
lab4 .place(x = 10,y = 110)
lab5 .place(x = 10,y = 140)
lab6 .place(x = 10,y = 170)
lab7 .place(x = 10,y = 200)
lab8 .place(x = 10,y = 230)
lab9 .place(x = 10,y = 260)
lab10.place(x = 10,y = 290)
lab11.place(x = 10,y = 320)
lab12.place(x = 10,y = 350)
lab13.place(x = 10,y = 380)
lab14.place(x = 10,y = 410)
lab15.place(x = 10,y = 440)
lab16.place(x = 10,y = 470)
lab17.place(x = 10,y = 500)
lab18.place(x = 10,y = 530)
lab19.place(x = 10,y = 560)
lab20.place(x = 10,y = 590)
lab21.place(x = 10,y = 620)
lab22.place(x = 10,y = 650)
lab23.place(x = 10,y = 680)
lab24.place(x = 10,y = 710)
lab25.place(x = 10,y = 740)

textrm = Text(frm6)
entex.place(x = 110,y = 70)
frm1.place(width = 75,height = 800)
frm2.place(x = 75,width = 75,height = 800)
frm3.place(x = 0,y = 800,width = 300,height = 300)
frm5.place(x = 150,width = 75,height = 800)
frm4.place(x = 225,width = 75,height =800)
frm6.place(x = 300,width = 300,height = 800)
textrm.place(x = 50,y = 50,width = 200,height = 100)
button1.place(x = 50,y = 30)
button2.place(x = 50,y = 90)
button3.place(x = 200,y = 30)
button4.place(x = 200,y = 90)
mwindow.mainloop()
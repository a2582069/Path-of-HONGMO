#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
@author hongmo
'''

from Tkinter import *
import requests

html = 'http://www.dd373.com/s/49pbxm-0-0-0-0-0-t3avtw-0-0-0-0-su-0-512-0.html'
html1= 'http://www.dd373.com/s/49pbxm-0-0-0-0-0-f25596-0-0-0-0-su-0-512-0.html'
html2= 'http://www.dd373.com/s/49pbxm-0-0-0-0-0-sqsr19-0-0-0-0-su-0-512-0.html'
html3= 'http://www.dd373.com/s/49pbxm-0-0-0-0-0-gscbm2-0-0-0-0-su-0-512-0.html'
html4= 'http://www.dd373.com/s/49pbxm-0-0-0-0-0-ukt4je-0-0-0-0-su-0-512-0.html'
html5= 'http://www.dd373.com/s/49pbxm-0-0-0-0-0-7tc0uu-0-0-0-0-su-0-512-0.html'
html6= 'http://www.dd373.com/s/49pbxm-0-0-0-0-0-5mhjef-0-0-0-0-su-0-512-0.html'
html7= 'http://www.dd373.com/s/49pbxm-0-0-0-0-0-f1kmbb-0-0-0-0-su-0-512-0.html'

usr_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = {'User-Agent':usr_agent}
gz = '<p>([\d|.]*).[^span]*</p>'
gzx = 'href="/(\w*)"'
pattern = re.compile(gz)
patternx = re.compile(gzx)

def get_price(html):
    content = requests.get(url=html, headers=headers).text
    contentx = re.findall(pattern, content)
    i = 0
    e = 0
    for index in contentx:
        i = i + 1
        if index != '':
            e = e + float(index)
        #print index
    e = e / i
    return e

mwindow = Tk()
mwindow.geometry('300x500')
frm1 = Frame(mwindow,bg = 'yellow',height = 300)
frm2 = Frame(mwindow,bg = 'green',height = 300)
frm3 = Frame(mwindow,bg = 'blue',height = 200)
frm4 = Frame(mwindow,height = 300)
frm5 = Frame(mwindow,height = 300)
def cmd1():
    enty1.delete(0,100)
    enty1.insert(0,get_price(html))
    enty2.delete(0,100)
    enty2.insert(0,get_price(html1))
    enty3.delete(0,100)
    enty3.insert(0,get_price(html2))
    enty4.delete(0,100)
    enty4.insert(0,get_price(html3))
    enty5.delete(0,100)
    enty5.insert(0,get_price(html4))
    enty6.delete(0,100)
    enty6.insert(0,get_price(html5))
    enty7.delete(0,100)
    enty7.insert(0,get_price(html6))
    enty8.delete(0,100)
    enty8.insert(0,get_price(html7))
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
    entex.delete(0,100)
    entex.insert(1,str(i))


entz1 = Entry(frm1,width = 7)
entz2 = Entry(frm1,width = 7)
entz3 = Entry(frm1,width = 7)
entz4 = Entry(frm1,width = 7)
entz5 = Entry(frm1,width = 7)
entz6 = Entry(frm1,width = 7)
entz7 = Entry(frm1,width = 7)
entz8 = Entry(frm1,width = 7)

enty1 = Entry(frm2,width = 7)
enty2 = Entry(frm2,width = 7)
enty3 = Entry(frm2,width = 7)
enty4 = Entry(frm2,width = 7)
enty5 = Entry(frm2,width = 7)
enty6 = Entry(frm2,width = 7)
enty7 = Entry(frm2,width = 7)
enty8 = Entry(frm2,width = 7)

entyy1 = Entry(frm5,width = 7)
entyy2 = Entry(frm5,width = 7)
entyy3 = Entry(frm5,width = 7)
entyy4 = Entry(frm5,width = 7)
entyy5 = Entry(frm5,width = 7)
entyy6 = Entry(frm5,width = 7)
entyy7 = Entry(frm5,width = 7)
entyy8 = Entry(frm5,width = 7)

lab1 = Label(frm4,text = 'Chaos')
lab2 = Label(frm4,text = 'Ex')
lab3 = Label(frm4,text = 'Link')
lab4 = Label(frm4,text = 'Color')
lab5 = Label(frm4,text = 'Gongjiang')
lab6 = Label(frm4,text = 'Change')
lab7 = Label(frm4,text = 'Mirrow')
lab8 = Label(frm4,text = 'Sliver Coin')


entex = Entry(frm3,text = '9',width = 10)
button1 = Button(frm3,text = 'get',command = cmd1,height = 1)
button2 = Button(frm3,text = 'put',command = cmd2,height = 1)
entz1.place(x = 10,y = 20)
entz2.place(x = 10,y = 50)
entz3.place(x = 10,y = 80)
entz4.place(x = 10,y = 110)
entz5.place(x = 10,y = 140)
entz6.place(x = 10,y = 170)
entz7.place(x = 10,y = 200)
entz8.place(x = 10,y = 230)

enty1.place(x = 10,y = 20)
enty2.place(x = 10,y = 50)
enty3.place(x = 10,y = 80)
enty4.place(x = 10,y = 110)
enty5.place(x = 10,y = 140)
enty6.place(x = 10,y = 170)
enty7.place(x = 10,y = 200)
enty8.place(x = 10,y = 230)

entyy1.place(x = 10,y = 20)
entyy2.place(x = 10,y = 50)
entyy3.place(x = 10,y = 80)
entyy4.place(x = 10,y = 110)
entyy5.place(x = 10,y = 140)
entyy6.place(x = 10,y = 170)
entyy7.place(x = 10,y = 200)
entyy8.place(x = 10,y = 230)

lab1.place(x = 10,y = 20)
lab2.place(x = 10,y = 50)
lab3.place(x = 10,y = 80)
lab4.place(x = 10,y = 110)
lab5.place(x = 10,y = 140)
lab6.place(x = 10,y = 170)
lab7.place(x = 10,y = 200)
lab8.place(x = 10,y = 230)

entex.place(x = 110,y = 80)
frm1.place(width = 75,height = 300)
frm2.place(x = 75,width = 75,height = 300)
frm3.place(x = 0,y = 300,width = 300,height = 300)
frm5.place(x = 150,width = 75,height = 300)
frm4.place(x = 225,width = 75,height =300)
button1.place(x = 50,y = 30)
button2.place(x = 200,y = 30)
mwindow.mainloop()

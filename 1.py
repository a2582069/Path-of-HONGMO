#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
@author hongmo
'''

from Tkinter import *
import requests

html = 'http://www.dd373.com/s/49pbxm-0-0-0-0-0-t3avtw-0-0-0-0-su-0-512-0.html'
usr_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = {'User-Agent':usr_agent}
gz = '<p>(\d\.\d\d).*</p>'
gzx = 'href="/(\w*)"'
pattern = re.compile(gz)
patternx = re.compile(gzx)

content = requests.get(url= html,headers = headers).text

contentx = re.findall(pattern,content)
i = 0
e = 0
for index in contentx:
    i = i+1
    e = e + float(index)
    print index
e = e / i
print e

mwindow = Tk()
mwindow.geometry('300x250')
frm1 = Frame(mwindow,bg = 'yellow',height = 300)
frm2 = Frame(mwindow,bg = 'green',height = 300)
frm3 = Frame(mwindow,bg = 'blue',height = 200)
def cmd1():
    i = 0
    ent5.delete(0,10)
    ent5.insert(0,e)
    if ent1.get()!= '':
        i = i + float(ent1.get()) * float(ent5.get())
    if ent2.get()!= '':
        i = i + float(ent2.get()) * float(ent6.get())
    if ent3.get()!= '':
        i = i + float(ent3.get()) * float(ent7.get())
    if ent4.get()!= '':
        i = i + float(ent4.get()) * float(ent8.get())
    entex.delete(0,10)
    entex.insert(1,str(i))


ent1 = Entry(frm1,text = '0',width = 7)
ent2 = Entry(frm1,text = '1',width = 7)
ent3 = Entry(frm1,text = '2',width = 7)
ent4 = Entry(frm1,text = '3',width = 7)
ent5 = Entry(frm2,text = '4',width = 7)
ent6 = Entry(frm2,text = '5',width = 7)
ent7 = Entry(frm2,text = '6',width = 7)
ent8 = Entry(frm2,text = '7',width = 7)
entex = Entry(frm3,text = '9',width = 10)
button1 = Button(frm3,text = 'press',command = cmd1,height = 1)

ent1.place(x = 10,y = 20)
ent2.place(x = 10,y = 50)
ent3.place(x = 10,y = 80)
ent4.place(x = 10,y = 110)
ent5.place(x = 10,y = 20)
ent6.place(x = 10,y = 50)
ent7.place(x = 10,y = 80)
ent8.place(x = 10,y = 110)
entex.place(x = 120,y = 40)

frm1.place(width = 150,height = 200)
frm2.place(x = 150,width = 150,height = 200)
frm3.place(x = 0,y = 150,width = 300,height = 300)
button1.place(x = 135,y = 10)

mwindow.mainloop()
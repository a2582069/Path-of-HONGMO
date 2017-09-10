#!/usr/bin/env python
#coding:utf-8
'''
@author hongmo
'''

from Tkinter import *
import requests


s1  = 0
s11 = 0



mainw = Tk()
txt = Text(mainw)
w = Checkbutton(mainw,text = '123')
w.place(x = 0)
txt.place(y = 30 ,width = 100,height = 100)




mainw.mainloop()
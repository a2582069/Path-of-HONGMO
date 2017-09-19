__author__ = 'cg'
#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
@author hongmo
'''

from Tkinter import *
import requests

mainw = Tk()
ent1 = Entry(mainw,width = 10)
ent2 = Entry(mainw,width = 10)
ent3 = Entry(mainw,width = 10)
ent_list = [ent1,ent2,ent3]

ent_list[1].place(x = 1,y = 1)
mainw.geometry('1000x1000')
mainw.mainloop()
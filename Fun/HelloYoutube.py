#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window, bg="black", bd=5, relief=SUNKEN)
frame.place(x=60, y=60)

Button(frame, text="W", font=("Consolas", 25), bg='light green').pack(side=TOP)
Button(frame, text="A", font=("Consolas", 25), bg='light green').pack(side=LEFT)
Button(frame, text="S", font=("Consolas", 25), bg='light green').pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 25), bg='light green').pack(side=LEFT)




window.mainloop()

#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    time_label.after(1000, update)




window = Tk()

time_label = Label(window, font=("Arial", 50), fg="green", bg="black")
time_label.pack()

day_label = Label(window, font=("Ink Free", 25), fg="black", bg="white")
day_label.pack()

date_label = Label(window, font=("Ink Free", 30), fg="black", bg="white")
date_label.pack()

update()

window.mainloop()

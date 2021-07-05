#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    print(color)
    colorHex = (color[1])
    window.config(bg=colorHex)#change background

window = Tk()
window.geometry("420x420")
button = Button(text='click me', command=click)
button.pack()
window.mainloop()

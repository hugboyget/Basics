#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-100)
def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+100)
def move_left(event):
    label.place(x=label.winfo_x() - 100, y=label.winfo_y())
def move_right(event):
    label.place(x=label.winfo_x() + 100, y=label.winfo_y())

window = Tk()
window.geometry("500x500")
window.config(bg="white")

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)


myimage = PhotoImage(file='plain.png')
label = Label(window, image=myimage, bg='white')
label.place(x=0, y=0)

window.mainloop()
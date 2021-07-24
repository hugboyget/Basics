#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *

def move_up(event):
    canvas.move(myimage, 0, -100)
def move_down(event):
    canvas.move(myimage, 0, 100)
def move_left(event):
    canvas.move(myimage, -100, 0)
def move_right(event):
    canvas.move(myimage, 100, 0)

window = Tk()

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

photoimage = PhotoImage(file='plain.png')
myimage = canvas.create_image(0, 0, image=photoimage, anchor=NW)


window.mainloop()
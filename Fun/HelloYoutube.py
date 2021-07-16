#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *

def doSomething(event):
    #print("dit a thing")
    print("Hello. !")
    print("You did a thing:", str(event.x)+","+str(event.y))
    label.config(text=event.keysym)

window = Tk()

#window.bind("<Key>", doSomething)
window.bind("<Button-1>", doSomething)#mouse left click
window.bind("<Button-2>", doSomething)#scroll wheel
window.bind("<Button-3>", doSomething)#right mouse click
window.bind("<Leave>", doSomething)#leave the window
window.bind("<Enter>", doSomething)#Enter the window
window.bind("<Motion>", doSomething)#where the mouse moved
label = Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()
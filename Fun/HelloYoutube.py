#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *

def doSomething(event):
    print("You did a thing:" + str(event.x) + "," + str(event.y))

window = Tk()

window.bind("<Button-1>", doSomething) #left mouse click
#window.bind("<Button-2>", doSomething) #scroll whell
#window.bind("<Button-3>", doSomething) #right mouse click
#window.bind("<ButtonRealease>", doSomething)
window.bind("<Enter>", doSomething) #enter the window
window.bind("<Leave>", doSomething) #leave the window
window.bind("<Motion>", doSomething) #Where the mouse moved




window.mainloop()
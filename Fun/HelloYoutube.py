#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm



from tkinter import *

def create_window():
    #Tk() = new independent window
    #Toplevel = new window 'on top' of other windows
    new_window = Tk()
    old_window.destroy()

old_window = Tk()
Button(old_window, text="new a window", command=create_window).pack()

old_window.mainloop()

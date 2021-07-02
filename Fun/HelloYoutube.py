#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *

window = Tk() #instantiate an instance of a window

window.geometry("490x490")
window.title("Bro Code first GUI program")

icon = PhotoImage(file="lo.gif")# PhotoImage图片必须gif格式
window.iconphoto(True, icon)
window.config(background="black")

window.mainloop() #place window on computer screen. listen for events


#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *

def display():
    if x.get() == "YES":
        print("you agree !")
    else:
        print("you don't agree:(")


window = Tk()

x = StringVar()

love_photo = PhotoImage(file='icon_love.png')

check_button = Checkbutton(window,
                           text="I agree with you.",
                           variable=x,
                           onvalue="YES",
                           offvalue="NO",
                           command=display,
                           font=('Arial', 20),
                           fg='red',
                           bg='black',
                           activeforeground='black',#点击时的颜色变化
                           activebackground='red',
                           padx=25,
                           pady=25,
                           bd=20,
                           image=love_photo,
                           compound='left')

check_button.pack()
window.mainloop()


#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count += 1
    print(count)
    print("You clicked the button !")

window = Tk()

photo = PhotoImage(file='icon_love.png')


button = Button(window,
                text='click me !',
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                #state=DISABLED,
                image=photo,
                compound='top')
button.pack()

window.mainloop()


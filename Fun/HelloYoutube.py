#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *

#entry widget = textbox that accept a signal line of user input

def submit():
    username = entry.get()
    print("hello " + username)


def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=("Arial", 50),
              bg="pink",
              )


#entry.config(state=DISABLED) #禁止输入
#entry.config(show="*") #隐藏显示
entry.insert(0, 'Spongebob') #默认值
entry.pack(side=LEFT)

submit_button = Button(window, text="submit", command=submit, bg="green")
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete, bg="red")
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace, bg="yellow")
backspace_button.pack(side=RIGHT)

window.mainloop()


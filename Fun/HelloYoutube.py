#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *

#grid() = geometry manager that organizes widgets in a table-like structure in a parent

window = Tk()

titleLabel = Label(window, text="Enter your info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window, text="First name:", width=20, bg="red").grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window, text="Last name:", width=20, bg="blue").grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)

emailNameLabel = Label(window, text="Email:", width=20, bg="pink").grid(row=3, column=0)
emailNameEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)

window.mainloop()



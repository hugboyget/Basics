#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

# text widget = funtions like a text area, you can enter multiple lines of text
from tkinter import *

def submit():
    input = text.get("1.0", END)
    print(input)

window = Tk()

text = Text(window,
            bg="light green",
            font=("Ink Free", 25),
            height=8,
            width=20)
text.pack()

button = Button(window, text="submit", command=submit)
button.pack()



window.mainloop()
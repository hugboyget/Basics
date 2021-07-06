#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="E:\\PYTHON\Basics\\Fun",
                                          title="Open a file okay?",
                                          filetypes=(("text files", "*.txt"),
                                          ("all files", "*.*"))
                                          )

    file = open(filepath, 'r')
    print(file.read())

window = Tk()

button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()

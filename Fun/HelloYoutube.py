#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="E:\\PYTHON\\Basics\\Fun",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ]
                                    )
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    #filetext = input("Enter some words to save:") # enter in Console
    file.write(filetext)
    file.close

window = Tk()

button = Button(text='save', command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()
#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm



from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that manges a collection of windows/displays
tab1 = Frame(notebook) # new frame for tabl
tab2 = Frame(notebook) # new frame for tab2

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")
#expand = expand to fill any space not otherwise
#fill = fill space on x and y axis

Label(tab1, text="this is tab#1", width=60, height=20).pack()
Label(tab2, text="this is tab#2", width=60, height=20).pack()
window.mainloop()

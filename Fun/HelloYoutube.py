#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *

window = Tk()

photo = PhotoImage(file='lo.gif')


#label = an area widget that holds text and/or an image within a window

label = Label(window,
              text="Hello World !",
              font=('Arial', 40, 'bold'),
              fg='#00FF00',
              background='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top')
label.pack()
#label.place(x=100, y=100)

window.mainloop()

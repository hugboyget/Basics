#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

# radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get()) + " degrees C")


window = Tk()



hotImage = PhotoImage(file='hot.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()



scale = Scale(window,
              from_=100,
              to=-20,
              length=500,
              orient=VERTICAL, #垂直方向
              font=('Consolas', 25),
              tickinterval=10, #刻度
              #showvalue=0, #隐藏
              resolution=5, #增量(解析度)
              troughcolor='yellow',#底色
              fg='red',
              bg='black'
              )
#scale.set(10) #默认值
scale.set((scale['from']-scale['to'])/2+scale['to'])
scale.pack()


coldImage = PhotoImage(file='cold.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()


button = Button(window, text="submit", command=submit)
button.pack()




window.mainloop()


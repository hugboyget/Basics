#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
canvas.create_line(0, 0, 500, 500, fill="blue", width="5")
canvas.create_line(0, 500, 500, 0, fill="red", width="10")
canvas.create_rectangle(20, 20, 250, 250, fill="pink")
canvas.create_polygon(250, 0, 500, 500, 0, 500, fill="green", outline="black", width=5)
points = [250, 0, 500, 500, 0, 500]
canvas.create_polygon(points, fill="yellow", outline="black", width=5)
canvas.create_arc(0, 0, 200, 200, fill="green", style=PIESLICE, start=45, extent=180)
canvas.create_arc(0, 0, 500, 500, fill="red", extent=180, start=0, width=10)
canvas.create_arc(0, 0, 500, 500, fill="white", extent=180, start=180, width=10)
canvas.create_oval(190, 190, 310, 310, fill="white", width=10)
canvas.pack()

window.mainloop()



#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 600
HEIGHT = 600

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
window.update()
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 1, 1, "red")
tennis_ball = Ball(canvas, 0, 0, 50, 4, 3, "yellow")
basket_ball = Ball(canvas, 0, 0, 125, 8, 7, "orange")

while True:

    window.update()
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    time.sleep(0.01)

window.mainloop()
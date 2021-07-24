#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *
import time

WIDTH = 600
HEIGHT = 400

xVelocity =1
yVelocity =2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
background_photo = PhotoImage(file='city.png')
background = canvas.create_image(0, 0, image=background_photo)

photo_image = PhotoImage(file='airship.png')
my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print("飞船当前坐标:"+str(coordinates))
    if coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0:
        xVelocity = -xVelocity
    if coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0:
        yVelocity = -yVelocity

    canvas.move(my_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
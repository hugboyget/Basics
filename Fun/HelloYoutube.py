#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

# radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

def order():
    if x.get() == 0:
        print("You ordered pizza !")
    elif x.get() == 1:
        print("You ordered hamburger")
    else:
        print("You ordered hotdog !")
window = Tk()


food = ["pizza", "hamburger", "hotdog"]

pizzaImage = PhotoImage(file="icon_love.png")
hamburgerImage = PhotoImage(file="icon_love.png")
hotdogImage = PhotoImage(file="icon_love.png")
foodImages = [pizzaImage, hamburgerImage, hotdogImage]


x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text to radio buttons
                              variable=x, #groups radiobuttons together if they share the variable
                              value=index, #assigns each radiobutton a different value
                              padx=25, #adds padding on x-axis
                              font=('Impact', 50),
                              image=foodImages[index],
                              compound='left',
                              indicatoron=0, #eliminate circle indicators
                              width=375, #sets width of radio buttons
                              command=order #set command of radiobutton to funtion
                              )
    radiobutton.pack(anchor=W)


window.mainloop()


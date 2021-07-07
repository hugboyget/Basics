#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

from tkinter import *
from tkinter.ttk import *
import time


def start():
    GB = 10
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        bar['value'] += 10
        download+=speed
        percent.set(str((download/GB)*100)+"%")
        text.set(str(download)+'/'+str(GB)+" GB completed")
        window.update_idletasks()



window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)


percentLabel = Label(window, textvariabl=percent).pack()
taskLabel = Label(window, textvariable=text).pack()
button = Button(window, text="download", command=start).pack()

window.mainloop()



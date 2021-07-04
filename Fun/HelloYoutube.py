#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm

# listbox = A list of selectabel text items within it's own container
from tkinter import *

def submit():
    print("You have ordered:")
    for i in listbox.curselection():
        print(listbox.get(i))

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
        listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg="pink",
                  font=("Constantia", 15),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())


entryBox = Entry(window,
                 bg='green')
entryBox.pack()


submitButton = Button(window, text="submit", command=submit)
submitButton.pack()

addButton = Button(window, text="add", command=add)
addButton.pack()

deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()




window.mainloop()


#-*- coding: utf-8 -*-
#@Time : 2021/6/18 21:33
#@Author : HUGBOY
#@File : HelloYoutube.py
#@Software: PyCharm



from tkinter import *
from tkinter import messagebox


def click():
    #messagebox.showinfo(title='INFO!', message='You are aperson.')
    #messagebox.showwarning(title='WARNING!', message='You have A VIRUS !')
    #messagebox.showwarning(title='ERROR!', message='something went wrong :(')

    #if messagebox.askokcancel(title='ask ok cancel', message='Do it ?'):
    #    print("You do it.")
    #else:
    #    print("You canceled it.")

    #if messagebox.askretrycancel(title='ask retry cancel', message='重试 ?'):
    #    print("You retry it.")
    #else:
    #    print("You canceled it.")

    #if messagebox.askyesno(title='ask yes or no', message='Do you like cake ?'):
    #   print('I like cake too:)')
    #else:
    #   print('Why do you not like cake:(')

    # answer = messagebox.askquestion(title='ask question', message='Do you like pie!')
    # if(answer == 'yes'):
    #     print('me too')
    # else:
    #     print('why ?')

    answer = messagebox.askyesnocancel(title='Yes no cancel',
                                       message='Do you like to code?',
                                       icon='warning')
    #icon= info,warning,error
    if answer == 'True':
        print("you like")
    elif answer == False:
        print("you dot like")
    else:
        print("you dodged it.")




window = Tk()

button = Button(window, command=click, text='click me!!!')
button.pack()

window.mainloop()


__author__ = 'tkessler'

from tkinter import *
from tkinter.colorchooser import askcolor

def setBgColor():
    (colorvalues, hexcolor) = askcolor()
    if hexcolor:
        thebutton.config(fg=hexcolor)
        print(hexcolor)

win = Tk()
thelabel = Label(win, text="This is the label")
thelabel.pack()
thebutton = Button(win, text="Change Label Color", command=setBgColor)
thebutton.pack()
win.mainloop()

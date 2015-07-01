__author__ = 'tkessler'

from tkinter import *
root = Tk()

def radio1():
    global tmp #sets tmp variable to global scope (can be initially called here or in parent of global tree...)
    tmp = IntVar()
    for i in range(10):
        Radiobutton(root, text=str(i), value=i, variable=tmp).pack(side=LEFT)
    tmp.set(5)

radio1()
root.mainloop()
__author__ = 'tkessler'

from Tour.entry2 import fields, fetch, makeform
from Tour.quitter import Quitter
from tkinter import *

def modalentry():
    subwin = Toplevel()
    entries=makeform(subwin, fields)
    Button(subwin,text="Fetch", command=(lambda: fetch(entries))).pack(side=LEFT)
    #Quitter(subwin).pack(side=RIGHT)
    subwin.focus_set()
    subwin.grab_set()
    subwin.wait_window()

root = Tk()
Button(root, text="Entry Form", command=modalentry).pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()
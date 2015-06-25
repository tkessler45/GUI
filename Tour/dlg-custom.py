__author__ = 'tkessler'

import sys
from tkinter import *
makemodal = (len(sys.argv) > 1) #T/F flag...

def dialog():
    win = Toplevel()
    Label(win, text="Hard drive reformatted!").pack()
    Button(win, text="OK", command=win.destroy).pack()
__author__ = 'tkessler'

import sys
from tkinter import *

def hello(event):
    print("single-click detected...")

def quit(event):
    print('double-click detected...')
    print("quitting...")
    sys.exit(0)

widget=Button(None,text='double-click to exit...')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)
widget.mainloop()
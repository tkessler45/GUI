__author__ = 'tkessler'

import tkinter
from tkinter import Tk, Button

tkinter.NoDefaultRoot()

win1 = Tk()
win2 = Tk()

Button(win1, text="button1", command=win1.destroy).pack() #quits only win1...
Button(win2, text='button2', command=win2.quit).pack() #quits all windows, by destroying the mainloop...

win1.mainloop() #must call a specific window's mainloop....no root to launch
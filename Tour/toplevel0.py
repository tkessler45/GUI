__author__ = 'tkessler'

import sys
from tkinter import Toplevel, Button, Label, mainloop

#independent windows, but part of the same process (may change with MP later on...)
win1 = Toplevel()
win2 = Toplevel()

Button(win1, text='button in first window', command=sys.exit).pack()
Button(win2, text='button in second window', command=sys.exit).pack()

Label(text='Popups').pack() #attached to "root" window...
#killing root window kills the app, and all topwindows, but killing the topwindows just kills that window...
mainloop()
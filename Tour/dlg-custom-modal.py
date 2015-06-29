__author__ = 'tkessler'

import sys
from tkinter import *
print(len(sys.argv))
makemodal = (len(sys.argv) > 1) #T/F flag...

#Modal mode is going to reserve creation of popup to one window....

def dialog():
    print("running...")
    win = Toplevel()
    Label(win, text="Hard drive reformatted!").pack()
    Button(win, text="OK", command=win.destroy).pack()
    if makemodal: #if more than one argument...
        win.focus_set() #take over input focus (direct focus to this widget...)
        win.grab_set() #disable other windows --> directs events to this widget
            # these capture the window manager? and focus all window tasks to this window...
        win.wait_window()
            # This prevents additional execution until window is destroyed...only for one instance though
    print('dialog exit')

root = Tk()
Button(root, text="popup", command=dialog).pack()
Button(root, text="quit", command=root.destroy).pack() #not interactable in with "win.grab_set" enabled above...
root.mainloop()
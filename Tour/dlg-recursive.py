__author__ = 'tkessler'

from tkinter import *

def dialog():
    win = Toplevel()
    Label(win, text="Hard drive reformatted").pack()
    Button(win, text="OK!", command=win.quit).pack() #quit instead of destroy kills the Tk() instance...
    win.protocol('WM_DELETE_WINDOW', win.quit) #when window is closed, invoke "quit" method...
    win.focus_set() # capture input by directing it to this window...
    win.grab_set() # direct events to this window, disabling others (ie, no buttons on other wins will work)
    win.mainloop() #starts a new mainloop for the "win" process...
        #all events from this point on wait until nested mainloop is done
        #win.quit call above kills this nested loop...
            # requires quit events be bound to buttons as well as windows, or else may be stuck endlessly...
    win.destroy() #destroy the current window once mainloop releases (ie, when win.quit is called).
    print('dialog exit...')

root = Tk()
Button(root, text="launch dialog", command=dialog).pack()
root.mainloop()
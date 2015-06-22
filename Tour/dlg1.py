__author__ = 'tkessler'

from tkinter import *
from tkinter.messagebox import *

def callback():
    if askyesno('Verify', 'Do you really want to quit?'): #tkinter messagebox method
        showwarning('Yes', 'Quit not yet implemented') #tkinter messagebox method...
    else:
        showinfo('No','Quit has been cancelled')

errmsg = 'Sorry, no Spam allowed!'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('Spam',errmsg))).pack(fill=X)
mainloop()
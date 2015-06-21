__author__ = 'tkessler'

import sys
from tkinter import *

class HelloClass:
    def __init__(self):
        widget = Button(None, text="Hello event world", command=self.quit) #calls a Tk instance???
        widget.pack()

    def quit(self):
        print("class quitting...")
        sys.exit()

class HelloCallable:
    def __init__(self):
        self.msg = "Called class..."

    def __call__(self):
        print(self.msg)
        sys.exit()

#HelloClass()
#mainloop()

widget = Button(None,text="call the class", command=HelloCallable())
widget.pack()
widget.mainloop()
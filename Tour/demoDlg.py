__author__ = 'tkessler'

# create a bar of buttons to launch dialog demos...

from tkinter import *
from Tour.dialogTable import demos
from Tour.quitter import Quitter
import tkinter

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Basic Demos").pack()
        for (key,value) in demos.items():
            Button(self,text=key, command=value).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)

if __name__ == '__main__': Demo().mainloop()

# from tkinter.simpledialog import askfloat
# print(askfloat("entry",'enter a number'))

from tkinter.colorchooser import askcolor
print(askcolor())

# from tkinter.filedialog import askopenfilename
# print(askopenfilename())
__author__ = 'tkessler'

from tkinter import *
from Tour.dialogTable import demos
from Tour.quitter import Quitter

#Changing tkinter variables changes the widgets associated to them...
#The unique identifier is the "value" key. This sets the associated stribg variable
    #if any tkinter object's value is the same as the variable, it will be activated
    #if any tkinter object's value is not the same as this variable, it will not be activated.
        #Can use to associate same radio control in different frames.

class Demo(Frame):
    def __init__(self, parent=None, **Options):
        Frame.__init__(self, master=parent, **Options)
        self.pack()
        Label(self, text="Radio demos").pack(side=TOP)
        self.var = StringVar() #Radio buttons that hold this in common will switch
        for key in demos:
            Radiobutton(self, text=key, command=self.onPress, variable=self.var, value=key).pack(anchor=NW)
            self.var.set(key)
        self.var2 = StringVar()
        for key in demos:
            Radiobutton(self, text=key, variable=self.var2, value=key).pack(anchor=NW)
            self.var2.set(key)
        Radiobutton(self, text='False Color', variable=self.var, value='Color').pack(anchor=NW)
        Button(self, text='State', command=self.report).pack(fill=X)
        Quitter(self).pack(fill=X)

    def onPress(self):
        pick = self.var.get()
        print('Result of %s is: %s' % (pick, demos[pick]()))

    def report(self):
        print(self.var.get())
        print(self.var2.get())

if __name__ == '__main__': Demo().mainloop()
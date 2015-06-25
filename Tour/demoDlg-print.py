__author__ = 'tkessler'

from tkinter import *
from Tour.dialogTable import demos
from Tour.quitter import Quitter

class Demo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, master=parent)
        self.pack()
        Label(self, text="Basic demos").pack()
        for key in demos:
            func = (lambda preserved=key: self.printit(preserved)) #preserve 'key'
            # otherwis, key will resolve to last item in loop
            # self reference means the embedded lambda will be a call of the "Demo" class...

            # for (key, value) in demos.items():
            #     func = (lambda key=key: self.printit(key)) # can be nested i Button()
            # for (key, value) in demos.items():
            #     def func(key=key): self.printit(key) # but def statement cannot

            Button(self, text=key, command=func).pack(side=TOP, fill=BOTH) #store lambda function in each button.
        Quitter(self).pack(side=TOP, fill=BOTH) #a frame object, can pack into geometry handler...

    def printit(self, name):
        print(name, 'returns =>', demos[name]()) # passed the name of the key, and calls the associated function...

if __name__ == '__main__': Demo().mainloop()
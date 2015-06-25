__author__ = 'tkessler'

from tkinter import *
from tkinter.messagebox import askokcancel

class Quitter(Frame): #in separate frame when instance mainloop is called...
    def __init__(self, parent=None): #default in no parent frame...
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text="Quit", command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)

if __name__ == "__main__": Quitter().mainloop()
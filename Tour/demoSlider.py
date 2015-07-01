__author__ = 'tkessler'

from tkinter import *
from Tour.dialogTable import demos
from Tour.quitter import Quitter

class Demo(Frame):
    def __init__(self, parent=None, **Options):
        Frame.__init__(self, master=parent, **Options)
        self.pack() #pack self into geometry handler
        Label(self, text="scale demos").pack()
        self.var = IntVar()
        Scale(self, label='Pick demo number',
              command=self.onMove,
              variable=self.var,
              from_=0,
              to=len(demos)-1).pack()
        Scale(self, label='Pick demo number',
              command=self.onMove,
              variable=self.var,
              from_=0, to=len(demos)-1,
              length=200, tickinterval=1,
              showvalue=YES, orient='horizontal').pack()
        Quitter(self).pack(side=RIGHT)
        Button(self, text="Run demo", command=self.onRun).pack(side=LEFT)
        Button(self, text="State", command=self.report).pack()

    def onMove(self, value):
        print('in onMove', value)

    def onRun(self):
        pos = self.var.get()
        print('You picked', pos)
        demo = list(demos.values())[pos]
        print(demo())

    def report(self):
        print(self.var.get())

if __name__=='__main__':
    print(list(demos.keys()))
    Demo().mainloop()
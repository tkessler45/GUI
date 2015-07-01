__author__ = 'tkessler'

from tkinter import *
from Tour.dialogTable import demos
from Tour.quitter import Quitter

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, master=parent, **options)
        self.pack()
        self.tools() #call instance of local tools widget
        Label(self, text="check demos").pack()
        self.vars = []
        self.returns = {}
        for key in demos:
            var = BooleanVar(value=True) #declare the GUI interface variable...
            Checkbutton(self,
                        text=key,
                        variable=var,
                        command=(lambda key=key: self.demoshandler(key, demos))).pack()
            self.vars.append(var)
            self.returns[key]=""

    def report(self):
        for var in self.vars:
            print(var.get(), end=' ') #print var (checkbox toggle) values
        print('')
        for key in self.returns:
            print("%s: %s" % (key,self.returns[key]))
        print('\n')

    def tools(self):
        frm = Frame(self) #create a new frame in which to house buttons...
        frm.pack(side=RIGHT) #place on right-hand side of parent frame...
        Button(frm, text="State", command=self.report).pack()
        Quitter(frm).pack(fill=X)

    def demoshandler(self, key, fndict):
        self.returns[key]=fndict[key]()

if __name__=="__main__":
    Demo().mainloop()
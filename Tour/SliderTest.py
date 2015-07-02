__author__ = 'tkessler'

from tkinter import *
from Tour.quitter import Quitter

class fineslider(Frame):
    def __init__(self, parent=None, **Options):
        Frame.__init__(self, master=parent, **Options)
        self.pack(expand=YES, fill=X, padx=5)
        self.var = DoubleVar()
        tickint = 100
        rangemax = 100
        Scale(self,
              label="Fine Slider",
              variable=self.var,
              command=self.sliderVal,
              from_=0,
              to=rangemax,
              tickinterval=tickint,
              #length=200,
              showvalue=YES,
              orient='horizontal',
              resolution=1/tickint).pack(expand=YES, fill=BOTH) #not working??? -- only fills self...
        Quitter(self).pack()

    def sliderVal(self,var):
        pass
        #print(var)

if __name__ == "__main__":
    fineslider().mainloop()


    # root = Tk()
    # scl = Scale(root, from_=-100, to=100, tickinterval=50, resolution=10, orient='horizontal').pack(expand=YES, fill=X)
    #
    # def report():
    #     print(scl.get())
    # Button(root, text='state', command=report).pack(side=RIGHT)
    # root.mainloop()
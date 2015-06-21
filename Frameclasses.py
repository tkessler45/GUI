__author__ = 'tkessler'

"""
Can create a "plug-in" of sorts for implementing GUI properties
    - such as a graph inset that can be appended to another layout...
    - or a listbox inset...
    - or a notes/text inset...
    - even custom buttons, etc...
"""

from tkinter import *

class CustomFrameClass(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, master=parent)
        self.pack()
        self.data = 42 # arbitrary data, settings, etc...
        self.makeWidgets()

    def makeWidgets(self): #build GUI options for this frame here...
        Button(self, text="button1", command=self.buttonCmd).pack()
        Button(self, text="button2", command=self.buttonCmd).pack()
        Button(self, text="button3", command=self.quit).pack() #self.quit inherited from Frame...

    def buttonCmd(self):
        self.data+=1
        print("button has been pressed")
        print("data value is now %d" % self.data)

#inherited widget with custom label, can be used to add additional buttons, etc...
class CustomFrameExtension(CustomFrameClass):
    def makeWidgets(self):
        CustomFrameClass.makeWidgets(self)
        Label(self, text='Extension label...').pack()
        Button(self, text="Extension function", command=self.extension).pack()

    def extension(self):
        print("extension button pressed!!!")

if __name__=="__main__":
    parent = Frame()
    parent.pack()
    #CustomFrameClass(parent).pack(side=RIGHT)
    CustomFrameExtension(parent).pack(side=RIGHT)

    Button(parent, command=sys.exit, text='non classed').pack(side=LEFT) #sys.exit equivalent to self.quit...
    parent.mainloop()
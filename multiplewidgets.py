__author__ = 'tkessler'

from tkinter import *
import sys

def greeting():
    print("Hello stdout...")

def buttonfn():
    mainwin.quit()
    #sys.exit(0)

mainwin = Frame() # from tkinter...
mainwin.pack(expand=YES, fill=BOTH)#allow main window to expand...?
    # expand allows the centering of the frame...
    # fill allows stretching of contents to proportionally match the frame....
    # side is not needed, but can ?anchor? the contents along a side???

#positioning using fill
# Button(mainwin, text="Print", command=greeting).pack(side=LEFT, fill=Y) #packed on top of other widgets...
# Label(mainwin, text="This is the label").pack(side=TOP)
# Button(mainwin, text="Quit", command=buttonfn).pack(side=RIGHT, expand=YES, fill=X)

#positioning using anchors
Label(mainwin, text="This is the label").pack(side=TOP)
Button(mainwin, text="Print", command=greeting).pack(side=LEFT, anchor=NW) #packed on top of other widgets...
Button(mainwin, text="Quit", command=buttonfn).pack(side=RIGHT, anchor=NE)

mainwin.mainloop()

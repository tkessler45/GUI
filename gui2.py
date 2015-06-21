__author__ = 'tkessler'

from tkinter import *

def buttonfn(): #callback handler...
    print("Pressed")
    sys.exit(0)

mainwin = Tk()
#handling function...
# thebutton = Button(mainwin,
#                    text="quit",
#                    command=buttonfn)

def fnWithArgs(x,y):
    global extArg1, extArg2 #can pass in globals, and then use arguments for user inputs, etc.
    print(x,y, extArg1, extArg2)

#lambda function...allows for inline use of sys.exit with "0" as argument...
# thebutton = Button(mainwin,
#                    text="add one",
#                    #command=(lambda: sys.exit(0)),
#                    #command=(lambda: fnWithArgs(42,45)),
#                    command=fnWithArgs(42,45), #no error, but calls the function immediately
#                    )

extArg1 = 999
extArg2 = 666

def argHandler():
    fnWithArgs(extArg1, extArg2)

thebutton = Button(mainwin,
                   text="trigger handler",
                   #command=(lambda: sys.exit(0)),
                   command=(lambda: argHandler()),
                   )

#thebutton.pack(side=TOP, expand=TRUE, fill=BOTH) #BAD! Places activation zones outside of button frame...
thebutton.pack(expand=TRUE, fill=BOTH)
Label(mainwin,text="A Label").pack(expand=TRUE, fill=BOTH)
mainwin.mainloop()
__author__ = 'tkessler'

# from tkinter import Label
# widget = Label(None, text="Hello GUI World!")
# widget2 = Label(None, text="     X     ")
# widget.pack() #packs the widget in its parent so tkinter geometry manager knows about them...
# widget2.pack()
# widget.mainloop()

#ALTERNATIVE
from tkinter import *
mainwin = Tk()
dud = Label(mainwin, text="asdfasdfasdf").pack(side=TOP, expand=YES, fill=BOTH)
print(dud)
mainwin.mainloop()
print("END")

#ALTERNATIVE 2
# from tkinter import *
# widget = Label()
# widget['text'] = "Hi there"
# widget.pack()
# mainloop()
# print("END")

from tkinter import *
# root = Tk()
# widget = Label(root)
# widget.config(text="ASDFASDFZXCXZCV")
# widget.pack(side=TOP, expand=TRUE, fill=BOTH)
# root.title('the title')
# root.mainloop()

# from tkinter import *
# newroot = Tk()
# options = {"text":"this is the text"}
# layout = {"side":"top", "expand":"true","fill":"both"}
# thewin = Label(newroot,**options)
# thewin.pack(**layout)
# thewin.mainloop()
__author__ = 'tkessler'

from tkinter import *
from Tour.quitter import Quitter

def fetch(event=NONE):
    print('Input => "%s"' % ent.get())
    if event:
        root.focus()

def cleartext(event):
    #ent.delete(0,len(ent.get()))
    ent.delete(0, END)

root = Tk() #create new toplevel widget
ent = Entry(root) # new text entry widget
ent.insert(0, "Type words here") #prime widget with text
ent.pack(side=TOP, fill=X) #pack the widget in the toplevel frame

#ent.focus() #switch focus to the text widget
ent.bind('<FocusIn>',cleartext)
ent.bind("<Return>", (lambda event: fetch(event))) #bind the "fetch" function to the Return key
    #(lambda event: fetch()) used to capture event and not pass it to the function
        # the function does not requre the event...
btn = Button(root, text='Fetch', command=fetch) #Create a separate button for the fetch event...
btn.pack(side=LEFT) #place the button on the left side
Quitter(root).pack(side=RIGHT) #place a qutter object on the right side (this quits the passed frame)
root.mainloop()
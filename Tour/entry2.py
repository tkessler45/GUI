__author__ = 'tkessler'

from tkinter import *
from Tour.quitter import Quitter
fields = 'Name', 'Job', 'Pay'

def fetch(entries):
    for entry in entries:
        print('Input => "%s"' % entry.get()) #entry is going to be a field object...

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root) #new frame in root to contain widgets...
        lab = Label(row, width=5, text=field) #add label to this row
        ent = Entry(row)
        row.pack(side=TOP, fill=X) #pile from top down, and expand to fill window width.
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, expand=YES, fill=X)
        entries.append(ent) #build the list of entry objects...
    return entries

if __name__ == "__main__":
    root = Tk()
    # form generator populates frame with widgets
        # creates list of entry objects, that is passed to "fetch" to "get" its content...
        # This list is shared objects that will be updated
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event: fetch(ents))) #hold the event and only call on "ents" object...
        # when lambda is built, it is passed "ents" object...???
    Button(root, text="Fetch", command=(lambda: fetch(ents))).pack(side=LEFT)
        # lambda preserves "ents" and allows it to be passed to "fetch"
        # using just fetch(ents) here will call it immediately
    Quitter(root).pack(side=RIGHT)
    root.mainloop()
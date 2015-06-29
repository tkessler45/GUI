__author__ = 'tkessler'

from tkinter import *
from Tour.quitter import Quitter
from Tour.entry2 import fields

"""
Using StringVars in this way can have them be associated to forms even after forms have been destroyed.
    tkinter variables (for interface variable storage):

        StringVars
        BooleanVar
        IntVar
        DoubleVar
"""

#Once variables is populated, fetching them with this function will print them...
def fetch(variables):
    for var in variables:
        print('Input => "%s"' % var.get()) #???

#This will return a list of variables
def makeform(root, fields):
    form = Frame(root)
    left = Frame(form)
    right = Frame(form)
    form.pack(fill=X) # spread frame throughout root frame
    left.pack(side=LEFT) #place on left side
    right.pack(side=RIGHT, expand=YES, fill=X)

    variables=[] #string variable objects, shared with main program...
    for field in fields:
        label = Label(left, width=5, text=field)
        entry = Entry(right)
        label.pack(side=TOP)
        entry.pack(side=TOP, fill=X)
        var = StringVar() #shared storage object for individual form entry objects...
        entry.config(textvariable=var) #the value of the stringvar will be displayed....
        var.set('enter here')
        variables.append(var)
    return variables

if __name__=="__main__":
    root = Tk()
    vars = makeform(root, fields)
    Button(root, text='Fetch', command=(lambda: fetch(vars))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind("<Return>", (lambda event: fetch(vars)))
    root.mainloop()
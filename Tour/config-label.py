__author__ = 'tkessler'

"""
Color
    bg -- background properties
    fg -- foreground (text) properties
Size
    height -- in px
    width
Font
    tuple of: (name, size, style)
    - names: system, Courier, Helvetica, times, etc...
    - size: int of font size...
    - style: bold, normal, italic, underline, over strike, or combo of these...
Layout
    pack -- package widget into geometry manager...
    expand -- move proportionally with window resize
    fill -- fill parent frame, resizing proportionally with window.

Borter and relief
    bd -- set border width
    relief -- set border style: FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE

Cursor
    cursor -- set to cursor type when overlayed: watch, pencil, cross, hand3, gumby

State
    state -- change interaction state: DISABLED, NORMAL, READONLY

Padding
    padx -- change external margins in x direction
    pady -- change external margins in y direction...
"""

from tkinter import *
root = Tk()
labelfont = ('times', 20, 'bold')
widget = Label(root, text='Hello config world')
widget.config(bg='black',fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=20)
widget.pack(expand=YES, fill=BOTH)

widget2=Label(root, text="crazy!")
widget2.config(height=50,width=50)
widget2.config(bg="#efcdab", fg="#abcdef")
widget2.config(font=('chalkduster',18,'italic'))
widget2.config(cursor='gumby')
widget2.config(padx=20,pady=40)
widget2.pack()

root.mainloop()
__author__ = 'tkessler'

from tkinter import *
msg = Message(text="This is a message that extends and extends and extends and extends...")
msg.config(bg='pink',font=('times',20,'bold italic'))
msg.pack(fill=BOTH,expand=YES)
mainloop()
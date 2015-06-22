__author__ = 'tkessler'

from tkinter import *

root = Tk() #explicit root declared before separate toplevels are spawned...

trees = [('The Larch!', 'light blue'),
         ('The Pine!', 'light green'),
         ('The Giant Redwood!', 'red')]

for (tree, color) in trees:
    win = Toplevel(root) #not packed...this gets things packed into it, but is not packed itself...
    win.title('Sing...%s' % tree)
    win.protocol('WM_DELETE_WINDOW', lambda: None) #intercept close window button action and nullify it
    win.iconbitmap('py-blue-trans-out.ico')

    msg = Button(win, text=tree, command=win.destroy) #can be used to destroy specific widgets...not just windows.
    msg.pack(expand=YES, fill=BOTH)
    msg.config(padx=10,pady=10,bd=10,relief=RAISED)
    msg.config(bg='black',fg=color,font=('times', 30, 'bold italic'))

root.title('Lumberjack Demo')
Label(root, text='Main Window', width=30).pack()
Button(root, text="Quit All", command=root.quit).pack()
root.mainloop()
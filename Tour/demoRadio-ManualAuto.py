__author__ = 'tkessler'

from tkinter import *

#manual
# if __name__=='__main__':
#     state = ''
#     buttons = []
#     def onPress(i):
#         global state
#         state=i
#         for btn in buttons:
#             btn.deselect()
#         buttons[i].select()
#
#     root = Tk()
#     for i in range(10):
#         rad = Radiobutton(root, text=str(i), value=str(i), command=(lambda i=i: onPress(i)))
#         rad.pack(side=LEFT)
#         buttons.append(rad)
#
#     onPress(0)
#     root.mainloop()
#     print(state)

#auto
if __name__=='__main__':
    root = Tk()
    var = StringVar() #must be declared after Tk is called...
    for i in range(10):
        Radiobutton(root, text=str(i), value=i, variable=var).pack(side=LEFT)
    var.set(0)
    root.mainloop()
    print(var.get())
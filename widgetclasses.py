__author__ = 'tkessler'

from tkinter import *

"""
Creating customizations to standardized classes that can all be called
independently without additional coding...such as look/feel customizations
"""

#new button class
class HelloButton(Button):
    def __init__(self, parent=None, **config): #pass parent frame default for initializing parent class...
        Button.__init__(self, master=parent, **config)
        self.pack()
        self.config(command=self.callback, font=('zapfino', 18))

    def callback(self):
        print("Adios!")
        self.quit()

#New subclass with redefined callback...but retains customizations from parent
class newButton(HelloButton):
    def callback(self):
        print("Goodbye!")
        self.quit()

if __name__ == "__main__":
    HelloButton(text="the button")
    newButton(text='subclassed')
    mainloop()
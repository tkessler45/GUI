__author__ = 'tkessler'

from tkinter import *
import threading, time, queue

def buttonhandler(arg1, arg2, arg3):
    global globalvar
    print("generated arguments:",arg1, arg2)
    print("global variable:", globalvar)
    print("second global variable in lambda:", arg3)

globalvar = 42
globalvar2 = 420
lock = threading.Lock()

def incrementor(): #update all globals in a separate thread...
    global globalvar
    global globalvar2
    while True:
        with lock:
            globalvar+=1
            globalvar2+=10
        time.sleep(1)

"""
lambda functions generate (and thus solidify) arguments
for functions called by the lambda, so for the function
'buttonhandler(genarg, x)' in lambda below, both the
genarg and x arguments are no longer variables. this is
auto-retention of their values...

THIS OCCURS WHEN LAMBDA IS CALLED, so 'globalvar2' should
update each time the button is pressed and the lambda is
run...
"""

def guigenerator(genarg, win):
    localvar = 5
    global globalvar2
    # x=localvar in lambda passes "localvar" in as the value for "x" in lambda (default argument values)
    # lambda can also be....(lambda: buttonhandler(genarg, localvar)) for the same effect.
    Button(win, text="click me", command=(lambda x=localvar: buttonhandler(genarg, x, globalvar2))).pack()
    print("gui generated... value %d retained in Button" % localvar)

master = Tk()
guigenerator(globalvar,master)

#increment globalvar every second in separate thread...
thethread = threading.Thread(target=incrementor)
thethread.setDaemon(True)
thethread.start()

master.mainloop()
print("end...")
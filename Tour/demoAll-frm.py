__author__ = 'tkessler'

from tkinter import *
from Tour.quitter import Quitter
demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']
parts = []

def addComponents(root):
    for demo in demoModules:
        module = __import__(demo) #dynamic importer...
        part = module.Demo(root)
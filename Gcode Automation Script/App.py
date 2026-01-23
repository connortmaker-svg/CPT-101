import pyperclip #Library for Copying things
import os #The Library for manuevering in the File systems
import tkinter as tk #Library for app dev
from tkinter import ttk
from tkinter import *

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

myapp = App()

myapp.master.title("Gcode Automation")
myapp.master.maxsize(500, 500)

ttk.Label(text="Hello World").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1,row=0)

myapp.mainloop()
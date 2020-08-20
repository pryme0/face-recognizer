import tkinter as tk
from tkinter import *
from PIL import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
import os

root = Tk()

root.filename = filedialog.askopenfilename(initialdir='C:/Users/prym0/PycharmProjects/face/venv/',filetypes=(("Image files", "*.txt"),
                                           ("Image files", "*.png")))
print(root.filename)
root.title(root.filename)
text2=open(root.filename).read()
print(text2)
t = Text(root,height=15,width=60)
t.insert(END,text2)
t.pack()

root.tk_setPalette(background='purple')
root.mainloop()

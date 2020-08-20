import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from pathlib import Path
import cv2
import os
def close():
    Label.destroy()
def toggle():
    if mylabel.visible:
        btnToggle["text"] = "Show Example"

        mylabel.place_forget()
    else:
        mylabel.place(mylabel.pi)
        with open('log.txt', 'r') as f:
                t = Text(root,height=15,width=60)
                t.insert(INSERT, f.read())
                t.pack()
        print ("Now you see it")
        btnToggle["text"] = "Hide Example"
        btnclose.pack()
    mylabel.visible = not mylabel.visible

root = tk.Tk()



mylabel = tk.Label(text="Example")
mylabel.visible = True
mylabel.place(x=20, y=50)
mylabel.pi = mylabel.place_info()

btnToggle = tk.Button(text="Hide Example", command=toggle)
btnToggle.place(x=70, y=150)
btnclose = tk.Button(text="Hide Example", command=close)


root.mainloop()

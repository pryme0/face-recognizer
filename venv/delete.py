import tkinter as tk
from tkinter import *
from PIL import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
import os
import shutil

path1 = os.getcwd()
root=Tk()
suc = tk.Label(text='').pack()
def click_close():
         root.destroy()
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    path2 = "C:/Users/prym0/PycharmProjects/face/venv/images"+ "/"+inputValue
    dele = shutil.rmtree(path2,ignore_errors=True)
    if dele:
        try:
            lag = tk.Label(text='image deleted uploaded').pack()
        except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        return



lag = tk.Label(text='Enter users name').pack()
textBox=Text(root, height=2, width=40)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Delete",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()
buttonClose=Button(root, height=1,bg='red', width=10, text="close",
                    command=lambda: click_close())
buttonClose.pack()
root.tk_setPalette(background='purple')


mainloop()





import cv2
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from pathlib import Path
import os
import numpy as np
import cv2


path1 = os.getcwd()
root = Tk()
suc = tk.Label(text='').pack()
def click_close():
         root.destroy()
def retrieve_input():
    inputValue = textBox.get("1.0","end-1c")
    path2 = "C:\\Users\\prym0\\PycharmProjects\\face\\venv\\images\\" + inputValue
    new_path = str(os.mkdir(path2))
    camera = cv2.VideoCapture(0)
    i = 0
    while i < 10:
        #raw_input('Press Enter to capture')
        input(tk.Label(text='press enter to capture image').pack())
        return_value, image = camera.read()
        scale_percent = 50 # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        image = resized
        cv2.imshow("Resized image", resized)

        cv2.imwrite(os.path.join(path2 ,str(i)+'.png'), image)
        i += 1
    del(camera)


    if i == 10:
        try:
            lag = tk.Label(text='user uploaded sucessfully').pack()
        except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        return



lag = tk.Label(text='Enter users name').pack()
textBox=Text(root, height=2, width=40)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Enroll",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()
buttonClose=Button(root, height=1, width=10,bg="red", text="close",
                    command=lambda: click_close())
buttonClose.pack()
root.tk_setPalette(background='purple')


mainloop()




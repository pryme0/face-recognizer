#!/usr/bin/python

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from pathlib import Path
import cv2
import os

path1 = os.getcwd()

class App(tk.Frame):

     def click_close():
         root.destroy()
     def retrieve_input(self):
            inputValue=textBox.get("1.0","end-1c")
            path2 = "C:\\Users\\prym0\\PycharmProjects\\face\\venv\\images\\" + inputValue
            new_path = str(os.mkdir(path2))
            camera = cv2.VideoCapture(0)
            i = 0
            while i < 10:
                #raw_input('Press Enter to capture')
                inp = input(tk.Label(text='press enter to capture image').pack_forget())


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


     def click_start(self):
            dialog_frame = tk.Frame(self)
            dialog_frame.pack(padx=50,pady=50)
            tk.Label(dialog_frame, text='system stopped..........').pack()
            os.system('python fc.py')
     def click_train(self):
              lag = tk.Label(text='Image training started').pack()
              os.system('python fc-train.py')
              lag = tk.Label(text='training completed sucessfully').pack()
     def close_log(self):
         Text.pack_forget(t)
     def click_log(self):
            val = 0
            with open('log.txt', 'r') as f:
                t = Text(root,height=15,width=60)
                t.visible = True
                if t.visible:
                    t.insert(INSERT, f.read())
                def log_close():
                    t.pack_forget()
               # t.insert(END,text1)
                t.pack()
                val = 1
                Button(text='close log',default='active',command=log_close,bg="black").pack(side='bottom')
                print (val)
     def click_delete(self):
            os.system('python delete.py')
     def click_enrol(self):
            os.system('python enrol.py')
     def click_close(selfself):
         root.destroy()



     def __init__(self,master):
        tk.Frame.__init__(self,master)
        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=60,pady=60)
        tk.Label(dialog_frame, text='FACIAL RECOGNITION SYSTEM').pack()
        button_frame = tk.Frame(self)
        text_frame = tk.Frame(self).pack(side='bottom')
        delete_frame = tk.Frame(self).pack(side='right')
        button_frame.pack(padx=200,pady=(70,10),anchor='e')
        tk.Button(button_frame,text='close',default='active',command=self.click_close,bg="red",padx=10,pady=10).pack(side='bottom')

        tk.Button(button_frame,text='Train',default='active',command=self.click_train,bg="black",).pack(side='right')
        tk.Button(button_frame,text='start system',default='active',command=self.click_start,bg="green").pack(side='right')
        tk.Button(button_frame,text='View Log',default='active',command=self.click_log,bg="black").pack(side='right')

        global textBox
        textBox = tk.Text(text_frame, height=2, width=40)
        tk.Button(text_frame,text='enrol user',default='active',command=self.retrieve_input,bg="red").pack(side='bottom')





        self.master.resizable(True,True)
        self.master.tk_setPalette(background='purple')
        self.pack()
        self.master.title("FACE")
        lag = tk.Label(text='Enter users name to enrol').pack()



#command=lambda: retrieve_input() >>> just means do this when i press the button
       # buttonCommit.pack()
        textBox.pack()

        root.tk_setPalette(background='purple')

if __name__== '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()


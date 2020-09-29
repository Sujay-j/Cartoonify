# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:24:07 2020

@author: Sujay J
"""

from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import cv2
import tkinter as tk
import random

root = Tk()
root.geometry("800x800")

def Select_image():
    #referencing to the image panels
    global imgp1 ,imgp2
    path = filedialog.askopenfilename()
    if len(path)>0:
        Label(root,text="original Image",bg = 'blue',fg = 'black',font = ('timesnewroman',10,'bold')).place(relx=0.04,rely=0.2)
        Label(root,text="Cartoon Image",bg = 'blue',fg = 'black',font = ('timesnewroman',10,'bold')).place(relx=0.04,rely=0.2)
        isSelected = True
        image = cv2.imread(path)
        width = 500
        height =500
        image = cv2.resize(image,(width,height),interpolation = cv2.INTER_NEAREST)
        #b,g,r = cv2.split(image)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray,7)
        edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,7)
        
        color = cv2.bilateralFilter(image,11,40,40)
        cartoon = cv2.bitwise_and(color,color,mask =edges)
        cartoon = cv2.resize(cartoon,(width,height),interpolation = cv2.INTER_NEAREST)
        
        image = Image.fromarray(image)
        cartoon = Image.fromarray(cartoon)
        r = random.random()
        c = cartoon.save(f"img_{r}.jpg")
        
        image = ImageTk.PhotoImage(image)
        cartoon= ImageTk.PhotoImage(cartoon)
        
        width,height = root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d+0+0"%(width,height))
        
        if imgp1 is None or imgp2 is None:
            imgp1 = Label(image = image)
            imgp1.image = image
            imgp1.pack(side="left",padx=10,pady=10)
            
            imgp2 = Label(image=cartoon)
            imgp2.image = cartoon
            imgp2.pack(side="right",padx=10,pady=10)
            
        else:
            imgp1.configure(image=image)
            imgp2.configure(image = cartoon)
            imgp1.image=image
            imgp2.image= cartoon
            
imgp1 = None
imgp2 = None

btn = Button(root,text="CLICK HERE TO SELECT NEW IMAGE",bg = 'Blue',fg = 'black',font = ('TimesNewRoman',10,'bold'),command = Select_image)
btn.pack(side ="top",padx=10,pady=10)
   
Label(root, text="Create  Your Own Cartoonify Image",bg='white',fg='black',font=('calibre',20, 'bold')).place(relx=0.08,rely=0.8)

root.mainloop()

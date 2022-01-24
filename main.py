import tkinter as tk
from tkinter import *
import subprocess
import os
from turtle import width

## The Main Root of this app

root = tk.Tk()
root.title("EventId")
root.geometry("800x700")
root.resizable(0,0)

## Creating a List Box to display the output

list = tk.Listbox(root, height=20, width=70, bg="#101010", font="Helvetica", fg="#AAFF00")
#list.grid(row=0,rowspan=2,column=0,padx=10,pady=10)
list.pack()

## Creating the frame for the RadioButtons

frame = tk.Frame(root, width=500, height=400, bd=1)

var = tk.IntVar(value=0)

def getc() :
    x = var.get()
    if x == 1 :
        return "cmd"
    elif x == 2 :
        return "powershell"


def com(comm) :
    type = getc()
    process=subprocess.Popen([type,comm],stdout=subprocess.PIPE)
    result=process.communicate()[0].splitlines()
    for i,j in enumerate(result) :
        x = j.decode("utf-8")
        list.insert(i, j)


frame1 = tk.Frame(root)
frame1.pack()
x = tk.Radiobutton(frame1, text="CMD", variable=var, value=1, command=getc).pack(side="left")
y = tk.Radiobutton(frame1, text="Powershell", variable=var, value=2, command=getc).pack(side="left")

root.mainloop()
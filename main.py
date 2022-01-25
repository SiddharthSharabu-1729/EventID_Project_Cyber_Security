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


def PrintList(result) :
    for i,j in enumerate(result) :
        x = j.decode("utf-8")
        list.insert(i, j)


def com(comm) :
    #type = getc()
    process=subprocess.Popen(["powershell",comm],stdout=subprocess.PIPE)
    result=process.communicate()[0].splitlines()
    PrintList(result)
    

frame1 = tk.Frame(root)
frame1.pack()
xx = tk.Radiobutton(frame1, text="CMD", variable=var, value=1, command=getc).pack(side="left")
y = tk.Radiobutton(frame1, text="Powershell", variable=var, value=2, command=getc).pack(side="left")


comm_label = tk.StringVar()
comm_entry = tk.Entry(root,textvariable=comm_label)
comm_entry.place(x = 10, y = 570, width=700, height=100)

def funn() :
    radio = var.get()
    print(radio)
    if radio == 1 :
        #process=subprocess.Popen(["CMD",comm_entry.get()],stdout=subprocess.PIPE)
        #result=process.communicate()[0].splitlines()
        result = os.popen(comm_entry.get())
        #list.insert(END,result)
        for i in result :
            list.insert(END,i)
    elif radio == 0 :
        #list.delete(0, END)
        list.insert(END,"Please Select CMD or Powershell")
    elif radio == 2 :
        com(comm_entry.get())


but = tk.Button(root,text="Run",height=6,width=9,command=funn)
but.place(x=718,y=570)

root.mainloop()
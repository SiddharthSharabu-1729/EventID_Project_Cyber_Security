import tkinter as tk
from tkinter import *
import subprocess
import os
from tkinter.filedialog import askopenfile, asksaveasfile


## The Main Root of this app

root = tk.Tk()
root.title("EventId")
root.geometry("800x700")
root.resizable(0,0)
root.config(bg="#000102")


## Creating a List Box to display the output

list = tk.Listbox(root, height=20, width=70, bg="#101010", font=("bold "), fg="#AAFF00")
list.pack()


## Creating the frame for the RadioButtons

frame = tk.Frame(root, width=500, height=400, bd=1)
var = tk.IntVar(value=0)


## Custom Functions

def getc(x) :
    #x = var.get()
    if x == 1 :
        return "cmd"
    elif x == 2 :
        return "powershell"


def PrintList(result) :
    for i,j in enumerate(result) :
        x = j.decode("utf-8")
        list.insert(i, j)


def com(comm) :
    if comm == "clear" :
        list.delete(0,END)
    elif comm == "" or comm == " " :
        list.insert(END,"Enter any command")
    else :
        process=subprocess.Popen(["powershell",comm],stdout=subprocess.PIPE)
        result=process.communicate()[0].splitlines()
        PrintList(result)
    

def funn() :
    radio = var.get()
    if radio == 1 :
        result = os.popen(comm_entry.get())
        for i in result :
            list.insert(END,i)
    elif radio == 0 :
        #list.delete(0, END)
        list.insert(END,"Please Select CMD or Powershell")
    elif radio == 2 :
        com(comm_entry.get())


def save():
    files = [('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)
    text = file.name
    wri = open(text,'w')
    wri.write("The Output of the Command " + comm_entry.get() + " is")
    wri.write("\n")
    for i in list.get(0,END) :
        t = i.decode("utf-8")
        wri.write(t)
        wri.write("\n")
    wri.close()


def comm () :
    com("Get-Process")
def comm1 () :
    com("Get-EventLog -list")
def comm2 () :
    com("Get-EventLog -LogName System -Newest 10")
def comm3 () :
    com("Get-Service")
def comm4 ():
    com("Get-EventLog -LogName System -EntryType Error")
def comm5 () :
    list.delete(0,END)


frame1 = tk.Frame(root)
frame1.pack()
xx = tk.Radiobutton(frame1, text="CMD",fg="white", variable=var,selectcolor="black", value=1, bg="#000102", command=getc(var.get())).pack(side="left")
y = tk.Radiobutton(frame1, text="Powershell", fg="white", variable=var,selectcolor="black", value=2, bg="#000102", command=getc(var.get())).pack(side="left")


comm_label = tk.StringVar()
comm_entry = tk.Entry(root,textvariable=comm_label,justify = CENTER, font = ('courier', 15, 'bold'), bg="#505050")
comm_entry.place(x = 10, y = 550, width=700, height=100)


but = tk.Button(root,text="Run",height=6,width=9,command=funn)
but.place(x=718,y=550)

but1 = tk.Button(root, text="Save To a File", height=1, width=10, command=save)
but1.place(x=365,y=660)

but2 = tk.Button(root, text="Get_Process", height=1, width=10, command=comm)
but2.place(x=50, y=513)

but3 = tk.Button(root, text="Get_EventId", height=1, width=10, command=comm1)
but3.place(x=171, y=513)

but4 = tk.Button(root, text="Newest 10", height=1, width=10, command=comm2)
but4.place(x=290, y=513)

but5 = tk.Button(root, text="Get-Services", height=1, width=10, command=comm3)
but5.place(x=410, y=513)

but6 = tk.Button(root, text="Error Events", height=1, width=10, command=comm4)
but6.place(x=530, y=513)

but6 = tk.Button(root, text="Clear", height=1, width=10, command=comm5)
but6.place(x=650, y=513)


root.mainloop()
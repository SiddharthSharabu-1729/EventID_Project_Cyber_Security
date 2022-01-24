import tkinter as tk
from tkinter import *
import os
from turtle import width
import subprocess

from matplotlib.pyplot import text

root = tk.Tk()
root.title("EventId's")
def com(c) :
    process=subprocess.Popen(["powershell","Get-EventLog " + c],stdout=subprocess.PIPE);
    result=process.communicate()[0].splitlines()

    for r in result :
        x = r.decode("utf-8")
        x = x.strip()
        l = tk.Label(frame,text=x,bg="white")
        l.pack()

w = Label(root, text ='Siddharth', font = "50") 
w.pack()
  
sp = Spinbox(root, from_= 0, to = 20)
sp.pack()


canva = tk.Canvas(root, height=500, width=800, bg="#263D42")

frame = tk.Frame(root,bg="white")
frame.place(relwidth="0.8",relheight="0.8",relx="0.1",rely="0.1")

#open = tk.Button(root, text="open",command=com("-list"),bg="#278333")

canva.pack()
#open.pack()



def printf() :
    inpp = inputtxt.get(1.0, "end-1c")
    lbl.config(text="Provided Input"+inpp)

root.mainloop()

inputtxt = tk.Text(frame,text="Print",command=printf)
inputtxt.pack()

lbl = tk.Label(frame,text="")
lbl.pack()


def fun() :
    frame = tk.Tk()
    frame.title("TextBox Input")
    frame.geometry('400x200')
    # Function for getting Input
    # from textbox and printing it 
    # at label widget
    
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "Provided Input: "+inp)
    
    # TextBox Creation
    inputtxt = tk.Text(frame,
                    height = 5,
                    width = 20)
    
    inputtxt.pack()
    
    # Button Creation
    printButton = tk.Button(frame,
                            text = "Print", 
                            command = printInput)
    printButton.pack()
    
    # Label Creation
    lbl = tk.Label(frame, text = "")
    lbl.pack()
    frame.mainloop()

import tkinter as tk
from tkinter import *
import subprocess
import os
from turtle import width

from matplotlib.pyplot import text

root = tk.Tk()
root.title("EventId")

canva = tk.Canvas(root, height=600, width=700, bg="gray")
canva.pack()

frame = tk.Frame(root,bg="white")
frame.place(relwidth="0.8",relheight="0.8",relx="0.01",rely="0.01")

frame1 = tk.Frame(root,bg="white")
frame1.place(relwidth="0.98",relheight="0.8989",relx="0.01",rely="0.82")

run = tk.Button(root, text="Run",command="",bg="gray")
run.pack()

root.mainloop()
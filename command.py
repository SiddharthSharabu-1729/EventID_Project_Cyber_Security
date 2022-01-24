from tkinter import *
import subprocess

process=subprocess.Popen(["powershell","Get-EventLog -list"],stdout=subprocess.PIPE);
result=process.communicate()[0].splitlines()

for r in result :
    x = r.decode("utf-8")
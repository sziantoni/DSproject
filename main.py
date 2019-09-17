
from tkinter import *
from tkinter import filedialog


root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
f=open(root.filename)
f.readline()
for x in f:
    print(x)
f.close()
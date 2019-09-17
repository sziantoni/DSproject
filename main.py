from tkinter import *
from tkinter import filedialog

root = Tk()
root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("txt", "*.txt"), ("all files", "*.*")))
f = open(root.filename)

nClienti = f.readline()
ciao = f.readline()
nVeicoli = f.readline()

print(nClienti)
print(nVeicoli)

for x in f:
    s = f.readline()
    print(s)


f.close()

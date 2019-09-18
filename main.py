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

s = f.readline()
currentLine = s.split("   ")
x_dep = currentLine[0]
y_dep = currentLine[1]
capacity_dep = currentLine[3]
print("Deposito : x: " + x_dep + " y : " + y_dep + " capacity : " + capacity_dep)

for i in f:
    currentLineCustomer = i.split("   ")
    x = currentLineCustomer[0]
    y = currentLineCustomer[1]
    delivery = currentLineCustomer[2]
    pickup = currentLineCustomer[3]
    print("x: " + x + " y : " + y + " delivery : " + delivery + " pickup : " + pickup)


f.close()

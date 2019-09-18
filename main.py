from tkinter import *
from tkinter import filedialog
import numpy as np

def distanza(x1, y1, x2, y2):
    from math import sqrt
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#Apertura file
root = Tk()
root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("txt", "*.txt"), ("all files", "*.*")))
f = open(root.filename)

#Lettura numero clienti
nClienti = f.readline()
f.readline()

#Lettura numero veicoli
nVeicoli = f.readline()
clients=[]

print(nClienti)
print(nVeicoli)

s = f.readline()
currentLine = s.split("   ")
x_dep = currentLine[0]
y_dep = currentLine[1]
capacity_dep = currentLine[3]
print("Deposito : x: " + x_dep + " y : " + y_dep + " capacity : " + capacity_dep)
clients.append(((float(x_dep), float(y_dep))))

for i in f:
    currentLineCustomer = i.split("   ")
    x = currentLineCustomer[0]
    y = currentLineCustomer[1]
    clients.append((float(x),float(y)))
    delivery = currentLineCustomer[2]
    pickup = currentLineCustomer[3]
    print("x: " + x + " y : " + y + " delivery : " + delivery + " pickup : " + pickup)

f.close()
print(clients)

w = int(nClienti)+1
costs=np.array([[0 for x in range(w)]for y in range(w)])
print(costs.shape)
cont1=0
cont2=0

for i in clients:
    for j in clients:
        if(cont1!=cont2):
            d=distanza(i[0], i[1], j[0], j[1])
            costs[cont1, cont2] = d
        else:
            costs[cont1, cont2]=0
        cont2+=1
    cont1+=1



print(costs)




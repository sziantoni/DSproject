from tkinter import *
from tkinter import filedialog
import numpy as np


def distanza(x1, y1, x2, y2):
    from math import sqrt
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Apertura file
root = Tk()
root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("txt", "*.txt"), ("all files", "*.*")))
f = open(root.filename)

# Lettura numero clienti
nClienti = f.readline()
f.readline()

# Lettura numero veicoli
nVeicoli = f.readline()
clients = []
clients_pickup = []
clients_delivery = []

s = f.readline()
currentLine = s.split("   ")
x_dep = currentLine[0]
y_dep = currentLine[1]
capacity_dep = currentLine[3]

clients.append((float(x_dep), float(y_dep)))
clients_pickup.append((float(x_dep), float(y_dep)))
clients_delivery.append((float(x_dep), float(y_dep)))
count_pickup = 1
count_delivery = 1

for i in f:
    currentLineCustomer = i.split("   ")
    x = currentLineCustomer[0]
    y = currentLineCustomer[1]
    delivery = int(currentLineCustomer[2])
    pickup = int(currentLineCustomer[3])
    # Lista clienti totale
    clients.append((float(x), float(y)))
    # divisione tra delivery e pickup
    if delivery == 0:
        clients_pickup.append((float(x), float(y)))
        count_pickup += 1
    else:
        clients_delivery.append((float(x), float(y)))
        count_delivery += 1

f.close()

w = int(nClienti) + 1
costs = np.array([[0 for x in range(w)] for y in range(w)])
costs_pickup = np.array([[0 for x in range(count_pickup)] for y in range(count_pickup)])
costs_delivery = np.array([[0 for x in range(count_delivery)] for y in range(count_delivery)])

cont1 = 0
cont2 = 0

for i in clients:
    for j in clients:
        if i != j:
            d = distanza(i[0], i[1], j[0], j[1])
            costs[cont1, cont2] = d
        else:
            costs[cont1, cont2] = 0
        cont2 += 1
    cont1 += 1
    cont2 = 0
cont1 = 0
cont2 = 0

for i in clients_pickup:
    for j in clients_pickup:
        if i != j:
            d = distanza(i[0], i[1], j[0], j[1])
            costs_pickup[cont1, cont2] = d
        else:
            costs_pickup[cont1, cont2] = 0
        cont2 += 1
    cont1 += 1
    cont2 = 0

cont1 = 0
cont2 = 0

for i in clients_delivery:
    for j in clients_delivery:
        if i != j:
            d = distanza(i[0], i[1], j[0], j[1])
            costs_delivery[cont1, cont2] = d
        else:
            costs_delivery[cont1, cont2] = 0
        cont2 += 1
    cont1 += 1
    cont2 = 0



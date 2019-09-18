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
demand_pickup = []
demand_delivery = []
routes_pickup = [[]]
routes_delivery = [[]]

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
        demand_pickup.append(pickup)
        if count_pickup > 0:
            routes_pickup.append([0, count_pickup, 0])
        count_pickup += 1
    else:
        clients_delivery.append((float(x), float(y)))
        demand_delivery.append(delivery)
        if count_delivery > 0:
            routes_delivery.append([0, count_pickup + count_delivery, 0])
        count_delivery += 1

f.close()

routes_pickup.remove([])
routes_delivery.remove([])

print(demand_pickup)
print(demand_delivery)
print(routes_pickup)
print(routes_delivery)

w = int(nClienti) + 1
costs = np.array([[0 for x in range(w)] for y in range(w)])
costs_pickup = np.array([[0 for x in range(count_pickup)] for y in range(count_pickup)])
costs_delivery = np.array([[0 for x in range(count_delivery)] for y in range(count_delivery)])
saving = np.array([[0 for x in range(w-1)] for y in range(w-1)])
saving_pickup = np.array([[0 for x in range(count_pickup-1)] for y in range(count_pickup-1)])
saving_delivery = np.array([[0 for x in range(count_delivery-1)] for y in range(count_delivery-1)])


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

count1 = 1
count2 = 1

for count1 in range(1,len(saving)+1):
    for count2 in range(1,len(saving)+1):
        if count1 != count2:
            saving[count1-1, count2-1] = costs[count1][0] + costs[0][count2] - costs[count1][count2]
    count2 = 1

print("COST")
print(costs)
print("SAVING")
print(saving)
print("DEMAND DELIVERY")
print(demand_delivery)
print("DEMAND PICKUP")
print(demand_pickup)
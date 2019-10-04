from tkinter import *
from tkinter import filedialog
from typing import List
import cw_p
import cw_s
import RPA_Solutions
import os
import numpy
import numpy as np
import merge

# Test dei risultati


def distanza(x1, y1, x2, y2):
    from math import sqrt
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


costPar = [[]]
costSeq = [[]]
istances = []
os.chdir("C:\\Users\\kikko\\PycharmProjects\\DSproject\\Instances")
l = os.listdir(os.getcwd())
for i in l:
    if os.path.isfile(i):
        if i != '.DS_Store' and i != 'info.txt':
            istances.append(i)

print(istances)
counter = 0


for inst in istances:

    f = open(inst, "r")
    # Lettura numero clienti
    nClienti = f.readline()
    f.readline()
    # Lettura numero veicoli
    nVeicoli = f.readline()
    clients = []  # lista di tutti i clienti
    clients_pickup = []  # lista dei clienti con pickup
    clients_delivery = []  # lista dei clienti con delivery
    demands: List[int] = []
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

    final_cost = []

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
            demands.append(pickup)
            if count_pickup > 0:
                routes_pickup.append([0, count_pickup, 0])
            count_pickup += 1
        else:
            clients_delivery.append((float(x), float(y)))
            demands.append(delivery)
            if count_delivery >= 0:
                routes_delivery.append([0, count_pickup + (count_delivery - 1), 0])
            count_delivery += 1

    f.close()

    routes_pickup.remove([])
    routes_delivery.remove([])

    w = int(nClienti) + 1

    costs = np.array([[0 for x in range(w)] for y in range(w)])
    costs_pickup = np.array([[0 for x in range(count_pickup)] for y in range(count_pickup)])
    costs_delivery = np.array([[0 for x in range(count_delivery)] for y in range(count_delivery)])
    saving_list = []
    saving_list_delivery = []
    saving_list_pickup = []

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

    for count1 in range(1, int(nClienti)):
        for count2 in range(1, int(nClienti)):
            if count1 != count2:
                saving = costs[count1][0] + costs[0][count2] - costs[count1][count2]
                if ((count1, count2, saving) not in saving_list) and (
                        (count2, count1, saving) not in saving_list) and len(saving_list) > 0:
                    saving_list.append((count1, count2, saving))
                else:
                    if len(saving_list) == 0:
                        saving_list.append((count1, count2, saving))

        count2 = 1

    for count1 in range(1, count_pickup - 1):
        for count2 in range(1, count_pickup):
            if count1 != count2:
                saving_pickup = costs_pickup[count1][0] + costs_pickup[0][count2] - costs_pickup[count1][count2]

                if ((count1, count2, saving_pickup) not in saving_list_pickup) and (
                        (count2, count1, saving_pickup) not in saving_list_pickup) and len(saving_list_pickup) > 0:

                    saving_list_pickup.append((count1, count2, saving_pickup))
                else:
                    if (len(saving_list_pickup) == 0) and (count1 != count2):
                        saving_list_pickup.append((count1, count2, saving_pickup))
        count2 = 1

    for count1 in range(1, count_delivery - 1):
        for count2 in range(1, count_delivery):
            if count1 != count2:
                saving_delivery = costs_delivery[count1][0] + costs_delivery[0][count2] - \
                                  costs_delivery[count1][count2]
                if ((count1 + count_pickup - 1, count2 + count_pickup - 1,
                     saving_delivery) not in saving_list_delivery) and (
                        (count2 + count_pickup - 1, count1 + count_pickup - 1,
                         saving_delivery) not in saving_list_delivery) and len(saving_list_delivery) > 0:
                    saving_list_delivery.append(
                        (count1 + count_pickup - 1, count2 + count_pickup - 1, saving_delivery))
                else:
                    if (len(saving_list_delivery) == 0) and (count1 != count2):
                        saving_list_delivery.append(
                            (count1 + count_pickup - 1, count2 + count_pickup - 1, saving_delivery))

        count2 = 1

    saving_list = sorted(saving_list, key=lambda tup: tup[2], reverse=True)
    saving_list_delivery = sorted(saving_list_delivery, key=lambda tup: tup[2], reverse=True)
    saving_list_pickup = sorted(saving_list_pickup, key=lambda tup: tup[2], reverse=True)

    # BACKHAUL Parallelo
    parallel_routesPickup = cw_p.CW_P(saving_list_pickup, routes_pickup, capacity_dep, nVeicoli, demands)
    # LINEHAUL Parallelo
    parallel_routesDelivery = cw_p.CW_P(saving_list_delivery, routes_delivery, capacity_dep, nVeicoli, demands)
    x=0
    x = merge.merge(parallel_routesPickup, parallel_routesDelivery, demands, costs)

    costPar.append([inst, str(x)])



    seq_routesPickup = []
    seq_routesDelivery=[]
    y=0
    mean = 0
    j = 0

    if len(routes_pickup) > 0 and len(routes_delivery) > 0:
        pickup=len(routes_pickup)
        deliv = len(routes_delivery)
        for n in routes_pickup:
            # BACKHAUL Sequenziale
            seq_routesPickup = cw_s.CW_S(n, saving_list_pickup, routes_pickup, capacity_dep, int(nVeicoli), demands)

            for j in routes_delivery:
                # LINEHAUL Sequenziale
                seq_routesDelivery = cw_s.CW_S(j, saving_list_delivery, routes_delivery, capacity_dep, int(nVeicoli), demands)
                y = merge.merge(seq_routesPickup, seq_routesDelivery, demands, costs)
                if(mean == 0 or (mean > 0 and y < mean)):
                    mean = y

    else:
        if len(routes_pickup) >0  and len(routes_delivery) == 0:
            pickup = len(routes_pickup)
            for n in routes_pickup:
                # BACKHAUL Sequenziale
                seq_routesPickup = cw_s.CW_S(n, saving_list_pickup, routes_pickup, capacity_dep, int(nVeicoli), demands)
                y = merge.merge(seq_routesPickup, seq_routesDelivery, demands, costs)
                if (mean == 0 or (mean > 0 and y < mean)):
                    mean = y
        else:
            if len(routes_pickup) == 0 and len(routes_delivery)>0:
                deliv = len(routes_delivery)
                for j in routes_delivery:
                    # LINEHAUL Sequenziale
                    seq_routesDelivery = cw_s.CW_S(j, saving_list_delivery, routes_delivery, capacity_dep, int(nVeicoli), demands)
                    y = merge.merge(seq_routesPickup, seq_routesDelivery, demands, costs)
                    if (mean == 0 or (mean > 0 and y < mean)):
                        mean = y
    print(mean)
    costSeq.append([inst, str(mean)])
    counter +=1
    #idx+=1

print (counter)





os.chdir("C:\\Users\\kikko\\PycharmProjects\\DSproject\\RPA_Solutions")

costiP = open("CostiParallelo.txt", "w")
for i in range(0, counter-1):
    costiP.write(str(costPar[i]))
costiP.close()

costiS = open("CostiSequenziale.txt", "w")
for i in range(0, counter-1):
    costiS.write(str(costSeq[i]))
costiS.close()







'''
for f in filelist:
    indice = 0
    while indice < len(f):
        if indice == (len(f) - 6):
'''


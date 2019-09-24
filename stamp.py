def stampAll(routes_pickup, routes_delivery, demands, cost_matrix, nPickUp, nVeicoli, capacità, fileName):

    fileName = fileName[len(fileName)-6:]
    f = open("Result_"+fileName, "w+")

    f.write("Risultato\n")
    f.write(" \n")
    f.write("Numero di Veicoli: " + nVeicoli + "\n")
    f.write("Capacita' massima: " + capacità + "\n")
    c = 0

    if len(routes_delivery) <= len(routes_pickup):
        routes_pickup = sorted(routes_pickup, key=lambda ele: len(ele), reverse=False)
        routes_delivery = sorted(routes_delivery, key=lambda ele: len(ele), reverse=True)
        for i in range(len(routes_delivery)):
            cost = 0
            demands_delivery = 0
            demands_pickup = 0
            start_route = routes_delivery[i][:-1]
            end_route = routes_pickup[i][1:]
            new_route = start_route + end_route
            l = 0
            firstZero = False
            for j in new_route:
                if j != 0 or firstZero == False:
                    cost += cost_matrix[l][new_route[l + 1]]
                    firstZero = True
                else:
                    if j == 0 and firstZero == True:
                        firstZero = False
                if j != 0 and j in end_route:
                    demands_pickup += demands[j - 1]
                else:
                    if j != 0 and j in start_route:
                        demands_delivery += demands[j - 1]

            f.write(" " + "\n")
            f.write("Route " + str(c) + "\n")
            f.write("Load Pickup: " + str(demands_pickup) + "\n")
            f.write("Load Delivery: " + str(demands_delivery) + "\n")
            f.write("Costo Totale: " + str(cost) + "\n")
            f.write("Sequenza dei vertici  " + str(new_route) + "\n")
            c += 1
        if c < len(routes_delivery) + len(routes_pickup):
            for x in range(c, len(routes_pickup)):
                cost = 0
                demands_pickup = 0
                new_route = routes_pickup[x]
                l = 0
                firstZero = False
                for j in new_route:
                    if j != 0 or firstZero == False:
                        cost += cost_matrix[l][new_route[l + 1]]
                        firstZero = True
                    else:
                        if j == 0 and firstZero == True:
                            firstZero = False
                    demands_pickup += demands[new_route[l] - 1]
                    l += 1
                    if j != 0:
                        demands_pickup += demands[j - 1]
                f.write(" " + "\n")
                f.write("Route " + str(c) + "\n")
                f.write("Load Pickup: " + str(demands_pickup) + "\n")
                f.write("Load Delivery: 0" + "\n")
                f.write("Costo Totale: " + str(cost) + "\n")
                f.write("Sequenza dei vertici  " + str(new_route) + "\n")
                c += 1
    else:
        routes_pickup = sorted(routes_pickup, key=lambda ele: len(ele), reverse=True)
        routes_delivery = sorted(routes_delivery, key=lambda ele: len(ele), reverse=False)
        for i in range(len(routes_pickup)):
            cost = 0
            demands_delivery = 0
            demands_pickup = 0
            start_route = routes_delivery[i][:-1]
            end_route = routes_pickup[i][1:]
            new_route = start_route + end_route
            l = 0
            firstZero = False
            for j in new_route:
                if j != 0 or firstZero == False:
                    cost += cost_matrix[j][new_route[l + 1]]
                    firstZero = True
                else:
                    if j == 0 and firstZero == True:
                        firstZero = False
                if j != 0 and j in end_route:
                    demands_pickup += demands[j - 1]
                else:
                    if j != 0 and j in start_route:
                        demands_delivery += demands[j - 1]
            f.write(" " + "\n")
            f.write("Route " + str(c) + "\n")
            f.write("Load Pickup: " + str(demands_pickup) + "\n")
            f.write("Load Delivery: " + str(demands_delivery) + "\n")
            f.write("Costo Totale: " + str(cost) + "\n")
            f.write("Sequenza dei vertici  " + str(new_route) + "\n")
            c += 1
        if c < len(routes_delivery) + len(routes_pickup):
            for x in range(c, len(routes_delivery)):
                cost = 0
                demands_delivery = 0
                new_route = routes_delivery[x]
                l = 0
                firstZero = False
                for j in new_route:
                    if j != 0 or firstZero == False:
                        cost += cost_matrix[l][new_route[l + 1]]
                        firstZero = True
                    else:
                        if j == 0 and firstZero == True:
                            firstZero = False
                    l += 1
                    if j != 0:
                        demands_delivery += demands[j - 1]
                f.write(" " + "\n")
                f.write("Route " + str(c) + "\n")
                f.write("Load Pickup: 0" + "\n")
                f.write("Load Delivery: " + str(demands_delivery) + "\n")
                f.write("Costo Totale: " + str(cost) + "\n")
                f.write("Sequenza dei vertici  " + str(new_route) + "\n")
                c += 1

    return 0

def CW_P(savings_list, routes, capacity_limit, number_of_vehicles, demands):
    count_pickup = 1
    count_delivery = 1

    final_cost = []
    start = 0
    end = 0
    route1 = 0
    route2 = 0
    routes_result = []
    firstUsed = False
    secondUsed = False
    nodeUsed = []

    for i in savings_list:
        alreadyUsed = False
        counter = 0
        best_saving = i
        start_route = []
        end_route = []
        flag1 = False
        flag2 = False
        if routes_result != [[]]:
            for j in range(len(routes_result)):
                if best_saving[0] in routes_result[j] and best_saving[1] in routes_result[j]:
                    alreadyUsed = True
                else:
                    if best_saving[0] in routes_result[j] and best_saving[1] not in routes_result[j] and routes_result[j] != []:
                        firstUsed = True
                        counterR = 0
                        for r in routes_result[j]:
                            if best_saving[0] == r and r != 0:
                                if routes_result[j][counterR + 1] == 0 and flag1 == False:
                                    route1 = j
                                    start = r
                                    start_route = routes_result[j][:counterR + 1]
                                    flag1 = True
                                else:
                                    if (routes_result[j][counterR - 1] == 0) and (flag2 == False):
                                        route1 = j
                                        end = r
                                        end_route = routes_result[j][counterR:]
                                        flag2 = True
                            counterR += 1
                    else:
                        if best_saving[0] not in routes_result[j] and best_saving[1] in routes_result[j] and \
                                routes_result[j] != []:
                            secondUsed = True
                            counterR = 0
                            for r in routes_result[j]:
                                if best_saving[1] == r and r != 0:
                                    if routes_result[j][counterR + 1] == 0 and flag1 == False:
                                        route2 = j
                                        start = r
                                        start_route = routes_result[j][:counterR + 1]
                                        flag1 = True
                                    else:
                                        if (routes_result[j][counterR - 1] == 0) and (flag2 == False):
                                            route2 = j
                                            end = r
                                            end_route = routes_result[j][counterR:]
                                            flag2 = True
                                counterR += 1
        if alreadyUsed == False:
            if firstUsed and secondUsed:
                firstUsed = False
                secondUsed = False
                if start != 0 and end != 0 and flag1 and flag2:
                    flag1 = False
                    flag2 = False
                    counter_demands = 0
                    demand_total = 0
                    for x in range(len(demands)):
                        if (x + 1 in start_route) or (x + 1 in end_route):
                            demand_total += demands[x]
                    if float(demand_total) <= float(capacity_limit):
                        new_route = start_route + end_route
                        if route1>route2:
                            del routes_result[route2]
                            del routes_result[route1 - 1]
                        else:
                            del routes_result[route1]
                            del routes_result[route2 - 1]
                        routes_result.append(new_route)
                        if start not in nodeUsed:
                            nodeUsed.append(start)
                        if end not in nodeUsed:
                            nodeUsed.append(end)
            else:
                if firstUsed == True and secondUsed == False:
                    firstUsed = False

                    if flag1:
                        end = best_saving[1]
                        end_route = [best_saving[1], 0]
                        flag2 = True
                    else:
                        if flag2:
                            start = best_saving[1]
                            start_route = [0, best_saving[1]]
                            flag1 = True

                    if start != 0 and end != 0 and flag1 and flag2:
                        flag1 = False
                        flag2 = False
                        demand_total = 0
                        for x in range(len(demands)):
                            if (x + 1 in start_route) or (x + 1 in end_route):
                                demand_total += demands[x]
                        if float(demand_total) <= float(capacity_limit):
                            new_route = start_route + end_route
                            del routes_result[route1]
                            routes_result.append(new_route)
                            if start not in nodeUsed:
                                nodeUsed.append(start)
                            if end not in nodeUsed:
                                nodeUsed.append(end)
                else:
                    if firstUsed == False and secondUsed == True:
                        secondUsed = False

                        if flag1:
                            end = best_saving[0]
                            end_route = [best_saving[0], 0]
                            flag2 = True
                        else:
                            if flag2:
                                start = best_saving[0]
                                start_route = [0, best_saving[0]]
                                flag1 = True

                        if start != 0 and end != 0 and flag1 and flag2:
                            flag1 = False
                            flag2 = False
                            counter_demands = 0
                            demand_total = 0
                            for x in range(len(demands)):
                                if (x + 1 in start_route) or (x + 1 in end_route):
                                    demand_total += demands[x]
                            if float(demand_total) <= float(capacity_limit):
                                new_route = start_route + end_route
                                del routes_result[route2]
                                routes_result.append(new_route)
                                if start not in nodeUsed:
                                    nodeUsed.append(start)
                                if end not in nodeUsed:
                                    nodeUsed.append(end)
                    else:
                        alreadyUsed = False
                        x = int(demands[best_saving[0] - 1]) + int(demands[best_saving[1] - 1])
                        if x < int(capacity_limit) and len(routes_result) < int(number_of_vehicles):
                            start = best_saving[0]
                            end = best_saving[1]
                            new_route = [0, best_saving[0], best_saving[1], 0]
                            routes_result.append(new_route)
                            if best_saving[0] not in nodeUsed:
                                nodeUsed.append(start)
                            if best_saving[1] not in nodeUsed:
                                nodeUsed.append(end)
    for r in routes:
        if r[1] not in nodeUsed:
            routes_result.append(r)

    return routes_result
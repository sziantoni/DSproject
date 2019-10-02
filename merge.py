def merge(routes_pickup, routes_delivery, demands, cost_matrix):

    c = 0
    totalcost = 0
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
            for l in range(len(new_route)-1):
                cost+=cost_matrix[new_route[l]][new_route[l+1]]
                if new_route[l] != 0 and new_route[l] in end_route:
                    demands_pickup += demands[new_route[l] - 1]
                else:
                    if new_route[l] != 0 and new_route[l] in start_route:
                        demands_delivery += demands[new_route[l] - 1]
            c += 1
            totalcost+=cost
        if c < len(routes_delivery) + len(routes_pickup):
            for x in range(c, len(routes_pickup)):
                cost = 0
                demands_pickup = 0
                new_route = routes_pickup[x]
                l = 0
                firstZero = False
                for l in range(len(new_route)-1):
                    cost += cost_matrix[new_route[l]][new_route[l + 1]]
                    if new_route[l] != 0 and new_route[l] in new_route:
                        demands_pickup += demands[new_route[l] - 1]

                c += 1
                totalcost+=cost
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
            for l in range(len(new_route)-1):
                cost+=cost_matrix[new_route[l]][new_route[l+1]]
                if new_route[l] != 0 and new_route[l] in end_route:
                    demands_pickup += demands[new_route[l] - 1]
                else:
                    if new_route[l] != 0 and new_route[l] in start_route:
                        demands_delivery += demands[new_route[l] - 1]

            c += 1
            totalcost += cost
        if c < len(routes_delivery) + len(routes_pickup):
            for x in range(c, len(routes_delivery)):
                cost = 0
                demands_delivery = 0
                new_route = routes_delivery[x]
                l = 0
                firstZero = False
                for l in range(len(new_route)-1):
                    cost += cost_matrix[new_route[l]][new_route[l + 1]]
                    if new_route[l] != 0 and new_route[l] in new_route:
                        demands_pickup += demands[new_route[l] - 1]

                c += 1
                totalcost+=cost

    return float(totalcost)

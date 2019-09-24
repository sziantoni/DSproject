import random
def CW_S(start, savings_list, routes, capacity_limit, number_of_vehicles, demands):
   if start in routes:
       number_of_vehicles-=1
       routes.remove(start)

   if len(routes)!=0 and number_of_vehicles>0:
        for s in savings_list: #scorro lista saving
            demand=0
            if s[0] in start or s[1] in start:
                if (s[0] == start[1] or s[0] == start[len(start)-2]) and s[1] not in start:
                    nodeRadice=s[0]
                    nodeToAdd=s[1]
                    for n in start:
                        if n!=0:
                            demand += demands[n - 1]
                    demand+=demands[nodeToAdd-1]
                    if demand<= int(capacity_limit):
                        start.insert(len(start)-1, nodeToAdd)

                        for r in routes:
                            if nodeToAdd in r:
                                routes.remove(r)

                        for saving in savings_list:
                            if nodeToAdd in saving and nodeRadice in saving:
                                savings_list.remove(saving)

                        return CW_S(start, savings_list, routes, capacity_limit, number_of_vehicles,demands)

                else:
                    if (s[1] == start[1] or s[1] == start[len(start) - 2]) and s[0] not in start:
                        nodeToAdd=s[0]
                        nodeRadice=s[1]
                        for n in start:
                            if n!=0:
                                demand+=demands[n-1]
                        demand+=demands[nodeToAdd-1]
                        if demand<=int(capacity_limit) :
                            start.insert(len(start)-1, nodeToAdd)

                            for r in routes:
                                if nodeToAdd in r:
                                    routes.remove(r)

                            for saving in savings_list:
                                if nodeToAdd in saving and nodeRadice in saving:
                                    savings_list.remove(saving)

                            return CW_S(start, savings_list, routes, capacity_limit, number_of_vehicles, demands)

        if len(routes) != 0 and number_of_vehicles>0:
            savingNew=savings_list.copy()
            for n in start:
                if n!=0:
                    for s in savings_list:
                        if n in s:
                            if s in savingNew:
                                savingNew.remove(s)

            newStart=routes[0]
            return [start] + (CW_S(newStart, savingNew, routes, capacity_limit, number_of_vehicles,demands))

   else:
       return [start]






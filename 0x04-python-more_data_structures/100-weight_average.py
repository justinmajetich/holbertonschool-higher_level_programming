#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0
    prods = []
    if my_list:
        for i in my_list:
            weight += i[1]
            prods.append(i[0] * i[1])
        return (sum(prods) / weight)
    return 0

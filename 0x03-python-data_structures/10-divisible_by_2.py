#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    b = []  # b for boolean list
    for i in range(0, len(my_list)):
        if my_list[i] % 2 is 0:
            b.append(True)
        else:
            b.append(False)
    return b

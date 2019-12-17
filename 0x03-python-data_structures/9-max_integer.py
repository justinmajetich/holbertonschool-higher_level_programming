#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        x = my_list[0]
        for i in my_list[1:]:
            if i > x:
                x = i
        return x
    else:
        return None

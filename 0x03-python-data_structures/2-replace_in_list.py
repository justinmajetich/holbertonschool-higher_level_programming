#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    #  determine if valid index
    if (idx < 0) or (idx > len(my_list) - 1):
        return my_list

    #  assign new element to index
    my_list[idx] = element

    return my_list

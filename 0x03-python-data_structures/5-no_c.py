#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    [my_list.remove(i) for i in my_list if i is 'c' or i is 'C']
    my_string = ''.join(my_list)
    return my_string

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i, elem in enumerate(my_list):
        try:
            if i < x:
                print(elem, end='')
            else:
                print('')
                return i
        except IndexError:
            None
    print('')
    return i + 1

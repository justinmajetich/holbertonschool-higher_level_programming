#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            printed += 1
        except (TypeError, ValueError):
            None
    print('')
    return printed

#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(i, a_dictionary[i])) for i in sorted(a_dictionary)]

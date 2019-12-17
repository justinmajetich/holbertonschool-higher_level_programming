#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_tuple = []
    for x in range(0, 2):
        if len(tuple_a) > x:
            a = tuple_a[x]
        else:
            a = 0
        if len(tuple_b) > x:
            b = tuple_b[x]
        else:
            b = 0
        sum_tuple.append(a + b)
    return tuple(sum_tuple)

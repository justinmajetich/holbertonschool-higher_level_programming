#!/usr/bin/python3
"""Adds two numbers and returns sum"""


def add_integer(a, b=98):
    """Adds two numbers and returns sum

    Parameters:
        a: integer/float to add
        b: integer/float to add

    Returns:
        The sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    return int(a) + int(b)

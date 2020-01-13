#!/usr/bin/python3
"""This module prints a square to given dimensions"""


def print_square(size):
    """Prints a square to user-defined dimensions

    Non-integers and arguments less than 0 will raise errors.

    Args:
        size: dimensions of square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for row in range(size):
        print('#' * size)

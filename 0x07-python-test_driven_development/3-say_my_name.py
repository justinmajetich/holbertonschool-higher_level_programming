#!/usr/bin/python3
"""This module prints the name passed in by user"""


def say_my_name(first_name, last_name=""):
    """Prints a name

    Both arguments passed must be strings

    Args:
        first_name: first name
        last_name: last name (optional)
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))

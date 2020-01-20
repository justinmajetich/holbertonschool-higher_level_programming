#!/usr/bin/python3
"""Module defines a function testing object as instance of class"""


def is_same_class(obj, a_class):
    """Tests is object is exactly instance of class

    Arguments:
        obj: object to test
        class: class to test against
    """
    if type(obj) == a_class:
        return True
    else:
        return False

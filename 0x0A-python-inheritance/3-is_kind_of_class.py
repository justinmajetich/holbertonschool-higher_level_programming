#!/usr/bin/python3
"""Module defines a function testing object as instance of class."""


def is_kind_of_class(obj, a_class):
    """Test if object is of given class or of class inherited
    from given class.

    Arguments:
        obj: object to test
        class: class to test against
    """
    return isinstance(obj, a_class)

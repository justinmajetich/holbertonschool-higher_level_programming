#!/usr/bin/python3
"""Module defines a function testing if object inherited from given class."""


def inherits_from(obj, a_class):
    """Test if object is of class inheritting given class.

    Arguments:
        obj: object to test
        class: class to test against
    """
    if issubclass(obj.__class__, a_class) is True:
        if obj.__class__ is not a_class:
            return True
    else:
        return False

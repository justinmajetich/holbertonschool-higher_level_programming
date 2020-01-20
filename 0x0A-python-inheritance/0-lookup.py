#!/usr/bin/python3
"""This module returns a list of all avialable attributes
and methods in a class
"""


def lookup(obj):
    """Return available class methods/attributes"""
    return dir(obj)

#!/usr/bin/python3
"""Inherit list class to new class with sorted print method"""


class MyList(list):
    """This class inherits from list and ammends with sorted print method"""
    def print_sorted(self):
        """Print list sorted in ascending order"""
        print(sorted(self))

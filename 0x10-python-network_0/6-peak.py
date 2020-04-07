#!/usr/bin/python3
"""Find peak in list of unsorted integers
"""


def find_peak(list_of_integers):
    """Find peak in unsorted list
    """
    loi = list_of_integers
    size = len(loi)

    if size == 0:
        return None

    if size is 1:
        return loi[0]

    mid = int((size - 1) / 2)


def recurse(loi, left, right):
    """Recursive component
    """
    mid = int((left + right) / 2)

    # recurse left
    if (mid - 1 >= 0) and loi[mid - 1] > loi[mid]:
        return recurse(loi, left, mid - 1)
    # recurse right
    elif (mid + 1 <= len(loi)) and loi[mid + 1] > loi[mid]:
        return recurse(loi, mid + 1, right)
    # peak found
    else:
        return loi[mid]

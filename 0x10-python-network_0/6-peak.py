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

    return recurse(loi, 0, size - 1)


def recurse(loi, left, right):
    """Recursive component
    """
    mid = int((left + right) / 2)

    if left > right:
        return loi[mid]

    if (mid == 0 or loi[mid] > loi[mid - 1])\
       and (mid == len(loi) - 1 or loi[mid] > loi[mid + 1]):
        return loi[mid]

    # recurse left
    elif (mid > 0) and loi[mid - 1] > loi[mid]:
        return recurse(loi, left, mid - 1)
    else:  # recurse right
        return recurse(loi, mid + 1, right)

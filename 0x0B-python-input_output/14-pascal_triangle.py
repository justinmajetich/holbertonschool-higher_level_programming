#!/usr/bin/python3
"""This module defines a function that creates a Pascal triangle
"""


def pascal_triangle(n):
    """Return a Pascal's triangle
    """
    if n <= 0:
        return []

    # create list triangle
    tri = [[1 for i in range(j + 1)] for j in range(n)]

    for row_n, row in enumerate(tri):
        for col in range(len(row) - 1):
            if col is 0:  # skip [n][0] index
                continue
            tri[row_n][col] = tri[row_n - 1][col - 1] + tri[row_n - 1][col]
    return tri

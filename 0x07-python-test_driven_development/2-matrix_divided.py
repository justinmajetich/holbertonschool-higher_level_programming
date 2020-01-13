#!/usr/bin/python3
"""This module will divide the elements of a matrix by a given divisor,
 appending the quotient to a new matrix"""


def matrix_divided(matrix, div):
    """Divide elements of matrix by div.

    Matrix elements and divisors must be integers or floats.

    Parameters:
        matrix: matrix to divide
        div: divisor
    """
    if type(div) is not float and type(div) is not int:  # check div type
        raise TypeError('div must be a number')
   
    if div == 0:
        raise ZeroDivisionError('division by zero')

    x = len(matrix)  # take number of rows
    ref_row = 0
    if x is not 0 and type(matrix[x - 1]) is list and len(matrix[x - 1]) > 0:
        ref_row = len(matrix[x - 1])  # use last row as reference
        n_matrix = [[] for row in range(x)]
    else:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')

    for row, n_row in zip(matrix, n_matrix):  # check element types
        if type(row) is not list:  # check that list member is list
            raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
        if len(row) != ref_row:  # check for uniform rows
            raise TypeError('Each row of the matrix must have the same size')
        for elem in row:
            if type(elem) is not float and type(elem) is not int:  # check types
                raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
            n_row.append(round(float(elem / div), 2))  # divide elements by div

    return n_matrix

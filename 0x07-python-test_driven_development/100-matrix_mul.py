#!/usr/bin/python3
"""Multiply two matrices against one another"""


def matrix_mul(m_a, m_b):  # must be list
    """Multiply two matrices, element by element
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    for item_a, item_b in zip(m_a, m_b):  # must be list of lists
        if type(item_a) is not list:
            raise TypeError('m_a must be a list of lists')
        if type(item_b) is not list:
            raise TypeError('m_b must be a list of lists')

    if len(m_a) is 0:  # check for empty lists
        raise ValueError('m_a can\'t be empty')
    else:
        for row in m_a:
            if len(row) is 0:
                raise ValueError('m_a can\'t be empty')
    if len(m_b) is 0:
        raise ValueError('m_b can\'t be empty')
    else:
        for row in m_b:
            if len(row) is 0:
                raise ValueError('m_b can\'t be empty')

    for item_a, item_b in zip(m_a, m_b):  # elems can only be float/int
        for elem_a, elem_b in zip(item_a, item_b):
            if type(elem_a) is not float and type(elem_a) is not int:
                raise TypeError('m_a should contain only integers or floats')
            if type(elem_b) is not float and type(elem_b) is not int:
                raise TypeError('m_b should contain only integers or floats')

    len_a = len(m_a[0])  # uniform rows
    len_b = len(m_b[0])
    for row_a, row_b in zip(m_a, m_b):
        if len(row_a) is not len_a:
            raise TypeError('each row of m_a must be of the same size')
        if len(row_b) is not len_b:
            raise TypeError('each row of m_b must be of the same size')

    m_p = [[0 for elem in range(len_b)]
           for row in range(len(m_a))]  # match m_a rows

    # perform multiplication
    for row_a in range(len(m_a)):
        for elem_b in range(len_b):
            for row_b in range(len(m_b)):
                m_p[row_a][elem_b] += m_a[row_a][row_b] * m_b[row_b][elem_b]

    return m_p

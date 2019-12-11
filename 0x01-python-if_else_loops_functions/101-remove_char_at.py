#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):  # if position is outside indices
        return str

    array = list(str)  # convert to list for mutability

    for i in range(0, len(str) - 1):
        if i >= n:
            array[i] = array[i + 1]  # shift contents left

    result = ''.join(array)  # join elements into string
    return result[:-1]  # truncate word by one character

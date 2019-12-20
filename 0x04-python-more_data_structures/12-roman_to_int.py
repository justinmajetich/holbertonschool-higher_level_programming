#!/usr/bin/python3
def roman_to_int(roman_string):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    skip = 0
    if roman_string is None or type(roman_string) is not str:
        return 0
    for i, letter in enumerate(roman_string):  # iterate through string
        if skip is 0:
            if letter in d:  # if letter exists in dict
                if i < (len(roman_string) - 1):  # letter is not last in string
                    if d[letter] < d[roman_string[i + 1]]:
                        number += (d[roman_string[i + 1]] - d[letter])
                        skip = 1
                        continue
                    else:
                        number += d[letter]
                else:  # if letter is last in string
                    number += d[letter]
            else:
                return 0
        skip = 0
    return number

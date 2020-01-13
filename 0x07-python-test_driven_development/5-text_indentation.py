#!/usr/bin/python3
"""This module prints formatted text"""


def text_indentation(text):
    """Prints formatted text

    Text is parsed and printed line by line (a line is defined as
    a '.', '?' or ':' terminated portion of text). Each line of text
    will be printed with no white space at either end, though each will
    be followed by two newlines. Non-string arguments will raise
    a TypeError.

    Args:
        text: text to be parsed and printed
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    in_line = 0  # flag to determine when line is being printed
    for c in text:
        if (c is ' ' or c is '\t') and in_line is 0:
            continue
        print(c, end='')
        in_line = 1  # set flag to denote active line printing
        if c is '.' or c is '?' or c is ':':
            print('\n')
            in_line = 0  # set flag to denote delimiting whitespace

#!/usr/bin/python3
"""This module defines a function to append string to file"""


def append_write(filename="", text=""):
    """Append text to file and return characters written

    Arguments:
        filename: file to append
        text: text to append to file
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)

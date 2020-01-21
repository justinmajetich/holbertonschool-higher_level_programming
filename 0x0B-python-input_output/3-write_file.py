#!/usr/bin/python3
"""This module defines a function to write to file"""


def write_file(filename="", text=""):
    """Writes string to text file
    Arguments:
        filename: name of file to write to
        text: string to write to file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)

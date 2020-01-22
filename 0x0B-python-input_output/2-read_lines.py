#!/usr/bin/python3
"""This module defines a function the reads and prints n lines from file"""


def read_lines(filename="", nb_lines=0):
    """Read and print n lines from file
    Arguments:
        filename: file to read from
        nb_lines: number of lines to read/print
    """
    line_count = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line_count, lines in enumerate(f):
            pass
        if nb_lines <= 0 or nb_lines > (line_count + 1):
            f.seek(0)
            print(f.read(), end='')
        else:
            f.seek(0)  # return to file beginning
            for line in range(nb_lines):
                print(f.readline(), end='')

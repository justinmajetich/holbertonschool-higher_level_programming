#!/usr/bin/python3
"""This module defines a function to count lines read from file"""


def number_of_lines(filename=""):
    """Return number of lines read"""
    line_count = 0
    with open(filename, mode='r', encoding='UTF-8') as f:
        for line in f:
            line_count += 1
    return line_count

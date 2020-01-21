#!/usr/bin/python3
"""This module defines a function to read files"""


def read_file(filename=""):
    """Reads a file and prints to stdout"""
    with open(filename, mode='r', encoding='utf-8') as fs:
        print(fs.read(), end='')

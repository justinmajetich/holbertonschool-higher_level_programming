#!/usr/bin/python3
"""This module defines a function that writes an object to text file"""


def save_to_json_file(my_obj, filename):
    """Writes object to text file using JSON representation

    Arguments:
        my_obj: onject to write
        filename: file to write to
    """
    import json
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)

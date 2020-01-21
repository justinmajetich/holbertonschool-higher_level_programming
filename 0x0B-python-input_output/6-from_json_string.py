#!/usr/bin/python3
"""This module defines a function that returns an object represented by JSON"""


def from_json_string(my_str):
    """Return object represented by JSON string

    Arguments:
        my_str: JSON string
    """
    import json
    return json.loads(my_str)

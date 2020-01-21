#!/usr/bin/python3
"""This module defines a function that returns a json representation"""


def to_json_string(my_obj):
    """Return json representation of object"""
    import json
    return json.dumps(my_obj)

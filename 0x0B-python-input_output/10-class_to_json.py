#!/usr/bin/python3
"""This module defines a function which returns dict description
for JSON-serialized object
"""


def class_to_json(obj):
    """Return dictionary description for JSON object serialization

    Argument:
        obj: object to serialize
    """
    return obj.__dict__

#!/usr/bin/python3
"""This module defines a function which returns dict description
for JSON-serialized object
"""


def class_to_json(obj):
    """Return dictionary description for JSON object serialization

    Argument:
        obj: object to serialize
    """
    import json
    return json.loads(json.dumps(obj.__dict__))

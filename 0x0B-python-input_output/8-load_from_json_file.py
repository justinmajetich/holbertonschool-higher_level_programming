#!/usr/bin/python3
"""This module defines function to create object from JSON file"""


def load_from_json_file(filename):
    """Create object from JSON file"""
    import json
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)

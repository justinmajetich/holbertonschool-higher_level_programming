#!/usr/bin/python3
"""This module defines a function which compiles all args into file"""


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
import sys
args = sys.argv

obj = load_from_json_file(args[0])

for arg in args[1:]:
    obj.append(arg)

save_to_json_file(f, 'add_item.json')

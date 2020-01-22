#!/usr/bin/python3
"""This module defines a function which compiles all args into file"""


import sys
import os
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
args = sys.argv

if not os.path.exists('add_item.json'):
    with open('add_item.json', mode='w', encoding='utf-8') as f:
        f.write('[]')

obj = load_from_json_file('add_item.json')

for arg in args[1:]:
    obj.append(arg)

save_to_json_file(obj, 'add_item.json')

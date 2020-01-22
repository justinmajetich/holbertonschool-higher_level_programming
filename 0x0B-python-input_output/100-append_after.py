#!/usr/bin/python3
"""This module defines a function to search and update a text file
"""


def append_after(filename="", search_string="", new_string=""):
    """Search lines for keyword and insert new linw on match
    """
    line_list = []
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as f:
            f.writelines(line_list)

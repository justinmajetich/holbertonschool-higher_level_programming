#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    hit_list = []
    for key, val in a_dictionary.items():
        if val is value:
            hit_list.append(key)
    if len(hit_list) > 0:
        for hits in hit_list:
            del a_dictionary[hits]
    return a_dictionary

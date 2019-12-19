#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for k, v in reversed(sorted(a_dictionary.items())):
            return k

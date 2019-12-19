#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v is max(a_dictionary.values()):
                return k
    else:
        return None

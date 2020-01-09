#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except Exception as message:
        print('Exception:', message, file=stderr)
        return None

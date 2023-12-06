#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    for x in keys:
        if a_dictionary[x] == value:
            del a_dictionary[x]
    return a_dictionary

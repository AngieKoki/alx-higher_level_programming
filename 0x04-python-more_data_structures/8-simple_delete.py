#!/usr/bin/python3

# Deletes a key in a dictionary

def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary.keys():
        return (a_dictionary)
    a_dictionary.pop(key)
    return (a_dictionary)

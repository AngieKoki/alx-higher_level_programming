#!/usr/bin/python3

# Returns a new dictionary with all values multiplies by 2

def multiply_by_2(a_dictionary):
    new_dict = (key: value for key, value in a_dictionary)
    for i in new_dict:
        new_dict[i] *= 2
    return (new_dict)

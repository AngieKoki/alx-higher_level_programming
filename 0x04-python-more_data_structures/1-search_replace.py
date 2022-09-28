#!/usr/bin/python3

# Replaces all occurrences of an element by another in a new list

def search_replace(my_list, search, replace):
    new = []
    for item in my_list:
        if item == search:
            item = replace
        new.append(item)
    return(new)

#!/usr/bin/python3
#Replacing elements of a list at a specific index

def replace_in_list(my_list, idx, element):
    len_list = len(my_list)
    if (idx < 0 or idx > len_list - 1):
        return my_list
    my_list[idx] = element
    return my_list

#!/user/bin/python3

# Returns a set of all elements present in only one set

def only_diff_elements(set1, set2):
    difference = set1.symmetric_difference(set2)
    return (difference)

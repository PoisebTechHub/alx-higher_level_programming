#!/usr/bin/python3

# Write a function that replaces an element in a list
# at a specific position without modification.
def new_in_list(my_list, idx, element):
    node = my_list[:]
    if idx < 0:   # when idx is negative return list
        return node
    if idx > len(my_list) - 1:   # when idx is greater than elements in list
        return node    # retun node list
    node[idx] = element   # Replacing element in list node
    return node

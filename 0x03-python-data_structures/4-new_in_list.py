#!/usr/bin/python3

# Write a function that replaces an element in a list
# at a specific position without modification.
def new_in_list(my_list, idx, element):
    if idx < 0:   # when idx is negative return list
        return my_list
    if idx > len(my_list) - 1:   # when idx is greater than elements in list
        return my_list    # retun list
    my_list[idx] = element   # Replacing element in list
    return my_list

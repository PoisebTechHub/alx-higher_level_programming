#!/usr/bin/python3

# Write a function that replaces an element of a list
# at a specific position like in C.

def replace_in_list(my_list, idx, element):
    # Return to original list if idx is negative
    if idx < 0:
        return my_list
    # Return the original list if idx is out of range
    if idx > len(my_list):
        return my_list
    # Replacing the element at specified position
    my_list[idx] = element
    return my_list

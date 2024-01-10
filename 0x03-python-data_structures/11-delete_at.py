#!/usr/bin/python3

# Writing a function that deletes the item at a specific position in a list
def delete_at(my_list=[], idx=0):   # prototype of function
    if idx < 0:   # if item idx is negative, return the list
        return my_list
    elif idx > len(my_list) - 1:  # return list, if item is out of range
        return my_list
    del my_list[idx]  # deleting item in list as required
    return my_list

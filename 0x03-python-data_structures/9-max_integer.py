#!/usr/bin/python3

def max_integer(my_list=[]):
    # Finding the biggest integer of list
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for k in range(len(my_list)):
        if my_list[k] > big:
            big = my_list[k]
            return (big)

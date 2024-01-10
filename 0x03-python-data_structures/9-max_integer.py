#!/usr/bin/python3

# Writing a function that finds the biggest interger of a list
def max_integer(my_list=[]):   # Prototype of function
    if len(my_list) == 0:   # Making the list empty
        return (None)

    big = my_list[0]   # Accessing thr big integers in the list
    for k in range(len(my_list)):
        if my_list[k] > big:
            big = my_list[k]
            return (big)

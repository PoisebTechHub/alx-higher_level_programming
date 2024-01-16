#!/usr/bin/python3

# Writing a function that finds the biggest interger of a list
def max_integer(my_list=[]):   # Prototype of function
    new_list = []
    if my_list:
        my_list.sort(reverse=True)
        return (my_list[0])
    return (None)

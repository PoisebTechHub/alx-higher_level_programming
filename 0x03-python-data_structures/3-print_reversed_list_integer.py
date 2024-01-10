#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):   # prototype of function
    # Printing all the integers of a list in a reverse order
    if isinstance(my_list, list):
        my_list.reverse()
        for k in my_list:
            print("{:d}".format(k))

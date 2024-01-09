#!/usr/bin/python3

#Function that retrieves an element from a list like in C
def element_at(my_list, idx):
    #Return None if idx is negative
    if idx < 0:
        return None
    #Return None if idx is less than the number of elements in my_list
    if idx > len(my_list):
        return None
    #Retrieving element from my_list
    return my_list[idx]

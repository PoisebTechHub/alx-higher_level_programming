#!/usr/bin/python3

# Writing a function that finds all multiples of 2 in a list
def divisible_by_2(my_list=[]):
    length = len(my_list)
    multiples = []   # accessing all multiple integers in list
    for k in range(length):  # integers k in the elements of list
        if my_list[k] % 2 == 0:   # checking if integers k is multiples of 2
            multiples.append(True)   # adding True if k is multiples of 2
        else:
            multiples.append(False)   # adding False if otherwise
            return (multiples)   # returning all multiples of 2

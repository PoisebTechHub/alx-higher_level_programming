#!/usr/bin/python3

'''Write a function that deletes keys with
a specific value in a dictionary.'''


def complex_delete(a_dictionary, value):
    net = a_dictionary.copy()
    for m, v in net.items():
        if value == v:
            a_dictionary.pop(m)
    return a_dictionary

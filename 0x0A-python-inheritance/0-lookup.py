#!/usr/bin/python3

"""
Write a function that returns the list of available
attributes and methods of an object:

1. Prototype: def lookup(obj):
2. Returns a list object
3. You are not allowed to import any module

Below is the solution
"""


def lookup(obj):
    """ Return lists of available attributes and methods of an obj """
    return dir(obj)

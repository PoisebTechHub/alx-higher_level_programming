#!/usr/bin/python3

"""
Write a function that returns True if the object is exactly an
instance of the specified class ; otherwise False.

1. Prototype: def is_same_class(obj, a_class):
2. You are not allowed to import any module

Below is the solution
"""


def is_same_class(obj, a_class):
    """ T or F for the instance of an obj of a class """
    if type(obj) is a_class:
        return True
    else:
        return False

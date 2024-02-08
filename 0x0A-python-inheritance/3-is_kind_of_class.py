#!/usr/bin/python3

"""
Write a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.

1. Prototype: def is_kind_of_class(obj, a_class):
2. You are not allowed to import any module

Below is the solution
"""


def is_kind_of_class(obj, a_class):
    """ T or F if obj is an instance of a class """
    if isinstance(obj, a_class):
        return True
    else:
        return False

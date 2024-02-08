#!/usr/bin/python3

"""
Write a function that returns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.

1. Prototype: def inherits_from(obj, a_class):
2. You are not allowed to import any module

Below is the solution
"""


def inherits_from(obj, a_class):
    """ is an obj a subclass of the specified class """
    if type(obj) is a_class:
        return False
    elif issubclass(type(obj), a_class):
        return True
    else:
        return False

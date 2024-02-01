#!/usr/bin/python3

'''
Write a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance
attributes, except if the new instance attribute is called
first_name.
1. You are not allowed to import any module

Below is the solution
'''


"""Defining locked class"""


class LockedClass:
    """
    This prevents the user from instantiating new LockedClass
    attributes for anything but attributes called 'first_name'
    """

    __slots__ = ["first_name"]

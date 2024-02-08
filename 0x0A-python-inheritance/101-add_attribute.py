#!/usr/bin/python3

"""
Write a function that adds a new attribute to an object if it’s possible:

1. Raise a TypeError exception, with the message can't add new
attribute if the object can’t have new attribute
2. You are not allowed to use try/except
3. You are not allowed to import any module

Below is the slution
"""


def add_attribute(obj, att, value):
    """Adding a new attribute to an object if possible.

    Args:
        obj (any): Object to add an attribute to.
        att (str): Name of the attribute to add to obj.
        value (any): Value of att.
    Raises:
        TypeError: The attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

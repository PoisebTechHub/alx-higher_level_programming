#!/usr/bin/python3

"""
Write a function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and
boolean) for JSON serialization of an object:

1. Prototype: def class_to_json(obj):
2. obj is an instance of a Class
3. All attributes of the obj Class are serializable:
list, dictionary, string, integer and boolean
4. You are not allowed to import any module

Below is the solution
"""


def class_to_json(obj):
    """Returning the dictionary represntation of a simple data structure."""
    return obj.__dict__

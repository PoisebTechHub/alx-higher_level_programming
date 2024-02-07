#!/usr/bin/python3

"""
Write a function that returns the JSON
representation of an object (string):

1. Prototype: def to_json_string(my_obj):
2. You don’t need to manage exceptions if
the object can’t be serialized.

Below is the solution
"""
import json


def to_json_string(my_obj):
    """Returning the JSON representation of a string object."""
    return json.dumps(my_obj)

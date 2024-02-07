#!/usr/bin/python3
# 6-from_json_string.py

"""
Write a function that returns an object (Python data structure)
represented by a JSON string:

1. Prototype: def from_json_string(my_str):
2. You don’t need to manage exceptions if the
JSON string doesn’t represent an object.

Below is the solution
"""
import json


def from_json_string(my_str):
    """Returning the Python object representation of a JSON string."""
    return json.loads(my_str)

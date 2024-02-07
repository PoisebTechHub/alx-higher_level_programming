#!/usr/bin/python3

"""
Write a function that creates an Object from a “JSON file”:

1. Prototype: def load_from_json_file(filename):
2. You must use the with statement
3. You don’t need to manage exceptions if the
JSON string doesn’t represent an object.
4. You don’t need to manage file permissions / exceptions.

Below is the solution
"""

import json


def load_from_json_file(filename):
    """Creating a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)

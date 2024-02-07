#!/usr/bin/python3

"""
Write a function that writes an Object to a text file,
using a JSON representation:

1. Prototype: def save_to_json_file(my_obj, filename):
2. You must use the with statement
3. You don’t need to manage exceptions if the object
can’t be serialized.
4. You don’t need to manage file permission exceptions.

Below is the solution
"""
import json


def save_to_json_file(my_obj, filename):
    """Writing an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

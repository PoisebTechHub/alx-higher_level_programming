#!/usr/bin/python3

"""
Write a script that adds all arguments to a Python list,
and then save them to a file:

1. You must use your function save_to_json_file
from 5-save_to_json_file.py
2. You must use your function load_from_json_file
from 6-load_from_json_file.py
3. The list must be saved as a JSON representation
in a file named add_item.json
4. If the file doesn’t exist, it should be created
5. You don’t need to manage file permissions / exceptions.

Below is the solution
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")

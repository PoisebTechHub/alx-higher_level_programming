#!/usr/bin/python3

"""
Write a function that inserts a line of text to a file, after each line
containing a specific string (see example):

1. Prototype: def append_after(filename="", search_string="", new_string=""):
2. You must use the with statement
3. You don’t need to manage file permission or file doesn't exist exceptions.
4. You are not allowed to import any module

Below is the solution
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserting text after each line containing a given string in a file.

    Args:
        filename (str): Name of the file.
        search_string (str): String to search for within the file.
        new_string (str): String to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

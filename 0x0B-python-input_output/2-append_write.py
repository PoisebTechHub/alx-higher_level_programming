#!/usr/bin/python3

"""
Write a function that appends a string at the end of a
text file (UTF8) and returns the number of characters added:

1. Prototype: def append_write(filename="", text=""):
2. If the file doesn’t exist, it should be created
3. You must use the with statement
4. You don’t need to manage file permission or file
doesn't exist exceptions.
5. You are not allowed to import any module

Below is the solution
"""


def append_write(filename="", text=""):
    """Appending a string to the end of a UTF8 text file.

    Args:
        filename (str): Name of the file to append to.
        text (str): String to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3

''' Write a function that replaces all occurrences
of an element by another in a new list '''


def search_replace(my_list, search, replace):
    return [replace if search == k else k for k in my_list]

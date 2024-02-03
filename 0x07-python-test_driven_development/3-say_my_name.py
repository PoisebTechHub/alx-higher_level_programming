#!/usr/bin/python3

'''
Write a function that prints My name is <first name> <last name>
1. Prototype: def say_my_name(first_name, last_name=""):
2. first_name and last_name must be strings otherwise,
raise a TypeError exception with the message first_name
must be a string or last_name must be a string
3. You are not allowed to import any module

Below is the solution
'''


def say_my_name(first_name, last_name=""):

    """ this function prints a name """

    if type(first_name) != str:
        TypeError("first_name must be a string")
    elif last_name and type(last_name) != str:
        TypeError("last_name must be a string")
    elif last_name is None:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))

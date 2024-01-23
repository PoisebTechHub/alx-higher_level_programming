#!/usr/bin/python3

'''
Writing a function that prints an integer.
1. Prototype: def safe_print_integer_err(value):
2. value can be any type (integer, string, etc.)
3. The integer should be printed followed by a new line
4. Returns True if value has been correctly printed
(it means the value is an integer)
5. Otherwise, returns False and prints in stderr
the error precede by Exception:
6. You have to use try: / except:
7. You have to use "{:d}".format() to print as integer
8. You are not allowed to use type()
Below is the solution
'''

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)

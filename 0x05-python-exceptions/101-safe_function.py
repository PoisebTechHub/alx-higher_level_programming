#!/usr/bin/python3

'''
Writing a function that executes a function safely.
1. You can assume fct will be always a pointer to a function
2. Returns the result of the function,
3. Otherwise, returns None if something happens during the function
4. and prints in stderr the error precede by Exception:
5. You have to use try: / except:
Below is the solution
'''
import sys


def safe_function(fct, *args):   # prototype of function
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None

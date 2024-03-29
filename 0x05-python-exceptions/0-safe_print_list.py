#!/usr/bin/python3

'''
Writing a function that prints x elements of a list
1. Prototype: def safe_print_list(my_list=[], x=0):
2. my_list can contain any type (integer, string, etc.)
3. All elements must be printed on the same line
followed by a new line.
4. x represents the number of elements to print
5. x can be bigger than the length of my_list
6. Returns the real number of elements printed
7. You have to use try: / except:
8. You are not allowed to import any module
9. You are not allowed to use len()
Below is the solution
'''


def safe_print_list(my_list=[], x=0):
    """Printing x elememts of a list.

    Args:
        my_list (list): List to print elements from
        x (int): Number of elements of my_list to print

    Returns:
        Number of elements printed
    """
    ret = 0
    for k in range(x):
        try:
            print("{}".format(my_list[k]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)

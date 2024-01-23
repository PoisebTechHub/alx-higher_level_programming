#!/usr/bin/python3

'''
Writing a function that divides element by element 2 lists.
1. Prototype: def list_division(my_list_1, my_list_2, list_length):
2. my_list_1 and my_list_2 can contain any type (integer, string, etc.)
3. list_length can be bigger than the length of both lists
4. Returns a new list (length = list_length) with all divisions
5. If 2 elements can’t be divided, the division result should be equal to 0
6. If an element is not an integer or float: print: wrong type
7. If the division can’t be done (/0): print: division by 0
8. If my_list_1 or my_list_2 is too short print: out of range
9. You have to use try: / except: / finally:
10. You are not allowed to import any module
Below is the solution
'''


def list_division(my_list_1, my_list_2, list_length):
    """Division of two lists element by element.
    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to be divided.
    Returns:
        A new list containing all divisions of list_length.
    """
    new_list = []
    for k in range(0, list_length):
        try:
            div = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)

#!/usr/bin/python3

# Write a function that removes all characters c and C from a string
def no_c(my_string):  # Prototype given
    if my_string[:]:
        new_string = my_string.translate({ord("c"): None})
        second_string = new_string.translate({ord("C"): None})
            return second_string
        return my_string

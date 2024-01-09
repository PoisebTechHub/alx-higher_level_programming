#!/usr/bin/python3

# Write a function that returns a tuple with the length of a string
# and its first character

def multiple_returns(sentence):
    # Returning the length of a string and the first character
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

#!/usr/bin/python3

''' Create a function def roman_to_int(roman_string):
    that converts a Roman numeral to an integer '''


def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [data[k] for k in roman_string] + [0]
    net = 0

    for m in range(len(numbers) - 1):
        if numbers[m] >= numbers[m+1]:
            net += numbers[m]
        else:
            net -= numbers[m]

    return net

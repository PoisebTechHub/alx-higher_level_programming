#!/usr/bin/python3

"""
Write a class MyInt that inherits from int:

1. MyInt is a rebel. MyInt has == and != operators inverted
2. You are not allowed to import any module

Below is the solution
"""


class MyInt(int):
    """Inverting  int operators == and !=."""

    def __eq__(self, value):
        """Overriding  == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value

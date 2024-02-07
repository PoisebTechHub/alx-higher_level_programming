#!/usr/bin/python3

"""
Write a class Student that defines a student by:

1. Public instance attributes:
first_name
last_name
age
2. Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
3. Public method def to_json(self): that retrieves a dictionary
representation of a Student instance (same as 8-class_to_json.py)
4. You are not allowed to import any module

Below is the solution
"""


class Student:
    """Representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing a new Student.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Getting a dictionary representation of the Student."""
        return self.__dict__

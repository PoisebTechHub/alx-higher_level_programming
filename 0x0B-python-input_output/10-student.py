#!/usr/bin/python3

"""
Write a class Student that defines a student by: (based on 9-student.py)

1. Public instance attributes:
first_name
last_name
age
2. Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
3. Public method def to_json(self, attrs=None):
that retrieves a dictionary representation of a Student
instance (same as 8-class_to_json.py):
4. If attrs is a list of strings, only attribute names
contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
5. You are not allowed to import any module

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

    def to_json(self, attrs=None):
        """Getting a dictionary representation of the Student.

        If attrs is list of strings, representing only those attributes
        included in the list.

        Args:
            attrs (list): Optional - The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

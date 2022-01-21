#!/usr/bin/python3
"""module for student class"""


class Student:
    """class for students"""
    def __init__(self, first_name, last_name, age):
        """initializes a student

        Args:
            first_name(str): students first name
            last_name(str): students last name
            age(int): students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary for student"""
        return self.__dict__

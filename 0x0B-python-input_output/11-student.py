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

    def to_json(self, attrs=None):
        """returns dictionary for student

        Args:
            attr(list): list of attributes to return
        """
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            my_dict = {}
            for item in self.__dict__:
                if item in attrs:
                    my_dict[item] = self.__dict__[item]
            return my_dict

    def reload_from_json(self, json):
        """changes student info based on json dictionary

        Arg:
            json(dict): dictionary of info changed
        """
        for item in json:
            if item in self.__dict__:
                self.__dict__[item] = json[item]

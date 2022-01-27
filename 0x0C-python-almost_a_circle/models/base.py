#!/usr/bin/python3
"""module that contains base class"""

import json


class Base:
    """base class"""
    __nb_objects = 0

    def __ini__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list of dictionaries -> json format"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json format from list_objs to type.json file"""
        name = cls.__name__ + ".json"
        with open(name, "w+") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                lst = []
                for o in list_objs:
                    lst.append(o.to_dictionary())
                f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """returns obj from json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a new object from given info"""
        if cls.__name__ == "Rectangle":
            dump = cls(1, 1, 0, 0)
        if cls.__name__ == "Square":
            dump = cls(1, 0, 0)
        dump.update(**dictionary)
        return dump

    @classmethod
    def load_from_file(cls):
        """returns object from data stored in json format in type.json file"""
        filename = cls.__name__ + ".json"
        objlist = []
        try:
            with open(filename, "r") as f:
                jsonlist = cls.from_json_string(f.read())
                for j in jsonlist:
                    objlist.append(cls.create(**j))
                    return objlist
        except FileNotFoundError:
            return []

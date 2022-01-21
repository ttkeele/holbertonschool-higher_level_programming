#!/usr/bin/python3
"""module converts JSON to object"""


import json


def from_json_string(my_str):
    """converts a json to an object

    Arg:
        my_obj(obj): object to be converted
    """
    return json.loads(my_str)

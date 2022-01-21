#!/usr/bin/python3
"""module that converts object to JSON"""


import json


def to_json_string(my_obj):
    """converts an object to json

    Arg:
        my_obj(obj): object to be converted
    """
    return json.dumps(my_obj)

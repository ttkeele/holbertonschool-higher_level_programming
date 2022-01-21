#!/usr/bin/python3
"""module that loads JSON file and creates an object"""


import json


def load_from_json_file(filename):
    """creates object from JSON file

    Arg:
        filename(str): file to load from
    """
    with open(filename) as f:
        return json.loads(f.read())

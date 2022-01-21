#!/usr/bin/python3
"""module saves object to file as JSON string"""


import json


def save_to_json_file(my_obj, filename):
    """saves object as JSON in a file

    Args:
        my_obj(obj): object to jsonify and save
        filename(str): name of file to write to
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))

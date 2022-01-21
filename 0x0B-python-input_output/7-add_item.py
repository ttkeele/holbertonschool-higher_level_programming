#!/usr/bin/python3
"""module that adds all arguments to python list,
and then saves them to JSON file
"""


from sys import argv
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def create_list():
    """adds command line arguments to a list in JSON file"""
    try:
        my_list = load_from_json_file("add_item.json")
    except:
        my_list = []
    my_list += argv[1:]
    save_to_json_file(my_list, "add_item.json")

if __name__ == "__main__":
    create_list()

#!/usr/bin/python3
"""module appends text to file"""


def append_write(filename="", text=""):
    """function that writes to file appending
    text if file is present

    Args:
        filename(str): name of file written to
        text(str): info to write to file
    """
    with open(filename, "a") as f:
        return f.write(text)

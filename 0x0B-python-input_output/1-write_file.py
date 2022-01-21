#!/usr/bin/python3
"""module that writes to a file"""


def write_file(filename="", text=""):
    """function that writes to file creating it if not present or overwriting if present

    Args:
        filename(str): name of file to be written to
        text(str): info to write to file
    """
    with open(filename, "w") as f:
        return f.write(text)

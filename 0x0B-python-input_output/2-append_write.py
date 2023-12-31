#!/usr/bin/python3
"""Defines file-appending function"""


def append_write(filename="", text=""):
    """Appends string to the end of a UTF8 text file

    Args:
        filename (str): Name of the file to append to
        text (str): str to append to the file
    Returns:
        number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

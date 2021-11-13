#!/usr/bin/python3
"""Tests for the AirBnb clone modules.
"""
import os


def read_text_file(file_name):
    """Reads the contents of a given file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The contents of the file if it exists.
    """
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            for line in file.readlines():
                lines.append(line)
    return ''.join(lines)


def write_text_file(file_name, text):
    """Writes a text to a given file.

    Args:
        file_name (str): The name of the file to write to.
        text (str): The content of the file.
    """
    with open(file_name, mode='w') as file:
        file.write(text)

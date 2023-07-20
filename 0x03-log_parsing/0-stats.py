#!/usr/bin/python3


"""
This module holds a simple module to do log
parsing. Given a input of log files, extract some
usefull information and print it to standard output
"""

import sys


def print_to_stdout(**kwargs):
    """
    A simple helper function to print
    the values to standard output
    """
    for key in kwargs.keys():
        if not isinstance(kwargs.get(key), dict):
            # Means this is not a dictionary of dictionaries
            # So Its the file size
            print("File Size {}".format(kwargs.get(key)))
        else:
            for nested_k, nested_v in key.items():
                print(f"{nested_k}: {nested_v}")

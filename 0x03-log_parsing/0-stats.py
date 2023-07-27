#!/usr/bin/python3


"""
This module holds a simple module to do log
parsing. Given a input of log files, extract some
usefull information and print it to standard output
"""

import sys
import re
def check_log_format(log_string):
    regex_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] "GET \/projects\/260 HTTP\/1\.1" \d{3} \d+'
    return re.match(regex_pattern, log_string)


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


def read_and_analyze_log_files():
    while True:
        try:
            status_codes = {
                "200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0

            }
            total_size = 0
            for time in range(11):
                log_info = input("").strip()
                if check_log_format(log_info):
                    log_info_list = log_info.split(" ")
                    f_size = log_info_list[-1]
                    s_code = log_info_list[-2]
                    status_codes[s_code] = status_codes.get(s_code) + 1
                    total_size += int(f_size)
                    sorted_keys_dict = {code: status_codes[code] for code in sorted(status_codes)}
            print_to_stdout(codes=sorted_keys_dict, size = total_size)
        except KeyboardInterrupt:
            print_to_stdout(codes=sorted_keys_dict, size = total_size)

#!/usr/bin/python3

"""
This module contains the solution to the
Inteview question of lockboxes
"""

from typing import List


def canUnlockAll(boxes: List[List]) -> bool:
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing box and keys
    Returns:
        bool: True if all the boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list):
        raise TypeError('Boxes should be a list')

    key_list = [0]
    for key in key_list:
        for j in boxes[key]:
            if j not in key_list and j < len(boxes):
                key_list.append(j)
    for i in range(len(boxes)):
        if i not in key_list:
            return False
    return True

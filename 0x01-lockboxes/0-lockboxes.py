#!/usr/bin/python3
"""
    A method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """Main method
    """
    boxsize = len(boxes)
    keys = {0}

    i = 0
    for box in boxes:
        for key in box:
            if key != i:
                keys.add(key)
        i += 1

    for x in range(boxsize):
        if x not in keys:
            return False

    return True

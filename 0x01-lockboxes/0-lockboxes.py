#!/usr/bin/python3
"""
    A method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """Main method
    """
    unlockedboxes = set()
    box = [0]

    while box:
        currentbox = box.pop()
        unlockedboxes.add(currentbox)

        for key in boxes[currentbox]:

            if key not in unlockedboxes:
                box.append(key)

    return (len(unlockedboxes) == len(boxes))

#!/usr/bin/python3
"""
    A method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """Main method
    """
    boxsize = len(boxes)
    unlockedboxes = {0}
    box = [0]

    while box:
        currentbox = box.pop()

        for key in boxes[currentbox]:
            if 0 < key < boxsize and key not in unlockedboxes:
                unlockedboxes.add(currentbox)
                box.append(key)

    return (len(unlockedboxes) == boxsize - 1)

#!/usr/bin/python3
"""LockBoxes module."""


def canUnlockAll(boxes):
    """
    canUnlockAll: Determines if all the boxes can be opened by\
        the provided keys.

    The box at index 0(zero) is unlocked by default. If it contains\
        a key to the next box, we can unlock it. If it contains a key\
        to a box that has already been unlocked, we can unlock it.

    Args:
        boxes (List[List[int]]): List of lists of keys.
    """
    unlockedBoxes = [False] * len(boxes)
    unlockedBoxes[0] = True
    keys = boxes[0]

    while len(keys) > 0:
        key = keys.pop()
        if not unlockedBoxes[key]:
            unlockedBoxes[key] = True
            keys.extend(boxes[key])

    return all(unlockedBoxes)

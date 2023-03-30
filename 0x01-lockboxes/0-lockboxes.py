#!/usr/bin/python3
"""
A module that implements lockboxes
"""
def canUnlockAll(boxes):
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = [0]
    
    while keys:
        box_index = keys.pop()
        for key in boxes[box_index]:
            if key >= len(boxes):
                continue
            if not unlocked[key]:
                unlocked[key] = True
                keys.append(key)
    
    return all(unlocked)


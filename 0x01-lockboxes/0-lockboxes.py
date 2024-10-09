#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    # Initialize a set to keep track of unlocked boxes
    unlocked_boxes = set()
    unlocked_boxes.add(0)  # The first box is initially unlocked

    # Initialize a stack with the keys from the first box
    keys = boxes[0]

    # Use a stack to perform a depth-first search (DFS)
    while keys:
        key = keys.pop()
        if key not in unlocked_boxes and key < len(boxes):
            unlocked_boxes.add(key)
            keys.extend(boxes[key])  # Add keys from the newly unlocked box

    # Check if all boxes have been unlocked
    return len(unlocked_boxes) == len(boxes)


# Example usage
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False

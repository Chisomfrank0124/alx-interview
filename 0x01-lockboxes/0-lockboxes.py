#!/usr/bin/python3

def canUnlockAll(boxes):
    def explore_box(box_index):
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited:
                explore_box(key)

    n = len(boxes)
    visited = set()
    explore_box(0)

    return len(visited) == n

# Example usage:
if __name__ == "__main__":
    boxes = [[1], [2], [3], []]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 2], [3], [], []]
    print(canUnlockAll(boxes))  # Output: False

"""
Sort the integers in a list. But the position of zeros should not be changed.

Input: A list of integers.

Output: A list or another Iterable (tuple, generator, iterator) of integers.
"""
from typing import Iterable


def except_zero(items: list) -> Iterable:
    # your code here
    list_items = []
    for item in sorted(items):
        if item != 0:
            list_items.append(item)
    for index,item in enumerate(items):
        if item == 0:
            list_items.insert(index, item)
    return list_items


print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

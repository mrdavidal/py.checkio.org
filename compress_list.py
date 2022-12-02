"""
A given list should be "compressed" in a way so, instead of two (or more) equal elements,
staying one after another, there should be only one in the result Iterable
(list, tuple, iterator, generator).

Input: A list.

Output: "Compressed" List or another Iterable (tuple, iterator, generator).
"""
from typing import Iterable


def compress(items: list[int]) -> Iterable[int]:
    # your code here
    new_list = []
    i = 0
    to_check = 0
    to_delete = 0
    while i < len(items):
        new_list.append(items[i])
        to_check = items[i]
        while to_check == items[i] and i + 1 < len(items):
            i += 1
        if items[i - 1] == to_check and items[i] != to_check:
            i -= 1
        i += 1
    return new_list


print("Example:")
print(list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])))

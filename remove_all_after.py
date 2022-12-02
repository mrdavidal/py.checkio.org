"""
Not all of the elements are important. What you need to do here is to remove all of the elements after the given one from list.

example

For illustration, we have a list [1, 2, 3, 4, 5] and we need to remove all the elements that go after 3 - which is 4 and 5.

We have two edge cases here:

if a cutting element cannot be found, then the list shouldn't be changed;
if the list is empty, then it should remains empty.
Input: List of integers and the border element integer.

Output: List or other Iterable (tuple, iterator, generator ...) of integers.
"""
from typing import Iterable


def remove_all_after(items: list[int], border: int) -> Iterable[int]:
    # your code here
    if border not in items:
        return items
    new_list = []
    check = 0
    for item in items:
        new_list.append(item)
        if item == border:
            break
    return new_list

print("Example:")
print(list(remove_all_after([7, 2, 3, 4, 5], 7)))

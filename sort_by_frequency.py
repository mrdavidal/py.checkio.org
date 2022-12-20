"""
Sort the given list so that its elements end up in the decreasing frequency order,
that is, the number of times they appear in elements.
If two elements have the same frequency, they should end up in the same order as
the first appearance in the list.

If you want to practice more with the similar case, try Frequency Sorting mission.

Input: List

Output: List or another Iterable (tuple, iterator, generator)
"""
from typing import Iterable


def frequency_sort(items: list[str | int]) -> Iterable[str | int]:
    # your code here
    list = sorted(items, key = lambda element:items.index(element))
    ret_list = sorted(list, key = lambda element:items.count(element), reverse = True)
    return ret_list

print("Example:")
print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))
print(list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])))

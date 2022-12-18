"""
You have to split a given list into two lists inside an Iterable.
If input sequence has an odd amount of elements,
then the first list inside result Iterable should have more elements.
If input sequence has no elements, then two empty lists inside result Iterable should be returned.

Input: A list.

Output: An Iterable of two lists.
"""
from typing import Any, Iterable


def split_list(items: list[Any]) -> Iterable[list[Any]]:
    # your code here
    n = len(items) // 2
    if len(items) == 0:
        return [[],[]]
    elif len(items) == 1:
        return [items,[]]
    elif len(items) % 2 != 0:
        n += 1
        return [items[:n], items[n:len(items)]]
    else:
        return [items[:n], items[n:len(items)]]



print("Example:")
print(list(split_list([])))
print(list(split_list([1])))
print(list(split_list([1, 2, 3, 4, 5, 6,7])))
print(list(split_list([1, 2, 3, 4, 5, 6])))

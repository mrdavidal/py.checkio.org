"""
Create and return a new Iterable that contains the same elements as the argument list items,
but with the reversed order of the elements inside every maximal strictly ascending subsequence.
This function should not modify the contents of the original list.

Input: List of integers.

Output: Iterable of integers.
"""
from typing import Iterable


def reverse_ascending(items: list[int]) -> Iterable[int]:
    # your code here
    if len(items) == 0 or len(items) == 1:
        return items
    list = []
    ret_list = []
    anterior = items[0]
    i = 1
    check = 0
    while i < len(items):
        if anterior < items[i]:
            while anterior < items[i] and i + 1 != len(items):
                list.append(anterior)
                anterior = items[i]
                i += 1
            list.append(anterior)
            if i + 1 == len(items):
                list.append(items[i])
            check += 1
        else:
            ret_list.append(anterior)
            if i + 1 == len(items):
                ret_list.append(items[i])
        if check > 0:
            list.reverse()
            ret_list.extend(list)
            check = 0
            del list
            list = []
        anterior = items[i]
        i += 1
    return ret_list


print("Example:")
print(list(reverse_ascending([5, 4, 3, 2, 1])))

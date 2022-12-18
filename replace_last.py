"""
In a given list the last element should become the first one.
An empty list or list with only one element should stay the same

example

Input: List.

Output: Iterable (tuple, generator, Iterator ...).
"""
from typing import Iterable


def replace_last(line: list) -> Iterable:
    # your code here
    if len(line) == 0 or len(line) == 1:
        return line
    ret_list = []
    ret_list.append(line[-1])
    for i in range(0,len(line) - 1):
        ret_list.append(line[i])
    return ret_list


print("Example:")
print(list(replace_last([])))
print(list(replace_last([1])))
print(list(replace_last([2, 3, 4, 1])))

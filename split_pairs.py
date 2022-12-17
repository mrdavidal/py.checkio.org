"""
Split the string into pairs of two characters.
If the string contains an odd number of characters,
then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: A list or another Iterable of strings.
"""
from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    # your code here
    if len(text) == 0:
        return []
    n = 2
    list = []
    for i in range(0, len(text), n):
        list.append(text[i:i + n])
    if len(list[-1]) == 1:
        list[-1] +="_"
    return list

print("Example:")
print(list(split_pairs("a")))

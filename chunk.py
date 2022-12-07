"""
You have a lot of work to do, so you might want to split it into smaller pieces.
This way you'll know which piece you'll do on Monday, which will be for Tuesday and so on.

Split a list into smaller lists of the same size (chunks).
The last chunk can be smaller than the default chunk-size. If the list is empty,
then you shouldn't have any chunks at all.


Input: Two arguments. A List and chunk size.

Output: An Iterable with chunked Iterable.
"""
from typing import Iterable


def chunking_by(items: list, size: int) -> Iterable:
    # your code here
    list = []
    for i in range(0, len(items), size):
        #easy solution
        #yield items[i : i + size]
        #same result withouth the use of yield
        list.append(items[i: i + size])
    return list


print("Example:")
print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

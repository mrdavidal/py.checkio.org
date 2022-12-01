#In a given list the first element should become the last one.
#An empty list or list with only one element should stay the same.
from typing import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    if len(items) == 1:
        return items
    elif len(items) == 0:
        return items
    it = items[0]
    del items[0]
    items.insert(len(items), it)
    return items


print("Example:")
print(list(replace_first([1, 2, 3, 4])))

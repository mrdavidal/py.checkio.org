#In this mission you should check if all elements in the given list are equal.
from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    if len(elements) == 1 or len(elements) == 0:
        return True
    check = 0
    first_elem = elements[0]
    for elem in elements:
        if elem == first_elem:
            check += 1
    if check == len(elements):
        return True
    else:
        return False


print("Example:")
print(all_the_same([1, 1, 1]))

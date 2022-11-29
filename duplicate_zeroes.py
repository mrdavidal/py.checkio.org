#You are given a list of integers.
#Your task in this mission is to duplicate (..., 🍩, ... --> ..., 🍩, 🍩, ...)
#all zeros (think about donuts ;-P) and return the result as any Iterable.
from typing import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    # your code here
    final_list = []
    for i in range(len(donuts)):
        if donuts[i] > 0:
            final_list.append(donuts[i])
        elif donuts[i] == 0:
            final_list.append(donuts[i])
            final_list.append(0)
    return final_list


print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))

"""
Sort the given list so that its elements end up in the decreasing frequency order,
 that is, the number of times they appear in elements.
 If two elements have the same frequency, they should end up according to their natural order.
 For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5].

If you want to practice more with the similar case, try Sort Array by Element Frequency mission.

Input: List of integers.

Output: List or another Iterable (tuple, iterator, generator).
"""
from typing import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    # replace this for solution
    my_tuple = ()
    list = []
    numbers = sorted(numbers)
    i = 0
    check = 0
    while i < len(numbers):
        if i + 1 < len(numbers) and numbers[i] == numbers[i + 1]:
            my_tuple = numbers.count(numbers[i]), numbers[i]
            list.append(my_tuple)
            while i + 1 < len(numbers) and numbers[i] == numbers[i + 1]:
                i += 1
        else:
            my_tuple = numbers.count(numbers[i]), numbers[i]
            list.append(my_tuple)
        i += 1
    new_list = []
    for j in range(len(list)):
        new_list.append(list[j][0])
    ret_list = []
    x = 0
    while len(new_list) > 0:
        ret_list.append(max(new_list))
        while x < len(new_list):
            if new_list[x] == max(new_list):
                del new_list[x]
                break
            x += 1
        x = 0
    last_list = []
    m = 0
    ct =0
    i = 0
    for elem in ret_list:
        while m < len(list):
            if elem == list[m][0] and list[m][0] == 1:
                last_list.append(list[m][1])
                del list[m]
                m = -1
                break
            elif elem == list[m][0] and list[m][0] > 1:
                while i < list[m][0]:
                    last_list.append(list[m][1])
                    i += 1
                del list[m]
                m = -1
            i = 0
            m += 1
        m = 0
    return last_list


print("Example:")
print(list(frequency_sorting([3, 4, 11, 13, 3, 4,11,11, 13])))

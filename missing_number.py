"""
You are given a list of integers, which are elements of arithmetic progression -
the difference between the consecutive elements is constant.
But this list is unsorted and one element is missing...good luck!

Input: List of integers.

Output: Integer.
"""
def missing_number(items: list[int]) -> int:
    # your code here
    items = sorted(items)
    difference = 0
    list_difference = []
    for i in range(len(items)):
        if i + 1 < len(items):
            difference = items[i + 1] - items[i]
            list_difference.append(difference)
    for j in range(len(items)):
        if j + 1 < len(items):
            if items[j + 1] - items[j] == max(list_difference):
                return items[j + 1] - min(list_difference)
print("Example:")
print(missing_number([1,2,4,5]))
print(missing_number([2,6,8]))
print(missing_number([3,9,12]))
print(missing_number([4,8,16]))
print(missing_number([5,15,20]))

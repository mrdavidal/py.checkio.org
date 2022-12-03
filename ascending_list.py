"""
Determine whether the list of elements is ascending such that each of its elements is
strictly larger than (and not merely equal to) the preceding element.
Empty list consider as ascending.

Input: A list with integers.

Output: Boolean.
"""
def is_ascending(items: list[int]) -> bool:
    # your code here
    if len(items) == 0 or len(items) == 1:
        return True
    check = 0
    for i in range(len(items)):
        if i + 1 < len(items):
            if items[i + 1] > items[i]:
                check += 1
    if check + 1 == len(items):
        return True
    else: return False

print("Example:")
print(is_ascending([-5, 10, 99, 123456, 23333333333]))

"""
Let's try some sorting. Here is an array with the specific rules.

The array (a list) has various numbers. You should sort it, but sort it by absolute value in ascending order. For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20). Your function should return the sorted list or tuple.

Precondition: The numbers in the array are unique by their absolute values.

Input: An array of numbers , a tuple..

Output: The list or tuple (but not a generator) sorted by absolute values in ascending order.
"""
def checkio(values: list) -> list:
    # your code here
    new_list = []
    ret_list = []
    min_index = 0
    minim = 0
    minimum = 0
    v =0
    for val in values:
        if val < 0:
            minim = val * -1
        else:
            minim = val
        new_list.append(minim)
    while len(new_list) > 0:
        minimum = min(new_list)
        ret_list.append(minimum)
        min_index = new_list.index(minimum)
        del new_list[min_index]
    for val in ret_list:
        v = val * -1
        if v in values:
            ret_list[ret_list.index(val)] = v
    return ret_list


print("Example:")
print(checkio([-20, -5, 10, 15]))

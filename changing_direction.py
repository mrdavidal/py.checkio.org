"""
You are given a list of integers. Your task in this mission is to find, how many times the sorting direction was changed in the given list. If the elements are equal - the previous sorting direction remains the same, if the sequence starts from the same elements - look for the next different to determine the sorting direction.

Let's look at the scheme:

changing_dir

There are three sorting directions:

on the chunk 1, 2, 2 - up (increasing);
on the chunk 2, 1 - down (decreasing);
and on the chunk 1, 2, 2 - up again.
So, you have two points of changing the sorting direction: #1 - from up to down, and #2 - from down to up. That's the result your function should return.
Input: A list of integers.

Output: Integer.
"""
def changing_direction(elements: list) -> int:
    new_list = []
    anterior = elements[0]
    res = 0
    if len(elements) == 1:
        return elements[0]
    for i in range(len(elements)):
        if elements[i] - anterior != 0:
            new_list.append(elements[i] - anterior)
        anterior = elements[i]
    ante = new_list[0]
    for j in range(len(new_list)):
        if (ante < 0 and new_list[j] > 0) or (ante > 0 and new_list[j] < 0):
            res += 1
        ante = new_list[j]
    return res

print("Example:")
#print(changing_direction([1, 2, 3, 4, 5]))
#print(changing_direction([1, 2, 3, 2, 1]))
#print(changing_direction([1, 2, 2, 1, 2, 2]))
print(changing_direction([1, 2, 2, 1, 2, 1, 2]))

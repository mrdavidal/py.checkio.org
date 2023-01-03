"""
You have a list. Each value from that list can be either a string or an integer.
Your task here is to return two values.
The first one is a concatenation of all strings from the given list.
 The second one is a sum of all integers from the given list.

Input: A list of strings and integers.

Output: A list or tuple.
"""
def sum_by_types(items: list[str, int]) -> tuple[str, int] | list[str, int]:
    # your code here
    s = ""
    i = 0
    for item in items:
        if type(item) == int:
            i += item
        elif type(item) == str:
            s += item
    return [s, i]


print("Example:")
print(list(sum_by_types([])))

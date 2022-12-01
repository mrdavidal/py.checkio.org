"""
We have a list of booleans. Let's check if the majority of elements are True.

Some cases worth mentioning: 1) an empty list should return False;
2) if True-s and False-s have an equal amount, function should return False.

Input: A list of booleans.

Output: A Boolean.
"""
def is_majority(items: list[bool]) -> bool:
    # your code here
    if len(items) == 0:
        return False
    check_trues = 0
    check_falses = 0
    for item in items:
        if item == True:
            check_trues += 1
        elif item == False:
            check_falses += 1
    if check_trues == check_falses:
        return False
    elif check_trues > check_falses:
        return True
    else: return False


print("Example:")
print(is_majority([True, False, True, False]))

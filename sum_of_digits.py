"""
The task in this mission is as follows:

You are given an integer. If it consists of one digit, simply return its value.
If it consists of two or more digits - add them until the number contains only one digit and return it.

Input: A int.

Output: A int.
"""
def sum_digits(num: int) -> int:
    # your code here
    number = str(num)
    while len(number) > 1:
        sum_digits = 0
        for ch in number:
            sum_digits += int(ch)
        number = str(sum_digits)
    return int(number)


print("Example:")
print(sum_digits(38))

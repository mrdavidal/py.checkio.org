"""
You need to count the number of digits in a given string.

Input: String.

Output: Integer.
"""
def count_digits(text: str) -> int:
    # your code here
    conter = 0
    for ch in text:
        if ord(ch) > 47 and ord(ch) < 58:
            conter += 1
    return conter


print("Example:")
print(count_digits("hi"))

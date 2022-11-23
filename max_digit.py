#You have a number and you need to determine which digit in this number is the biggest.
def max_digit(value: int) -> int:
    # your code here
    return int(max(str(value)))


print("Example:")
print(max_digit(0))

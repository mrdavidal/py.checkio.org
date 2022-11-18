#You have a string that consist only of digits.
#You need to find how many zero digits ("0") are at the beginning of the given string.
def beginning_zeros(a: str) -> int:
    # your code here
    i = 0
    zeroes = []
    while i < len(a):
        if a[i] == "0":
            zeroes.append(a[i])
        else: break
        i += 1
    return len(zeroes)


print("Example:")
print(beginning_zeros("10"))
print(beginning_zeros("010"))
print(beginning_zeros("0010"))
print(beginning_zeros("00010"))

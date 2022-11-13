#Try to find out how many zeros a given number has at the end.
def end_zeros(a: int) -> int:
    # your code here
    number = reversed(str(a))
    counter = 0
    for i in number:
        if i == "0":
            counter += 1
        else: break
    return counter


print("Example:")
print(end_zeros(10))

assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")

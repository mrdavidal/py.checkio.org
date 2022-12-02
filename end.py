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
print(end_zeros(1000000))

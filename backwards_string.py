#You should return a given string in reverse order.
def backward_string(val: str) -> str:
    # your code here
    list = []
    string = ""
    for i in val:
        list.insert(0,i)
    for i in list:
        string += i
    return string


print("Example:")
print(backward_string("val"))

assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"

print("The mission is done! Click 'Check Solution' to earn rewards!")

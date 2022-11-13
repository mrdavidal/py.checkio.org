"""
In this mission, you need to create a password verification function.
The verification condition is:
the length should be bigger than 6.
"""
def is_acceptable_password(password: str) -> bool:
    # your code here
    counter = 0
    for i in range(0,len(password)):
        counter += 1
    if counter <= 6:
        return False
    return True


print("Example:")
print(is_acceptable_password("short"))

assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

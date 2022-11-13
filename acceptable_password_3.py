"""
The verification conditions are:

the length should be bigger than 6;
should contain at least one digit, but cannot consist of just digits.
"""
# Taken from mission Acceptable Password II

# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    # your code her
    if password.isdigit():
        return False
    counter = 0
    check = 0
    for i, v in enumerate(password):
        counter += 1
        if v.isdigit():
            check += 1
    if counter <= 6:
        return False
    if check > 0:
        return True
    return False



assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

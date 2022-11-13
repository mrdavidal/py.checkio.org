"""
The verification conditions are:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
if the password is longer than 9 - previous rule (about one digit), is not required.
"""
# Taken from mission Acceptable Password III

# Taken from mission Acceptable Password II

# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    # your code her
    counter = 0
    check = 0
    for i, v in enumerate(password):
        counter += 1
        if v.isdigit():
            check += 1
    if counter <= 6:
        return False
    if check == len(password) and counter > 9:
        return True
    if counter > 9:
        return True
    if check > 0 and check < len(password) and counter < 9:
        return True
    return False





assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("notshort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")

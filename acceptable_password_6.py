"""
The verification conditions are:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
a string should not contain the word "password" in any case;
should contain at least 3 different letters (or digits) even if it is longer than 10
"""
# Taken from mission Acceptable Password V

# Taken from mission Acceptable Password IV

# Taken from mission Acceptable Password III

# Taken from mission Acceptable Password II

# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    #we define the variables needed:
    counter = 0 #to check the lenght
    check = 0 # to check if there are digits in string
    check_ch = "" #to check if characters are unique
    cnt = 0
    #iterate and enumerate the string
    for i, v in enumerate(password):
        counter += 1# will be equal to lenght of password
        if v.isdigit():#check if ch is digit
            check += 1#will be equal to total numbers of digits
    for i in password:
        if i not in check_ch:
            check_ch = check_ch + i
            cnt += 1
    #if the password word is found it will return false
    if password.find("password") > -1 or password.find("PASSWORD") > -1 :
        return False
    if counter <= 6:
        return False
    if check > 0 and check < len(password) and (counter < 9 or counter >= 9)and cnt < 3:
        return False
    if check == len(password) and counter >= 9 and cnt >=3:
        return True
    if counter >= 9 and cnt >= 3:
        return True

    if check > 0 and check < len(password) and counter <= 9 and cnt >=3:
        return True
    return False









assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False
assert is_acceptable_password("pass1234word") == True
assert is_acceptable_password("aaaaaa1") == False
assert is_acceptable_password("aaaaaabbbbb") == False
assert is_acceptable_password("aaaaaabb1") == True
assert is_acceptable_password("abc1") == False
assert is_acceptable_password("abbcc12") == True
assert is_acceptable_password("aaaaaaabbaaaaaaaab") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

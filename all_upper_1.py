#Check if a given string has all symbols in upper case.
#If the string is empty or doesn't have any letter in it - function should return True.
def is_all_upper(text: str) -> bool:
    # your code here
    i = 0
    check_up = 0
    check_spaces = 0
    check_nr = 0
    check_spaces = 0
    if len(text) == 0:
        return True
    while i < len(text):
        if ord(text[i]) > 64 and ord(text[i]) < 91:
            check_up += 1
        elif ord(text[i]) > 47 and ord(text[i]) < 58:
            check_nr += 1
        elif ord(text[i]) == 32:
            check_spaces += 1
        i += 1
    if check_nr + check_spaces == len(text):
        return True
    elif check_up + check_spaces == len(text):
        return True
    elif check_nr + check_up + check_spaces == len(text):
        return True
    return False


print("Example:")
print(is_all_upper("ALL UPPER"))

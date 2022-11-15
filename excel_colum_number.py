#Given a string that represents the column title as appears in an Excel sheet,
#return its corresponding column number
def column_number(name: str) -> int:
    # your code here
    result = 0
    while name:
        result += (26 ** (len(name) - 1)) * (ord(name[0]) - 64)
        name = name[1:]
    return result

print("Example:")
print(column_number("AA"))

print("Example:")
print(column_number("ZY"))

#Given a string that represents the column title as appears in an Excel sheet,
#return its corresponding column number
def column_number(name: str) -> int:
    # your code here
    dictionary = {"A": 1,
                  "B": 2,
                  "C": 3,
                  "D": 4,
                  "E": 5,
                  "F": 6,
                  "G": 7,
                  "H": 8,
                  "I": 9,
                  "J": 10,
                  "K": 11,
                  "L": 12,
                  "M": 13,
                  "N": 14,
                  "O": 15,
                  "P": 16,
                  "Q": 17,
                  "R": 18,
                  "S": 19,
                  "T": 20,
                  "U": 21,
                  "V": 22,
                  "W": 23,
                  "X": 24,
                  "Y": 25,
                  "Z": 26
                  }
    col_number = 0
    second_col = 0
    list_positions = []
    check = 0
    product = 0
    for i in range(len(name)):
        for key in dictionary.keys():
            if key == name[i]:
                list_positions.append(dictionary[key])
    if len(list_positions) == 1:
        check = 1
    elif len(list_positions) > 1:
        check = 2
    if check == 2:
        for j in range(len(list_positions)):
            if j == 0:
                col_number = (list_positions[j] * 26)
            elif j == 1:
                second_col = 26 - (26 - list_positions[j])
            product = col_number + second_col
    else:
        return list_positions[0]
    return product


print("Example:")
print(column_number("ZY"))

#Your mission is to convert the name of a function (a string) from the Python format
#(for example "my_function_name") into CamelCase ("MyFunctionName"),
#where the first char of every word is in uppercase and all words are concatenated
#without any intervening characters.
def to_camel_case(name: str) -> str:
    # replace this for solution
    list_name = name.split("_")
    first_letter = ""
    string = ""
    for i in range(len(list_name)):
        for j in range(len(list_name[i])):
            if j == 0:
                first_letter = list_name[i][0]
                first_letter = first_letter.upper()
                string += first_letter
            else:
                string += list_name[i][j]


    return string


print("Example:")
print(to_camel_case("my_function_name"))

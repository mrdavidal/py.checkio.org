#Your mission is to convert the name of a function (a string) from the Python format
#(for example "my_function_name") into CamelCase ("MyFunctionName"),
#where the first char of every word is in uppercase and all words are concatenated
#without any intervening characters.
def to_camel_case(name: str) -> str:
    # replace this for solution
    list_name = name.split("_")
    string = ""
    for i in range(len(list_name)):
        for j in range(len(list_name[i])):
            list_name[i][0] = list_name[i][0].upper()
    return list_name


print("Example:")
print(to_camel_case("my_function_name"))

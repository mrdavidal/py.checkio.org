#Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName")
#into the Python format ("my_function_name") where all chars are in lowercase and all words are concatenated
#with an intervening underscore symbol "_".
import re
def from_camel_case(name: str) -> str:
    # replace this for solution
    function_name = re.findall("[a-zA-Z][^A-Z]*", name)
    string = ""
    for i in range(len(function_name)):
        string += function_name[i]
        if i + 1 != len(function_name):
            string += "_"
    return string.lower()


print("Example:")
print(from_camel_case("MyFunctionName"))

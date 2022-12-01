"""
In a given string you should reverse every word, but the words should stay in their places.

Input: A string.

Output: A string.
"""
def rev_string(string):
    ret_string = ""
    for i in range(len(string) - 1, -1, -1):
        ret_string += string[i]
    return ret_string

def backward_string_by_word(text: str) -> str:
    # your code here
    if len(text) == 0:
        return text
    string = ""
    list_string = text.split(" ")
    for i in range(len(list_string)):
        if list_string[i] == "":
            string += " "
        else:
            string += rev_string(list_string[i])
            if i < len(list_string) - 1:
                string += " "
    return string


print("Example:")
print(backward_string_by_word("hello"))

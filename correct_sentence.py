#For the input of your function, you will be given one sentence.
#You have to return a corrected version, that starts with a capital letter and ends with a period (dot).
#Pay attention to the fact that not all of the fixes are necessary.
#If a sentence already ends with a period (dot), then adding another one will be a mistake.
#Input: A string.
#Output: A string.
def correct_sentence(text: str) -> str:
    """
    returns a corrected sentence which starts with a capital letter
    and ends with a dot.
    """
    string = ""
    for i in range(len(text)):
        if ord(text[i]) > 96 and ord(text[i]) < 123 and i == 0:
            string += text[0].upper()
        else:
            string += text[i]
    if string[-1] == ".":
        pass
    else:
        string += "."
    return string


print("Example:")
print(correct_sentence("greetings, friends"))

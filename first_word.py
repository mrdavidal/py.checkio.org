#You are given a string where you have to find its first word.
#When solving a task pay attention to the following points:

#There can be dots and commas in a string.
#A string can start with a letter or, for example, one/multiple dot(s) or space(s).
#A word can contain an apostrophe and it's a part of a word.
#The whole text can be represented with one word and that's it.
#Input: A string.
#Output: A string.
def first_word(text: str) -> str:
    """
    function returns the first word in a given text.
    """
    # your code here
    list_text = text.split(" ")
    string = ""
    ret_string = ""
    for j in range(len(list_text)):
        if list_text[j] == "":
            continue
        for i in range(len(list_text[j])):
            if (ord(list_text[j][i]) > 31 and ord(list_text[j][i]) < 65) or \
            (ord(list_text[j][i]) > 90 and ord(list_text[j][i]) < 97) or \
            (ord(list_text[j][i]) > 122 and ord(list_text[j][i]) < 127):
                try:
                    if ord(list_text[j][i]) == 39 and (ord(list_text[j][i - 1]) > 64 and ord(list_text[j][i - 1]) < 91 or \
                    ord(list_text[j][i - 1]) > 96 and ord(list_text[j][i - 1]) < 123) \
                    and (ord(list_text[j][i + 1]) > 64 and ord(list_text[j][i + 1]) < 91 or \
                    ord(list_text[j][i + 1]) > 96 and ord(list_text[j][i + 1]) < 123):
                        string += list_text[j][i]
                    else:
                        string += " "
                except:
                    string += " "
            else:
                string += list_text[j][i]
        string += " "
    list_string = string.split(" ")
    x = 0
    while x < len(list_string):
        if list_string[x] == "":
            del list_string[x]
            x = -1
        x += 1
    for i in range(len(list_string[:1])):
        ret_string += list_string[i]
    return ret_string

print("Example:")
print(first_word("... and so on ..."))

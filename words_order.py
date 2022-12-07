"""
You have a text and a list of words. You need to check if the words in a list
appear in the same order as in the given text.

Cases you should expect while solving this challenge:

a word from the list is not in the text - your function should return False;
any word can appear more than once in a text - use only the first one;
two words in the given list are the same - your function should return False;
the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
the text includes only English letters and spaces.
Input: Two arguments. The first one is a given text, the second is a list of words.

Output: A bool.
"""
def words_order(text: str, words: list) -> bool:
    # your code here
    text_list = text.split()
    check_list = []
    check = 0
    conter = 1
    for word in words:
        for index, txt in enumerate(text_list):
            if word == txt:
                check_list.append(index)
                break
    try:
        anterior = check_list[0]
    except: pass
    if len(check_list) == len(words):
        for i in range(1, len(check_list)):
            if check_list[i] > anterior:
                conter += 1
            anterior = check_list[i]
    else: return False
    if conter == len(check_list):
        return True
    else: return False

print("Example:")
print(words_order("here world world hi im here", ["here", "world"]))

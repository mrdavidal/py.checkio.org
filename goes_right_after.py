#In a given word you need to check if one symbol goes only right after another.

#Cases you should expect while solving this challenge:

#one of the symbols is not in the given word - your function should return False;
#any symbol appears in a word more than once - use only the first one;
#two symbols are the same - your function should return False;
#the condition is case sensitive, which means 'a' and 'A' are two different symbols.
#: Three arguments. The first one is a given string, second is a symbol that should go first,
#and the third is a symbol that should go after the first one.

#Output: A bool.
def goes_after(word: str, first: str, second: str) -> bool:
    # your code here
    check = 0
    if first == second:
        return False
    for i in range(len(word)):
        try:
            if word[i] == first or word[i] == second:
                check += 1
            if word[i] == first and word[i + 1] == second and check == 1:
                return True
        except:
            return False
    return False


print("Example:")
print(goes_after("worldror", "o", "r"))

#You are given a string with words and numbers separated by whitespaces (one space).
#The words contains only letters. You should check if the string contains three words in succession .
#For example, the string "start 5 one two three 7 end" contains three words in succession.

#Input: A string with words.

#Output: The answer as a boolean.
def checkio(words: str) -> bool:
    # add your code here
    list_words = words.split(" ")
    conter = 0
    for ch in list_words:
        try :
            int(ch)
            conter = 0
        except:
            conter += 1
        if conter == 3:
            return True
    return False

print("Example:")
print(checkio("Hello 7 World hello hi 8"))

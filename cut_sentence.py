#Your task in this mission is to truncate a sentence
#to a length that does not exceed a given number of characters.
#If the given sentence already is short enough,
#you don't have to do anything to it.
#But if it needs to be truncated, the omission must be indicated
#by concatenating an ellipsis ("...") to the end of the shortened sentence.

#The shortened sentence can contain complete words and spaces.
#It must neither contain truncated words nor trailing spaces.
#The ellipsis has been taken into account for the allowed number of characters,
#so it does not count against the given length.

#Input: Two arguments:
#one-line sentence as a string;
#max length of the truncated sentence as an int.

#Output: The shortened sentence plus the ellipsis (if required) as a one-line string.

def cut_sentence(line: str, length: int) -> str:
    """
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    """
    # your code here
    i = 0
    x = 0
    check = 0
    for ch in line[:length]:
        if ch == " ":
            check += 1
    if len(line) <= length:
        return line[:]
    elif len(line) > length and line[length] == " ":
        return line[:length] + "..."
    elif check > 0:
        for ch in line[:length]:
            x += 1
            if ch == " ":
                i = x
        return line[:i - 1] + "..."
    else:
        return "..."

print("Example:")
print(cut_sentence("Hi my name is Alex", 4))

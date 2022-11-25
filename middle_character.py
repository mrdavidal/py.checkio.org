#You are given some string where you need to find its middle character(s).
#The string may contain one word, a few symbols or a whole sentence.
#If the length of the string is even, then you should return two middle characters,
#but if the length is odd, return just one. For more details look at the Example.
def middle(text: str) -> str:
    # replace this for solution
    holder = 0
    if len(text) % 2 == 0:
        holder = len(text) // 2
        return text[holder - 1] + text[holder]
    else:
        holder = (len(text) - 1) // 2
        return text[holder]


print("Example:")
print(middle("test"))

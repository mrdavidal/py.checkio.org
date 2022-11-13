#You are given a string and you have to find its first word.
def first_word(text: str) -> str:
    # your code here
    string = ""
    for i in text:
        if i == " ":
            return string
        string += i
    return string


print("Example:")
print(first_word("Hello world"))

assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")

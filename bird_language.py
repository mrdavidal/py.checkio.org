"""
The bird converts words by two rules:
- after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
Vowels letters == "aeiouy".

You are given an ornithological phrase as several words which are separated by white-spaces
(each pair of words by one whitespace).
The bird does not know how to punctuate its phrases and only speaks words as letters.
All words are given in lowercase.
You should translate this phrase from the bird language to something more understandable.
"""
def translate(text: str) -> str:
    # your code here
    text_list = text.split()
    string = ""
    i = 0
    for word in text_list:
        while i <= len(word) -1:
            if word[i] == "a" or\
            word[i] == "e" or\
            word[i] == "i" or\
            word[i] == "o" or\
            word[i] == "y" or\
            word[i] == "u":
                string += word[i]
                i += 3
            elif word[i] == "b" or\
            word[i] == "c" or\
            word[i] == "d" or\
            word[i] == "f" or\
            word[i] == "g" or\
            word[i] == "h" or\
            word[i] == "j" or\
            word[i] == "k" or\
            word[i] == "l" or\
            word[i] == "m" or\
            word[i] == "n" or\
            word[i] == "p" or\
            word[i] == "q" or\
            word[i] == "r" or\
            word[i] == "s" or\
            word[i] == "t" or\
            word[i] == "v" or\
            word[i] == "w" or\
            word[i] == "x" or\
            word[i] == "z":
                string += word[i]
                i += 2
        i = 0
        if word != text_list[-1]:
            string += " "
    return string


print("Example:")
print(translate("hieeelalaooo"))
print(translate("hoooowe yyyooouuu duoooiiine"))

assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")

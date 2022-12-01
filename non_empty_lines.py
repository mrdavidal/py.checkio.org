"""
You need to count how many non-empty lines a given text has.

An empty line is a line without symbols or the one that contains only spaces.

Input: A text.

Output: An int.
"""
def non_empty_lines(text: str) -> int:
    # your code here
    ch_count = 0
    lines = 0
    for ch in text:
        if ord(ch) != 32 and ch != "\n":
            ch_count +=1
        if ch == "\n" and ch_count > 0:
            lines += 1
            ch_count = 0
    return lines


print("Example:")
print(non_empty_lines(
        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
    ))

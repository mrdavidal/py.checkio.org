"""
You are given a string and two markers (the initial one and final).
You have to find a substring enclosed between these two markers.
But there are a few important conditions.

This is a simplified version of the Between Markers mission.

The initial and final markers are always different.
The initial and final markers are always 1 char size.
The initial and final markers always exist in a string and go one after another.
"""
def between_markers(text: str, start: str, end: str) -> str:
    # your code here
    string = ""
    i = 0
    for ch in text:
        if ch == start:
            i += 1
            continue
        if ch == end:
            i += 1
        if i == 1:
            string += ch
        elif i == 2:
            i = 0

    return string


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

print("The mission is done! Click 'Check Solution' to earn rewards!")

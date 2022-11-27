#Your mission here is to create a function that gets a tuple and returns a tuple with only 3 elements
#- the first, third and second element from the last for the given tuple.
def easy_unpack(elements: tuple) -> tuple:
    # your code here
    return elements[0], elements[2], elements[-2]

print("Example:")
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

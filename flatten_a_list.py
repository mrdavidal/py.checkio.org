"""
Nicola likes to categorize all sorts of things.
He categorized a series of numbers and as the result of his efforts,
a simple sequence of numbers became a deeply-nested list.
Sophia and Stephan don't really understand his organization and
need to figure out what it all means.
They need your help to understand Nikolas crazy list.

There is a list which contains integers or other nested lists which may contain
yet more lists and integers which then… you get the idea.
You should put all of the integer values into one flat list.
The order should be as it was in the original list with string representation from left to right.

We need to hide this program from Nikola by keeping it small and easy to hide.
Because of this, your code should be shorter than 140 characters (with whitespaces) .

Input data: A nested list with integers.

Output data: The one-dimensional list with integers.
"""
def flat_list(array):
    l = []
    for elem in array:
        if type(elem) != list: l.append(elem)
        else: l.extend(flat_list(elem))
    return l

print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))

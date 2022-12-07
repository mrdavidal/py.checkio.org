"""
Your function should create a list of lists, that represents a two-dimensional grid with the given number of rows and cols.

This grid should contain the integers from start to start + rows * cols - 1 in ascending order, but the elements of every odd-index row have to be listed in descending order, so that when read in ascending order, the numbers zigzag through the two-dimensional grid.

Input: Two integers - rows and columns. One optional integer - start.

Output: List of lists.
"""
def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
    # your code here
    conter = start
    list = [[j for j in range(0, cols)] for i in range(0, rows)]
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j] = conter
            conter += 1
    for i in range(len(list)):
        if i > 0 and i % 2 != 0:
            list[i].reverse()
    return list


print("Example:")
print(create_zigzag(3, 3, 5))

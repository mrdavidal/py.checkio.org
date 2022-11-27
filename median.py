"""
A median is a numerical value separating the upper half of a sorted list of numbers
from the lower half. In a list where there are an odd number of entities,
the median is the number found in the middle of the list.
If the list contains an even number of entities, then there is no single middle value,
 instead the median becomes the average of the two numbers found in the middle.
 For this mission, you are given a non-empty list of natural integers.
 With it, you must separate the upper half of the numbers from the lower half and find the median.
 """
def checkio(data: list[int]) -> int | float:
    # replace this for solution
    data = sorted(data)
    median = 0
    if len(data) % 2 == 0:
        median = (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2
    else:
        median = data[(len(data) - 1) // 2]
    return median

print("Example:")
print(checkio([1, 3, 2, 4, 5, 6]))

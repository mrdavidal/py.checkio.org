#You are given an array of integers.
#You should find the sum of the integers with even indexes (0th, 2nd, 4th...).
#Then multiply this summed number and the final element of the array together.
#Don't forget that the first element has an index of 0.
#For an empty array, the result will always be 0 (zero).
#Input: A list of integers.
#Output: The number as an integer.
def checkio(array: list[int]) -> int:
    # your code here
    if len(array) == 0:
        return 0
    even_list = array[::2]
    sum = 0
    for nr in even_list:
        sum += nr
    return sum * array[-1]


print("Example:")
print(checkio([]))

#You are given a positive integer.
#Your function should calculate the product of the digits excluding any zeroes.
#For example: The number given is 123405.
#The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
def checkio(number: int) -> int:
    # your code here
    nr = str(number)
    sum = 0
    list_numbers = []
    for i in range(len(nr)):
        if nr[i] != "0":
            list_numbers.append(nr[i])
    for j in range(len(list_numbers)):
        if j == 0:
            sum = int(list_numbers[j])
        elif j > 0 and j < len(list_numbers):
            sum *= int(list_numbers[j])

    return sum


print("Example:")
print(checkio(123405))

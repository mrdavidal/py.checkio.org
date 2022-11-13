"""
Stephen's speech module is broken.
This module is responsible for his number pronunciation.
He has to click to input all of the numerical digits in a figure,
so when there are big numbers it can take him a long time.
Help the robot to speak properly and increase his number processing speed
by writing a new speech module for him.
All the words in the string must be separated by exactly one space character.
Be careful with spaces - it's hard to see if you place two spaces instead one.
Precondition: 0 < number < 1000
"""
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):

    #replace this for solution
    string = str(number)
    list_number = []
    write = ""
    for i in range(len(string)):
        list_number.append(string[i])
    if len(list_number) == 1:
        return FIRST_TEN[int(list_number[0]) - 1]
    elif len(list_number) == 2:
        if number  < 20:
            return SECOND_TEN[number - 10]
        elif number >= 20 and number % 10 == 0:
            return OTHER_TENS[int(list_number[0]) - 2]
        else: return OTHER_TENS[int(list_number[0]) - 2] + " " + FIRST_TEN[int(list_number[1]) - 1]
    elif len(list_number) == 3:
        write = list_number[1] + list_number[2]
        if int(write) == 0:
            return FIRST_TEN[int(list_number[0]) - 1] + " " + HUNDRED
        elif int(write) < 10:
            return FIRST_TEN[int(list_number[0]) - 1] + " " + HUNDRED + " " + FIRST_TEN[int(list_number[2]) - 1]
        elif int(write) < 20:
            return FIRST_TEN[int(list_number[0]) - 1] + " " + HUNDRED + " " + SECOND_TEN[int(write) - 10]
        elif int(write) % 10 == 0:
            return FIRST_TEN[int(list_number[0]) - 1] + " " + HUNDRED + " " + OTHER_TENS[int(list_number[1]) - 2]
        else: return FIRST_TEN[int(list_number[0]) - 1] + " " + HUNDRED + " " + OTHER_TENS[int(list_number[1]) - 2] + " " + FIRST_TEN[int(list_number[2]) - 1]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(44) == 'forty four', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')

#You are given a text, which contains different English letters and punctuation symbols.
#You should find the most frequent letter in the text. The letter returned must be in lower case.
#While checking for the most wanted letter, casing does not matter,
#so for the purpose of your search, "A" == "a".
#Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
#If you have two or more letters with the same frequency ,
#then return the letter which comes first in the Latin alphabet.
#For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
def checkio(text: str) -> str:
    # your code here
    text = text.lower()
    my_list = []
    new_list = []
    my_tuple = ()
    list_max = []
    conter = 0
    deletion = 0
    to_delete = 0
    max = 0
    sliced = ""
    for i in range(len(text)):
        if ord(text[i]) > 31 and ord(text[i]) < 65:
            continue
        else:
            my_list.append(text[i])
    my_list = sorted(my_list)
    while conter < len(my_list):
        my_tuple += my_list[conter], my_list.count(my_list[conter])
        new_list.append(my_tuple)
        del my_tuple
        my_tuple = ()
        deletion = my_list.count(my_list[conter])
        while  to_delete < deletion:
            if to_delete + 1 == deletion:
                pass
            else:
                conter += 1
            to_delete += 1
        to_delete = 0
        conter +=1
    for tup in new_list:
        for z in range(len(tup)):
            if type(tup[z]) == int:
                list_max.append(int(tup[z]))
            else:
                continue

    for w in range(len(list_max)):
        if max < list_max[w]:
            max = list_max[w]
    for k in range(len(new_list)):
        for z in range(len(new_list[k])):
            if new_list[k][z] == max:
                return new_list[k][z - 1]

print("Example:")
print(checkio("Aaaaaaaaaaaaaaaa!!!!"))

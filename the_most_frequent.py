"""
You have a sequence of strings, and you’d like to determine the most frequently
occurring string in the sequence. It can be only one.

Input: non empty list of strings.

Output: a string.
"""
def most_frequent(data: list[str]) -> str:
    # your code here
    my_list = sorted(data)
    conter = 0
    my_tuple = ()
    new_list = []
    to_delete = 0
    list_max = []
    max = 0
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
print(most_frequent(["a", "b", "c", "a", "bi", "a", "bi", "bi",]))

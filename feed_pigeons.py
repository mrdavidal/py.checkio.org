"""
I start to feed one of the pigeons.
A minute later two more fly by and a minute after that another 3.
Then 4, and so on (Ex: 1+2+3+4+...).
One portion of food lasts a pigeon for a minute,
but in case there's not enough food for all the birds,
the pigeons who arrived first ate first.
Pigeons are hungry animals and eat without knowing when to stop.
If I have N portions of bird feed, how many pigeons will be fed with at least one portion of wheat?
"""
def checkio(food: int) -> int:
    # your code here
    pigeons = 1
    one_pigeon = 0
    pigeons_comed = 2
    feed = 0
    list_pg = []
    i = 0
    counter = 0
    while food != 0:
        while pigeons != 0:
            list_pg.append(one_pigeon)
            pigeons -= 1
        while i < len(list_pg):
            food -=1
            list_pg[i] = list_pg[i] + 1
            i += 1
            if food == 0:
                break
        pigeons = pigeons_comed
        pigeons_comed += 1
        i = 0
    for x in range(len(list_pg)):
        if list_pg[x] != 0:
            counter += 1
        else: break
    return counter


print("Example:")
print(checkio(10))

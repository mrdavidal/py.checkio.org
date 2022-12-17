"""
The main architect of the city wants to build a new highest building.
You have to help him find the current highest building in the city.

Input: Heights of the buildings as a 2D-array. Building height is defined as a column in an array.

Output: The number of the highest building and height of it as a list of integers
(Important: in this task the building numbers starts from "1", not from "0")
"""
def highest_building(buildings):
    #replace this for solution
    collumn = 0
    height = 0
    check = 0
    i = 0
    j = 0
    list = []
    my_tuple = ()
    while i < len(buildings):
        check = i
        while j < len(buildings[i]):
            if buildings[i][j] == 1:
                height = 1
                collumn = j + 1
                if i + 1 < len(buildings):
                    while i + 1 < len(buildings):
                        if buildings[i + 1][j] == 1:
                            height += 1
                        i += 1
                my_tuple = collumn,height
                list.append(my_tuple)
            j += 1
            del my_tuple
            my_tuple = ()
            i = check
        i += 1
        j = 0
    height_list = []
    ret_list = []
    for tup in list:
        height_list.append(tup[1])
    max_height = max(height_list)
    for tup in list:
        if tup[1] == max_height:
            ret_list.append(tup[0])
            ret_list.append(tup[1])
            break
    return ret_list
if __name__ == '__main__':
    print("Example:")
    print(highest_building([
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]))
    print(highest_building([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]))
    print(highest_building([
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1]
    ]))

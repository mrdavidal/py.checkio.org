"""
You have a list with all available products in a store. The data is represented as a list of dicts

Your mission here is to find the most expensive products in the list.
The number of products we are looking for will be given as the first argument
and the list of all products as the second argument.

Input: int and list of dicts. Each dict has the two keys "name" and "price"

Output: The same format as the second input argument.
"""
def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    """
    TOP most expensive goods
    """
    # your code here
    i = 0
    ret_list = []
    price_list = []
    max_price = 0
    ind = 0
    for dt in data:
        for key,item in dt.items():
            if type(item) == int:
                price_list.append(item)
    while i < limit:
        max_price = max(price_list)
        ind = price_list.index(max_price)
        del price_list[ind]
        for dt in data:
            for key,item in dt.items():
                if item == max_price:
                    ret_list.append(dt)
        i += 1
    return ret_list


print("Example:")
print(
    bigger_price(
        2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ],
    )
)

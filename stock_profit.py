#You are a broker with a single chance to buy stock and sell stock.
#Having an array of prices, pick the best time to buy stock and sell stock to maximize the profit.

#“short-selling” (sell first, buy later) is not allowed in this market.

#Your profit is zero when it is impossible to get profit at all. The size of pricing can't be less than 2.

#Input: Array of int. Stock prices.

#Output: Int. Maximum possible profit.
def stock_profit(stock: list) -> int:
    # your code here
    profit = 0
    minimum = stock[0]
    for st in stock:
        profit = max(profit, st - minimum)
        minimum = min(st, minimum)
    return profit


print("Example:")
#print(stock_profit([2, 3, 4, 5]))
print(stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]))

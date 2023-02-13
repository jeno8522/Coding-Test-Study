import sys

def maxProfit(prices):
    min_price = sys.maxsize
    profit = sys.minsize

    for price in prices:
        min_price = min(min_price,price)
        profit = max(profit, price-min_price)

    return profit
import sys
import time
from utils import *
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, combinations_with_replacement
from dataclasses import dataclass
import string
from functools import cache, lru_cache


INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

data = read(INPUT_FILE)

max_transactions, fee = map(int, data[0].split())
max_transactions = int(max_transactions) * 2  # buy + sell
prices = list(map(int, data[1].split()))

print(max_transactions, fee, len(prices))

# Actions per day. buy, sell, hold
# Can hold at most one stock at a time
frontier = [(0, 0, 0, True, 0, [])]

profits = []

while frontier:
    day, profit, num_transactions, can_buy, last_price, path = frontier.pop()
    if day >= len(prices) or num_transactions >= max_transactions:
        profits.append(profit)
        # pri#nt(
        #    f"End day {day} profit {profit} transactions {num_transactions} path {', '.join(path)}"
        # )
        continue

    if profit < 0 and (can_buy or num_transactions > 1):
        # Prune unprofitable buy paths
        continue

    # Hold
    frontier.append(
        (day + 1, profit, num_transactions, can_buy, last_price, path + ["H"])
    )
    # Buy
    if can_buy:
        frontier.append(
            (
                day + 1,
                profit - prices[day] - fee,
                num_transactions + 1,
                False,
                prices[day],
                path + [f"B({prices[day]})"],
            )
        )
    else:  # Sell
        if prices[day] > last_price:
            frontier.append(
                (
                    day + 1,
                    profit + prices[day],
                    num_transactions + 1,
                    True,
                    0,
                    path + [f"S({prices[day]})"],
                )
            )
answer = max(profits)

print("Answer", answer)
print("\n--------\n")

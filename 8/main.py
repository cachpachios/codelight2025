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

n_trans, fee = map(int, data[0].split())
prices = list(map(int, data[1].split()))

print(n_trans, fee, len(prices))

profit = [0 for _ in range(n_trans + 1)]
holding = [None for _ in range(n_trans + 1)]

for _day, price in enumerate(prices):
    for t in range(1, n_trans + 1):
        buy_today = profit[t - 1] - price
        holding[t] = max(holding[t], buy_today) if holding[t] is not None else buy_today
        sell_today = holding[t] + price - fee
        profit[t] = max(profit[t], sell_today)

answer = max(profit)

print("Answer", answer)
print("\n--------\n")

import sys
from utils import *
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, combinations_with_replacement
from dataclasses import dataclass
import string
from functools import cache, lru_cache


INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

data = read(INPUT_FILE)[0]
data = data[1:-1]  # Remove brackets
numbers = list(map(int, data.split(", ")))

print("Data:", numbers)

timers_count = {i: 0 for i in range(10)}
for n in numbers:
    timers_count[n] += 1

DAYS = 365
print("Initial timers:", timers_count)
for day in range(DAYS):
    timers_count_copy = timers_count.copy()
    timers_count[6] += timers_count_copy[0]
    timers_count[9] += timers_count_copy[0]
    timers_count[0] = 0
    for t in range(1, 10):
        timers_count[t - 1] += timers_count_copy[t]
        timers_count[t] -= timers_count_copy[t]
    print(
        "Day ",
        day + 1,
        "Timers:",
        {k: v for k, v in timers_count.items() if v > 0},
        "Users:",
        sum(timers_count.values()),
    )


answer = sum(timers_count.values())

# incorrect 3339422328001382


print("Answer", answer)
print("\n--------\n")

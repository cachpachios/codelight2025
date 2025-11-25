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

complexities = {
    "espresso": 1,
    "americano": 2,
    "latte": 3,
    "cappuccino": 3,
    "mocha": 4,
}

drinks = {}

for line in data:
    drink, size, t = line.split(",")
    t = int(t)
    key = f"{drink}_{size}"
    drinks[key] = sorted(drinks.get(key, []) + [t])


def comp_complexity(group, drink):
    base = complexities[drink]
    return sum(base - int(i > 0) for i in range(len(group)))


group_complexity = []

for key, timestamps in drinks.items():
    local_groups = []
    tsc = timestamps.copy()
    while tsc:
        start = tsc.pop(0)
        local_group = [start]
        while tsc and tsc[0] - start <= 5:
            local_group.append(tsc.pop(0))
        local_groups.append(local_group)
    drink, size = key.split("_")
    for group in local_groups:
        group_complexity.append((comp_complexity(group, drink), group))

print(group_complexity)
answer = sum(gc[0] for gc in group_complexity)

print("Answer", answer)
print("\n--------\n")

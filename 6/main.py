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


def find_max_in_line(arr):
    last_max = 0
    last_last_max = 0
    for x in arr:
        curr = max(last_max, last_last_max + x)
        last_last_max = last_max
        last_max = curr
        print("Current:", curr, "Last max:", last_max, "Last last max:", last_last_max)
    return last_max


for line in data:
    impacts = tuple(map(int, line.split()))

    answer = max(find_max_in_line(impacts[:-1]), find_max_in_line(impacts[1:]))
    print("Answer", answer)
    print("\n--------\n")

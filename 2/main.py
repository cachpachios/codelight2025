import sys
from utils import *
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, combinations_with_replacement
from dataclasses import dataclass
import string
from functools import cache, lru_cache


INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

for data in read(INPUT_FILE):
    current = []
    count = 0
    errors = 0

    opens = {"(": ")", "[": "]", "{": "}"}
    closes = {")": "(", "]": "[", "}": "{"}

    for c in data:
        if c in opens:
            current.append(c)
        if c in closes:
            last = current.pop()
            if closes[c] == last:
                count += 1
            else:
                errors += 1
                current.append(last)
                # break

    if len(current) > 0:
        errors += 1

    print("Errors", errors)

    if errors == 0:
        count += 1

    answer = count

    print("Answer", answer)
    print("\n--------\n")

import sys
from utils import *
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, combinations_with_replacement
from dataclasses import dataclass
import string
from functools import cache, lru_cache


INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

lines = read(INPUT_FILE)

lines = map(lambda x: "".join(filter(lambda c: c in string.ascii_letters, x)), lines)
print(lines)

answer = sum(1 for line in lines if line == line[::-1])

print("Answer", answer)

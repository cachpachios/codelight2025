import sys
from utils import *
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, combinations_with_replacement
from dataclasses import dataclass
import string
from functools import cache, lru_cache


INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

lines = read(INPUT_FILE)
IN_STATE = "IN"
OUT_STATE = "OUT"

priority = [IN_STATE, OUT_STATE]

events = []

for line in lines:
    time, user, state = line.split(" ")

    hour, minute = time.split(":")
    time = int(hour) * 60 + int(minute)

    events.append((time, user, state))

min_t = min(events, key=lambda x: x[0])[0]
max_t = max(events, key=lambda x: x[0])[0]

time_people_in = {}

time_people_in[min_t - 1] = set()

for t in range(min_t, max_t + 1):
    events_at_t = [e for e in events if e[0] == t]
    events_at_t.sort(key=lambda x: priority.index(x[2]))  # Sort by IN before OUT
    hour = t // 60
    minute = t % 60
    # print(f"{hour:02d}:{minute:02d}", events_at_t)

    people_in = time_people_in[t - 1].copy()
    for _, user, state in events_at_t:
        if state == IN_STATE:
            people_in.add(user)
        elif state == OUT_STATE:
            if user in people_in:
                people_in.remove(user)
        else:
            raise ValueError("Unknown state")
    time_people_in[t] = people_in

answer = 0
for t in range(
    min_t, max_t
):  # Note: max_t is exclusive, we shouldnt count the last minute
    people_in = time_people_in[t]
    events_at_t = [e for e in events if e[0] == t].sort(
        key=lambda x: priority.index(x[2])
    )
    if len(people_in) == 3:
        hour = t // 60
        minute = t % 60
        print(
            f"{hour:02d}:{minute:02d}",
            len(people_in),
            "PEOPLE IN:",
            people_in,
            "EVENTS:",
            events_at_t,
        )
        answer += 1

print("Answer", answer)
print("\n--------\n")

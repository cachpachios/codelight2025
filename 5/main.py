import sys
import time
from utils import *
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, combinations_with_replacement
from dataclasses import dataclass
import string
from functools import cache, lru_cache


INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"


map = read(INPUT_FILE)

def print_map_with_path(map, path, energy, total):
    lx, ly, ldir = path[-1]
    ps = ""
    total = str(total)
    ps += f"Last position: {lx},{ly} facing {ldir} Energy: {energy}/SPOILER\n"
    ps += "-"*160
    ps += "\n\n"
    dir_map = {
        ">": "→",
        "<": "←",
        "^": "↑",
        "v": "↓",
    }
    map_copy = [list(row) for row in map]
    for (x, y, dir) in path:
        map_copy[y][x] = dir_map[dir]
    
    # only print wxh area around last position
    # make sure the size is alwayhs within the map bounds, and consistent size.
    # We should not center. If we are on the top left we show 19x9 from there.
    w = 160
    h = 48
    min_x = max(0, min(lx - w // 2, len(map[0]) - w))
    max_x = min(len(map[0]), min_x + w)
    min_y = max(0, min(ly - h // 2, len(map) - h))
    max_y = min(len(map), min_y + h)
    for row in map_copy[min_y:max_y]:
        ps += "".join(row[min_x:max_x]) + "\n"
    return ps

frontier = deque()
visited = set()


MOVES = {
    ">": (1, 0),
    "^": (0, -1),
    "<": (-1, 0),
    "v": (0, 1),
}

TURN_LEFT = {
    ">": "^",
    "^": "<",
    "<": "v",
    "v": ">",
}

TURN_RIGHT = {
    ">": "v",
    "v": "<",
    "<": "^",
    "^": ">",
}

start_pos = None
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == "S":
            start_pos = (y, x, '>')
            break
    
frontier.append((start_pos, 0, []))
visited.add(start_pos)



while frontier:
    (x, y, dir), energy, path = frontier.popleft()
    # print(x,y,dir,path)
    val = map[y][x]
    if val == "E":
        input("\033[H\033[JFound exit with energy <SPOILER>. Press Enter to visualize...")
        path = path + [(x, y, dir, energy)]
        for i in range(len(path)):
            #clear screen
            subpath = path[:i+1]
            subpath = [(px, py, pdir) for (px, py, pdir, peng) in subpath]
            path_eng = path[i][3]
            ps = print_map_with_path(map, subpath, path_eng, energy)
            print("\033[H\033[J" + ps + "\n"*5)
            time.sleep(0.03)
        break
    
    # Move forward
    nx,ny = x + MOVES[dir][0], y + MOVES[dir][1]
    nv = map[ny][nx]

    if nv != "#":
        forward_state = (nx, ny, dir)
        if forward_state not in visited:
            visited.add(forward_state)
            frontier.append((forward_state, energy + 1, path + [(x, y, dir, energy)]))

    # Turn left and move forward
    dx, dy = MOVES[TURN_LEFT[dir]]
    turn_left = (x+dx, y+dy, TURN_LEFT[dir])
    nv = map[turn_left[1]][turn_left[0]]
    if turn_left not in visited and nv != "#":
        visited.add(turn_left)
        frontier.append((turn_left, energy + 2, path + [(x, y, dir, energy)]))

    # Turn right
    dx, dy = MOVES[TURN_RIGHT[dir]]
    turn_right = (x+dx, y+dy, TURN_RIGHT[dir])
    nv = map[turn_right[1]][turn_right[0]]
    if turn_right not in visited and nv != "#":
        visited.add(turn_right)
        frontier.append((turn_right, energy + 3, path + [(x, y, dir, energy)]))


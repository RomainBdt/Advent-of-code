# %%
# PART 1
import pathlib
from collections import deque, defaultdict
import re

path = pathlib.Path.cwd() / "input.txt"
lines = [x for x in open(path).read().splitlines()]


class pos:
    def __init__(self, row, col):
        pos.row = row
        pos.col = col


# read the grid
grid_row = []
col_num = max([len(line) for line in lines[:-2]])
grid_col = [list() for _ in range(col_num)]
for row, line in enumerate(lines):
    if len(line) == 0:
        break
    grid_row.append([])
    for col, x in enumerate(line):
        if x != " ":
            grid_row[-1].append((row, col, x))
            grid_col[col].append((row, col, x))

# Define starting point
start = pos(grid_row[0][0][0], grid_row[0][0][1])

# read command line
cmd = []
for x in lines[-1]:
    if x.isdigit():
        try:
            cmd[-1] = 10 * cmd[-1] + int(x)
        except:
            cmd.append(int(x))
    else:
        cmd.append(x)

d = 200
directions = ["E", "S", "W", "N"] * 100  # E, S, W, N

pos_ = start

for a in cmd:
    if isinstance(a, int):
        if directions[d] in ["E", "W"]:
            road = grid_row[pos_.row]
        else:
            road = grid_col[pos_.col]

        idx = road.index((pos_.row, pos_.col, "."))
        road = road[idx:] + road[:idx]  # road starts at pos_

        # Reverse list if direction is N or W
        if directions[d] in ["N", "W"]:
            road = [road[0]] + list(reversed(road[1:]))

        # print(directions[d], a, road)

        road = road * 100  # extend the road to avoid reaching the end

        for step in range(a + 1):
            if road[step + 1][2] == "#":
                break
        pos_.row = road[step][0]
        pos_.col = road[step][1]
        # print(pos_.row, pos_.col)

    else:  # Update direction d
        if a == "R":
            d += 1
        else:
            d -= 1


facing = directions.index(directions[d])

print("PART 1:", 1000 * (pos_.row + 1) + 4 * (pos_.col + 1) + facing)
# %%
# PART 2 inspired by hyper-neutrino
import pathlib
from collections import deque, defaultdict
import re

path = pathlib.Path.cwd() / "input.txt"
lines = [x for x in open(path).read().splitlines()]

grid = []
max_len = len(lines[0])

for row, line in enumerate(lines):
    if len(line) == 0:
        break
    grid.append([x for x in line])
    if len(grid[-1]) < max_len:
        grid[-1] += [" "] * (max_len - len(grid[-1]))

# read command line
cmd = []
for x in lines[-1]:
    if x.isdigit():
        try:
            cmd[-1] = 10 * cmd[-1] + int(x)
        except:
            cmd.append(int(x))
    else:
        cmd.append(x)


next_cell = {}
for i in range(50):
    next_cell[(0, 50 + i, -1, 0)] = (150 + i, 0, 0, 1)
    next_cell[(150 + i, 0, 0, -1)] = (0, 50 + i, 1, 0)

    next_cell[(0, 100 + i, -1, 0)] = (199, i, -1, 0)
    next_cell[(199, i, 1, 0)] = (0, 100 + i, 1, 0)

    next_cell[(i, 149, 0, 1)] = (149 - i, 99, 0, -1)
    next_cell[(149 - i, 99, 0, 1)] = (i, 149, 0, -1)

    next_cell[(49, 100 + i, 1, 0)] = (50 + i, 99, 0, -1)
    next_cell[(50 + i, 99, 0, 1)] = (49, 100 + i, -1, 0)

    next_cell[(149, 50 + i, 1, 0)] = (150 + i, 49, 0, -1)
    next_cell[(150 + i, 49, 0, 1)] = (149, 50 + i, -1, 0)

    next_cell[(100, i, -1, 0)] = (50 + i, 50, 0, 1)
    next_cell[(50 + i, 50, 0, -1)] = (100, i, 1, 0)

    next_cell[(i, 50, 0, -1)] = (149 - i, 0, 0, 1)
    next_cell[(149 - i, 0, 0, -1)] = (i, 50, 0, 1)

i = 0
while grid[0][i] == " ":
    i += 1

r = 0
c = i
dr = 0
dc = 1

for a in cmd:
    if isinstance(a, int):
        nr, nc, ndr, ndc = r, c, dr, dc
        for _ in range(a):
            if (r, c, dr, dc) in next_cell:
                nr, nc, ndr, ndc = next_cell[(r, c, dr, dc)]
            else:
                nr += dr
                nc += dc

            if grid[nr][nc] == "#":
                break
            else:
                r, c, dr, dc = nr, nc, ndr, ndc
        # print(r, c, dr, dc, a)
    else:
        if a == "R":
            dr, dc = dc, -dr
        else:
            dr, dc = -dc, dr
        # print(r, c, dr, dc, a)
        # print("-" * 10)

if dr == 0:
    if dc == 1:
        direction = 0
    else:
        direction = 2
elif dr == 1:
    direction = 1
else:
    direction = 3

print("PART 2:", 1000 * (r + 1) + 4 * (c + 1) + direction)

# %%

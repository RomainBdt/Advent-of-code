# %%
#  PART 1
import pathlib
from collections import deque, defaultdict
import re

path = pathlib.Path.cwd() / "input.txt"
lines = [x for x in open(path).read().splitlines()]

width = len(lines[0])
height = len(lines)

grid_init = defaultdict(list)
for imag, line in enumerate(lines):

    for real, ch in enumerate(line):
        if ch in ["^", "v", ">", "<"]:
            grid_init[complex(real, imag)].append(ch)

d = {"^": -1j, "v": 1j, ">": 1, "<": -1}
GRIDS = [grid_init.copy()]
grid = GRIDS[0]

while True:
    new_grid = defaultdict(list)
    for key, values in grid.items():
        for value in values:
            new_key = key + d[value]
            if int(new_key.real) == 0:
                new_key += width - 2
            elif int(new_key.real) == width - 1:
                new_key -= width - 2
            if int(new_key.imag) == 0:
                new_key += complex(0, height - 2)
            elif int(new_key.imag) == height - 1:
                new_key -= complex(0, height - 2)
            new_grid[new_key].append(value)
    grid = new_grid.copy()
    if grid in GRIDS:
        break
    else:
        GRIDS.append(new_grid.copy())


def dfs(pos, steps):
    global cache
    global fastest

    if steps >= fastest:
        return fastest

    if (
        END.real + END.imag - pos.real - pos.imag + steps
    ) >= fastest:  # no possible improvement
        return fastest

    next_pos = [pos + 1, pos + 1j, pos - 1, pos - 1j, pos]

    score = int(1e9)
    for new_pos in next_pos:
        if new_pos == END:
            score = steps + 1
            fastest = min(fastest, score)
            cache = {c for c in cache if c[1] < fastest}  # reduce size of the cache
            print(f"NEW BEST SCORE: {score}, cache size is {len(cache)}")
            break
        if (
            (new_pos not in GRIDS[steps % len(GRIDS)])
            and (0 < new_pos.real < width - 1)
            and (0 < new_pos.imag < height - 1)
            and (steps < fastest)
            and ((new_pos, steps + 1) not in cache)
        ):
            cache.add((new_pos, steps + 1))
            score = min(score, dfs(new_pos, steps + 1))

    return score  # no path


cache = set()
INIT = 1j
END = complex(width - 2, height - 1)
fastest = 1e9
print(f"PART 1. Trip took {dfs(INIT, 1) - 1} minutes")


# %%
# PART 2
def dfs(pos, steps):
    global cache
    global fastest

    if steps >= fastest:
        return fastest

    if (
        abs(END.real - pos.real) + abs(END.imag - pos.imag) + steps
    ) >= fastest:  # no possible improvement
        return fastest

    if END == 1j:
        next_pos = [pos - 1, pos - 1j, pos + 1, pos + 1j, pos]
    else:
        next_pos = [pos + 1, pos + 1j, pos - 1, pos - 1j, pos]

    score = int(1e9)
    for new_pos in next_pos:
        if new_pos == END:
            score = steps + 1
            fastest = min(fastest, score)
            cache = {c for c in cache if c[1] < fastest}  # reduce size of the cache
            # print(f"NEW BEST SCORE: {score}, cache size is {len(cache)}")
            break
        if (
            (new_pos not in GRIDS[steps % len(GRIDS)])
            and (
                ((0 < new_pos.real < width - 1) and (0 < new_pos.imag < height - 1))
                or (new_pos == INIT and steps < 1000)
            )
            and (steps < fastest)
            and ((new_pos, steps + 1) not in cache)
        ):
            cache.add((new_pos, steps + 1))
            score = min(score, dfs(new_pos, steps + 1))

    return score  # no path


INIT = 1j
END = complex(width - 2, height - 1)
time = 1

for i in range(3):
    cache = set()
    fastest = 1e9
    trip = dfs(INIT, time) - 1
    INIT, END = END, INIT
    time = trip

print(f"PART 2. All trips took {trip} minutes")

# %%
# Alternative solution with queue

INIT = 1j
END = complex(width - 2, height - 1)
q = [(INIT, 1)]
cache = []
prev_time = 0

for _ in range(3):
    while q:
        pos, time = q.pop(0)

        if pos == END:
            print(f"This trip took {time - prev_time} minutes")
            break

        time += 1
        for move in (1, 1j, -1, -1j, 0):
            next_pos = pos + move
            if (
                next_pos not in GRIDS[time % len(GRIDS)]
                and (0 < next_pos.real < width - 1)
                and (0 < next_pos.imag < height - 1)
                and ((next_pos, time) not in cache)
                or next_pos in [INIT, END]
            ):
                q.append((next_pos, time))
                cache.append((next_pos, time))

    INIT, END = END, INIT
    cache = []
    q = [(INIT, time)]
    prev_time = time

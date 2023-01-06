# %%
# PART 1
from collections import deque
import pathlib


def parse(path):
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


path = pathlib.Path.cwd() / "input.txt"
data = parse(path)

grid = [list(x) for x in open(path).read().strip().splitlines()]

for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == "S":
            sr = r
            sc = c
            grid[r][c] = "a"
        if item == "E":
            er = r
            ec = c
            grid[r][c] = "z"

q = deque()
q.append((0, sr, sc))

visited = {(sr, sc)}
exit_ = False

while not exit_:
    d, r, c = q.popleft()
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):  # out of the grid
            continue
        if (nr, nc) in visited:  # already visited
            continue
        if ord(grid[nr][nc]) - ord(grid[r][c]) > 1:  # step up too big
            continue
        if nr == er and nc == ec:  # reach target point
            print("PART 1:", d + 1)
            exit_ = True
        visited.add((nr, nc))
        q.append((d + 1, nr, nc))  # add possible step to the deque

# %%
# PART 2
# Start from the end to search for the first 'a'
from collections import deque
import pathlib


def parse(path):
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


path = pathlib.Path.cwd() / "input.txt"
data = parse(path)

grid = [list(x) for x in open(path).read().strip().splitlines()]

for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == "S":
            grid[r][c] = "a"
        if item == "E":
            er = r
            ec = c
            grid[r][c] = "z"

q = deque()
q.append((0, er, ec))

visited = {(er, ec)}
exit_ = False

while not exit_:
    d, r, c = q.popleft()
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):  # out of the grid
            continue
        if (nr, nc) in visited:  # already visited
            continue
        if ord(grid[nr][nc]) - ord(grid[r][c]) < -1:  # step down too big
            continue
        if grid[nr][nc] == "a":  # reach target point
            print("PART 2:", d + 1)
            exit_ = True
        visited.add((nr, nc))
        q.append((d + 1, nr, nc))  # add possible step to the deque

print("END")
# %%

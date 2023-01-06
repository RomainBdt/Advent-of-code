# %%
# # PART 1
import pathlib
from collections import deque, defaultdict

path = pathlib.Path.cwd() / "input.txt"
data = open(path).read().splitlines()

grid = [eval(x) for x in data]
grid.sort()

cnt = len(grid) * 6

extended_cubes = []
for n, cube1 in enumerate(grid):

    x1, y1, z1 = cube1
    extended_cubes = extended_cubes + [
        (x1, y1, z1),
        (x1 - 1, y1, z1),
        (x1 + 1, y1, z1),
        (x1, y1 - 1, z1),
        (x1, y1 + 1, z1),
        (x1, y1, z1 - 1),
        (x1, y1, z1 + 1),
    ]
    for cube2 in grid[n + 1 :]:
        x2, y2, z2 = cube2
        if cube1 == cube2:
            continue
        else:
            if x1 == x2 and y1 == y2 and abs(z1 - z2) == 1:
                cnt -= 2
            elif y1 == y2 and z1 == z2 and abs(x1 - x2) == 1:
                cnt -= 2
            elif z1 == z2 and x1 == x2 and abs(y1 - y2) == 1:
                cnt -= 2

print("part 1:", cnt)

# %%
min_x, min_y, min_z = 1e9, 1e9, 1e9
max_x, max_y, max_z = -1e9, -1e9, -1e9

for x, y, z in grid:
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
    min_z = min(min_z, z)
    max_z = max(max_z, z)

min_x -= 1
max_x += 1
min_y -= 1
max_y += 1
min_z -= 1
max_z += 1

q = [(min_x, min_y, min_z)]

MOVES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
visited = []
cnt = 0
while q:
    pos = q.pop(0)

    for move in MOVES:
        next_pos = (pos[0] + move[0], pos[1] + move[1], pos[2] + move[2])
        if (
            (min_x <= next_pos[0] <= max_x)
            and (min_y <= next_pos[1] <= max_y)
            and (min_z <= next_pos[2] <= max_z)
            and next_pos not in visited
        ):
            if next_pos in grid:
                cnt += 1
            else:
                q.append(next_pos)
                visited.append(next_pos)

print("PART 2:", cnt)


# %%

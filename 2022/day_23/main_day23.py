# %%
# PART 1 & 2
import pathlib
from collections import deque
from tqdm import trange

path = pathlib.Path.cwd() / "input.txt"
lines = [x for x in open(path).read().splitlines()]

grid = []
for line in lines:
    grid.append([x for x in line])

# extend the grid
extension = 100
for _ in range(extension):
    grid.insert(0, ["." for __ in range(len(lines[0]))])
    grid.append(["." for __ in range(len(lines[0]))])
for i in range(len(grid)):
    grid[i] = (
        ["." for __ in range(extension)] + grid[i] + ["." for __ in range(extension)]
    )

WIDTH = len(grid[0])
DEPTH = len(grid)

q = deque(["N", "S", "W", "E"])

N_CHAR = 0
for line in grid:
    N_CHAR += line.count("#")

max_round = 1000
for rnd in trange(max_round):
    elves = {}
    moves = []
    moves_to_ignore = []

    for r in range(DEPTH):
        for c in range(WIDTH):
            x = grid[r][c]

            if x == "#":
                # Check if there is other elves around
                no_neighboors = True
                for nr in range(r - 1, r + 2):
                    for nc in range(c - 1, c + 2):
                        if (0 <= nr < DEPTH) and (0 <= nc < WIDTH):
                            if grid[nr][nc] == "#" and (nr, nc) != (r, c):
                                no_neighboors = False
                                break
                # print((r, c), no_neighboors)
                if no_neighboors:
                    continue

                for direction in q:
                    if direction == "N":
                        lookup = grid[r - 1][c - 1 : c + 2]
                        move = (r - 1, c)
                    elif direction == "S":
                        lookup = grid[r + 1][c - 1 : c + 2]
                        move = (r + 1, c)
                    elif direction == "W":
                        lookup = [x[c - 1] for x in grid[r - 1 : r + 2]]
                        move = (r, c - 1)
                    elif direction == "E":
                        lookup = [x[c + 1] for x in grid[r - 1 : r + 2]]
                        move = (r, c + 1)

                    # print((r, c), direction, lookup, move)
                    if "#" not in lookup:
                        elves[(r, c)] = move
                        if move in moves:
                            moves_to_ignore.append(move)
                        else:
                            moves.append(move)
                        # print("-" * 10)
                        break

    q.append(q.popleft())

    if len(moves) == 0:
        # print("no more moves")
        print(f"PART 2. First round with no move is: {rnd + 1}")  # Answer of part 2
        break  # no more moves needed

    # Make moves
    for elf, move in elves.items():
        if move not in moves_to_ignore:
            grid[elf[0]][elf[1]] = "."
            grid[move[0]][move[1]] = "#"

    if rnd == 9:
        r_min, c_min = DEPTH, WIDTH
        r_max, c_max = 0, 0

        for r, line in enumerate(grid):
            if "#" in line:
                r_min = min(r_min, r)
                r_max = max(r_max, r)
            for c, char in enumerate(line):
                if char == "#":
                    c_min = min(c_min, c)
                    c_max = max(c_max, c)

        print("PART 1:", (r_max - r_min + 1) * (c_max - c_min + 1) - N_CHAR)

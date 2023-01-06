# %%
import pathlib
import numpy as np


def parse(path):
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


path = pathlib.Path.cwd() / "input.txt"
data = parse(path)

# %% PART 1

s = (0, 0)
H = [0, 0]
T = [0, 0]

MOVES = {
    'R' : (1, 0),
    'U' : (0, 1),
    'L' : (-1, 0),
    'D' : (0, -1)
}

def update_pos(H, T, direction):
    H[0] += MOVES[direction][0]
    H[1] += MOVES[direction][1]

    # distance = np.sqrt((H[0] - T[0])**2 + (H[1] - T[1])**2)
    h_dist = np.abs(H[0] - T[0])
    v_dist = np.abs(H[1] - T[1])
    if ((h_dist == 2) and (v_dist == 0)) or ((h_dist == 0) and (v_dist == 2)):
        T[0] += MOVES[direction][0]
        T[1] += MOVES[direction][1]
    elif ((h_dist == 2) and (v_dist == 1)):
        T[0] += MOVES[direction][0]
        T[1] = H[1]
    elif ((h_dist == 1) and (v_dist == 2)):
        T[0] = H[0]
        T[1] += MOVES[direction][1]

    return H, T

historical_pos = []
for move in data:
    direction, length = move.split()
    for _ in range(int(length)):
        H, T = update_pos(H, T, direction)
        print(H, T)
        historical_pos.append(tuple(T))

print(len(set(historical_pos)))

# %%
# PART 2

knots = 10
positions = [[0, 0] for _ in range(knots)]

MOVES = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}


def update_pos(positions, direction):
    positions[0][0] += MOVES[direction][0]
    positions[0][1] += MOVES[direction][1]

    for i in range(knots - 1):
        h_dist = positions[i][0] - positions[i + 1][0]
        v_dist = positions[i][1] - positions[i + 1][1]

        if abs(h_dist) == 2:
            positions[i + 1][0] += h_dist // 2
            if abs(v_dist) == 1:
                positions[i + 1][1] = positions[i][1]
        if abs(v_dist) == 2:
            positions[i + 1][1] += v_dist // 2
            if abs(h_dist) == 1:
                positions[i + 1][0] = positions[i][0]

    return positions


historical_pos = []
for move in data:
    direction, length = move.split()
    print(direction, length)
    for _ in range(int(length)):
        positions = update_pos(positions, direction)
        print(positions)
        historical_pos.append(tuple(positions[-1]))

print(len(set(historical_pos)))
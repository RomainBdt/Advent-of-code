from pathlib import Path
from time import time
from itertools import combinations
from collections import OrderedDict

start_time = time()
file_num = 2
filename = "test.txt" if file_num == 1 else "input.txt"
path = Path(__file__).resolve().parent / filename

with open(path, mode="r", encoding="utf-8") as fid:
    lines = [tuple(map(int, (line.strip().split(',')))) for line in fid]

PAIRS = 10 if file_num == 1 else 1000

import numpy as np

def euclidean_distance_np(point1, point2):
    """
    Calculate Euclidean distance using NumPy.
    """
    p1 = np.array(point1, dtype=float)
    p2 = np.array(point2, dtype=float)
    
    if p1.shape != p2.shape:
        raise ValueError("Points must have the same number of dimensions.")
    
    return np.linalg.norm(p1 - p2)

distances = dict()
for idx1, P1 in enumerate(lines):
    for idx2, P2 in enumerate(lines):
        if (idx2, idx1) in distances.keys() or idx1 == idx2:
            continue
        dist = euclidean_distance_np(P1, P2)
        distances[(idx1, idx2)] = dist

sorted_dict = OrderedDict(sorted(distances.items(), key=lambda item: item[1]))

groups = [[]]

def get_group_index(val):
    for i, group in enumerate(groups):
        if val in group:
            return i
    return None

for (idx1, idx2) in list(sorted_dict.keys())[:PAIRS]:
    group_idx1 = get_group_index(idx1)
    group_idx2 = get_group_index(idx2)

    if group_idx1:
        if group_idx2:
            # Already in the same group
            if group_idx1 == group_idx2:
                continue
            # Need to merge the 2 groups
            groups[group_idx1].extend(groups[group_idx2])
            groups[group_idx2] = []
        else:
            # Add idx2 to the group of idx1
            groups[group_idx1].append(idx2)
    elif group_idx2:
        groups[group_idx2].append(idx1)
    else:
        groups.append([idx1, idx2])

sorted_length = sorted([len(x) for x in groups])
result = sorted_length[-1] * sorted_length[-2] * sorted_length[-3]

print("Part 1:", result)

groups = [[]]
for (idx1, idx2) in sorted_dict.keys():
    group_idx1 = get_group_index(idx1)
    group_idx2 = get_group_index(idx2)

    if group_idx1:
        if group_idx2:
            # Already in the same group
            if group_idx1 == group_idx2:
                continue
            # Need to merge the 2 groups
            groups[group_idx1].extend(groups[group_idx2])
            groups[group_idx2] = []
        else:
            # Add idx2 to the group of idx1
            groups[group_idx1].append(idx2)
    elif group_idx2:
        groups[group_idx2].append(idx1)
    else:
        groups.append([idx1, idx2])

    if max([len(x) for x in groups]) == len(lines):
        result = lines[idx1][0] * lines[idx2][0]
        break

print("Part 2:", result)

print(f"Time: {time() - start_time:.6f} seconds")
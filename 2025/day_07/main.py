from pathlib import Path
from time import time


start_time = time()
file_num = 2
filename = "test.txt" if file_num == 1 else "input.txt"
path = Path(__file__).resolve().parent / filename

with open(path, mode="r", encoding="utf-8") as fid:
    puzzle = [line.strip() for line in fid]

indexes = [set([puzzle[0].index('S')])]
split_count = 0
for line in puzzle[1:]:
    next_indexes = []
    for idx in indexes[-1]:
        if line[idx] == '^':
            next_indexes.append(idx-1)
            next_indexes.append(idx+1)
            split_count += 1
        else:
            next_indexes.append(idx)
    # print(indexes)
    indexes.append(set(next_indexes))

print("Part 1:", split_count)

from collections import defaultdict

# The dict key is the index position and its value is the number of quantum tachyon manifold
d = defaultdict(int)
d[puzzle[0].index('S')] += 1

for line in puzzle[1:]:
    next_d = defaultdict(int)
    for idx, weight in d.items():
        if line[idx] == '^':
            next_d[idx-1] += weight
            next_d[idx+1] += weight
        else:
            next_d[idx] += weight
    d = next_d.copy()

print("Part 2:", sum([v for v in next_d.values()]))

print(f"Time: {time() - start_time:.6f} seconds")
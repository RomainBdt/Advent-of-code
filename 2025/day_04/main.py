from pathlib import Path
from time import time


start_time = time()
file_num = 2
filename = "test.txt" if file_num == 1 else "input.txt"
path = Path(__file__).resolve().parent / filename

with open(path, mode="r", encoding="utf-8") as fid:
    grid = [line.strip() for line in fid]


R = len(grid)
C = len(grid[0])

def remove_roll(grid):
    result = 0
    grid_copy = grid.copy()
    for r, row in enumerate(grid):
        for c, roll in enumerate(row):
            if grid[r][c] != '@':
                continue
            count = 0
            for rr in [-1, 0, 1]:
                idr = r + rr
                if idr < 0 or idr >= R:
                    continue
                for cc in [-1, 0, 1]:
                    if rr == 0 and cc == 0:
                        continue
                    idc = c + cc
                    if idc < 0 or idc >= C:
                        continue
                    if grid[idr][idc] == '@':
                        count += 1
            if count < 4:
                result += 1
                updated_line = list(grid_copy[r])
                updated_line[c] = 'x'
                grid_copy[r] = "".join(updated_line)

    for line in grid_copy:
        # print(line)
        line.replace('x', '.')

    return result, grid_copy

result, _ = remove_roll(grid)

print("Part 1", result)

result = 0
i = 0
while(i < 1e9):
    i += 1
    result_prev = result
    count, grid = remove_roll(grid)
    result += count
    if result_prev == result:
        break

print("Part 2", result)

print(f"Time: {time() - start_time:.6f} seconds")
from pathlib import Path
from time import time

start = time()
file_num = 2
filename = "test.txt" if file_num == 1 else "input.txt"
path = Path(__file__).resolve().parent / filename

with open(path, mode="r", encoding="utf-8") as fid:
    puzzle_input = [line.strip() for line in fid]

dial = 50
counter = 0

for r in puzzle_input:
    rotation = r[0]
    steps = int(r[1:])
    sign = 1 if rotation == "R" else -1
    dial += sign * steps
    if dial % 100 == 0:
        counter += 1
    dial = dial % 100
print(f"Part 1: {counter}")

dial = 50
counter = 0
for r in puzzle_input:
    rotation = r[0]
    steps = int(r[1:])
    sign = 1 if rotation == "R" else -1

    dial_temp = dial
    # Reverse direction for calculation when going left
    if sign == -1 and dial_temp != 0:
        dial_temp = 100 - dial_temp
    dial_temp += steps
    counter += dial_temp // 100

    dial += sign * steps
    dial = dial % 100

print(f"Part 2: {counter}")
print(f"Time: {time() - start:.6f} seconds")
from pathlib import Path
from time import time


start_time = time()
file_num = 2
filename = "test.txt" if file_num == 1 else "input.txt"
path = Path(__file__).resolve().parent / filename

with open(path, mode="r", encoding="utf-8") as fid:
    puzzle_input = [line.strip() for line in fid]

result = 0
for line in puzzle_input:
    digits = sorted(int(x) for x in line)[::-1]
    max_value = digits[0]
    second_max_value = digits[1]
    index_max_value = line.index(str(max_value))

    # Le dernier digit est égal au max
    if index_max_value == len(line)-1:
        # Le dernier digit est égal au max
        joltage = int(str(second_max_value) + str(max_value))
    else:
        subline = line[index_max_value+1:]
        second_digit = max(int(x) for x in subline)
        joltage = int(str(max_value) + str(second_digit))
    result += joltage

print("Part 1", result)

K = 12
result = 0
for line in puzzle_input:
    n = len(line)
    start_idx = 0
    number_str = ""
    for i in range(K):
        end_idx = n - (K - i) + 1
        subline = line[start_idx:end_idx]
        max_value_str = max(subline)
        start_idx += subline.index(max_value_str) + 1
        number_str += max_value_str
    result += int(number_str)

print("Part 2", result)

print(f"Time: {time() - start_time:.6f} seconds")
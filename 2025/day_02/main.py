from pathlib import Path
from time import time

start_time = time()
file_num = 2
filename = "test.txt" if file_num == 1 else "input.txt"
path = Path(__file__).resolve().parent / filename

with open(path, mode="r", encoding="utf-8") as fid:
    puzzle_input = [line.strip().split(",") for line in fid][0]

invalid_ids = []
for segment in puzzle_input:
    start, end = segment.split('-')
    for x in range(int(start), int(end)+1):
        x = str(x)
        half_length = int(len(x) / 2)
        if x[:half_length] == x[half_length:]:
            invalid_ids.append(int(x))

print('Part 1:', sum(invalid_ids))

invalid_ids = []
for segment in puzzle_input:
    start, end = segment.split('-')
    for number in range(int(start), int(end)+1):
        number_str = str(number)
        half_length = int(len(number_str) / 2)
        for size in range(half_length+1):
            _number_str = number_str
            to_replace = _number_str[:size]
            _number_str_replaced = _number_str.replace(to_replace, "")
            if len(_number_str_replaced) == 0:
                invalid_ids.append(int(number))
                break

print('Part 2:', sum(invalid_ids))
print(f"Time: {time() - start_time:.6f} seconds")
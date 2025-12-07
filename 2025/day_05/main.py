from pathlib import Path
from time import time


start_time = time()
file_num = 2
filename = "test.txt" if file_num == 1 else "input.txt"
path = Path(__file__).resolve().parent / filename

with open(path, mode="r", encoding="utf-8") as fid:
    puzzle = [line.strip() for line in fid]

result = 0
ranges = []
ingredients = []
blank_line_met = False
for line in puzzle:
    if len(line) == 0:
        blank_line_met = True
        continue
    if not blank_line_met: 
        ranges.append([int(x) for x in line.split('-')])
    else:
        ingredients.append(int(line))

for ingredient in ingredients:
    found = False
    for start, end in ranges:
        if start <= ingredient <= end:
            result += 1
            break

        
print("Part 1:", result)

sorted_ranges = sorted(ranges)
new_ranges = []

for start, end in sorted_ranges:
    if not new_ranges:
        # Add the first range to the list
        new_ranges.append([start, end])
        continue
    last_range_start, last_range_end = new_ranges[-1]
    if start <= last_range_end:
        # The tested range overlaps the last new_ranges, extending last new_ranges
        new_ranges[-1] = [last_range_start, max(end, last_range_end)]
    else:
        # The tested range does not overlap, adding in it to the new_ranges
        new_ranges.append([start, end])

counter = 0
for start, end in new_ranges:
    counter += end - start + 1

print("Part 2:", counter)

print(f"Time: {time() - start_time:.6f} seconds")
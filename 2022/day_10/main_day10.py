# %%
# PART 1
import pathlib


def parse(path):
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


path = pathlib.Path.cwd() / "input.txt"
data = parse(path)

new_data = []

for line in data:
    if line.startswith("noop"):
        new_data.append(line)
    else:
        new_data.append("addx 0")
        new_data.append(line)

scores = []
x = 1

for idx, line in enumerate(new_data):
    idx += 1
    if idx in [20, 60, 100, 140, 180, 220]:
        scores.append((idx) * x)
        print(idx, x, scores)
    if line.startswith("addx"):
        x += int(line.split()[1])
print(sum(scores))

# %%
# PART2
for line in data:
    if line.startswith("noop"):
        new_data.append(line)
    else:
        new_data.append("addx 0")
        new_data.append(line)

x = 1
total = []
row = []
cst = 0
for idx, line in enumerate(new_data):
    if (idx - cst) in [x - 1, x, x + 1]:
        row.append("#")
    else:
        row.append(" ")

    if idx + 1 in [40, 80, 120, 160, 200, 240]:
        print("".join(row))
        cst += 40
        total.append(row)
        row = []
    if line.startswith("addx"):
        x += int(line.split()[1])

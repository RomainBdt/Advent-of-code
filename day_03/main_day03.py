# %%
import pathlib


def parse(path):
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


path = pathlib.Path.cwd() / "input.txt"
data = parse(path)

# %%
# PART 1
total = 0
for i in data:
    compartment_length = int(len(i) / 2)
    common_item = set(i[:compartment_length]).intersection(i[compartment_length:]).pop()
    if common_item.islower():
        number = ord(common_item) - 96
    else:
        number = ord(common_item) - 64 + 26
    # print(common_item, number)
    total += number

print(total)

# %%
# PART 2
count = 3
total = 0
for i in data:
    count += 1
    if count <= 3:
        badge = badge.intersection(set(i[:]))
    else:
        count = 1
        badge = set(i[:])

    if count == 3:
        common_item = badge.pop()
        if common_item.islower():
            total += ord(common_item) - 96
        else:
            total += ord(common_item) - 64 + 26

        # print(count, i, common_item, total)
print(total)

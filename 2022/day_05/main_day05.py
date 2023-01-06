# %%
import pathlib


def parse(path):
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line for line in fid]
    return puzzle_input


path = pathlib.Path.cwd() / "input.txt"
data = parse(path)

# %% Part 1
stacks = {}
for col in range(len(data[0]) // 4):
    stacks[col + 1] = []

stack_complete = False

for line in data:
    if len(line) > 1:
        if line[1].isdigit():
            stack_complete = True
            continue
        if not stack_complete:
            for i, crane in enumerate(line[1::4]):
                i += 1  # to match input column index
                if crane.isalpha():
                    stacks[i].insert(0, crane)

        else:
            line_split = line.split()
            move = int(line_split[1])
            from_ = int(line_split[3])
            to = int(line_split[5])
            for _ in range(int(move)):
                stacks[to].append(stacks[from_].pop())

print("".join([x[-1] for x in stacks.values()]))

# %% Part 2
stacks = {}
for col in range(len(data[0]) // 4):
    stacks[col + 1] = []

stack_complete = False

for line in data:
    if len(line) > 1:
        if line[1].isdigit():
            stack_complete = True
            continue
        if not stack_complete:
            for i, crane in enumerate(line[1::4]):
                i += 1  # to match input column index
                if crane.isalpha():
                    stacks[i].insert(0, crane)

        else:
            line_split = line.split()
            move = int(line_split[1])
            from_ = int(line_split[3])
            to = int(line_split[5])
            temp = []
            for _ in range(int(move)):
                temp.insert(0, stacks[from_].pop())
            stacks[to].extend(temp)

print("".join([x[-1] for x in stacks.values()]))

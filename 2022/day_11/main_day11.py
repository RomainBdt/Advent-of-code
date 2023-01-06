# %%
# PART 1
import pathlib


def parse(path):
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


path = pathlib.Path.cwd() / "input.txt"
data = parse(path)

monkeys = {}
for i, line in enumerate(data):
    if line.startswith("Monkey"):

        items = data[i + 1].replace(",", "").split()
        items = items[2:]

        monkeys[line[-2]] = {
            "items": items,
            "op": data[i + 2].split("=")[1],
            "test": data[i + 3].split()[-1],
            "true": data[i + 4].split()[-1],
            "false": data[i + 5].split()[-1],
            "cnt": 0,
        }

for _ in range(20):
    for monkey in monkeys.values():
        for __ in range(len(monkey["items"])):
            monkey["cnt"] += 1
            old = int(monkey["items"].pop(0))
            test = eval(monkey["op"]) // 3
            if test % int(monkey["test"]) == 0:
                monkeys[monkey["true"]]["items"].append(test)
                # print(f'Item with worry level {test} is thrown to monkey {monkey["true"]}. old:{old}; formula: {monkey["op"]} ')
            else:
                monkeys[monkey["false"]]["items"].append(test)
                # print(f'Item with worry level {test} is thrown to monkey {monkey["false"]}. old:{old}; formula: {monkey["op"]} ')
inspections_cnt = []
for key in monkeys.keys():
    # print(sorted(monkey['items']))
    print(key, monkeys[key]["cnt"])
    inspections_cnt.append(monkeys[key]["cnt"])
    pass
inspections_cnt.sort()
print("PART 1", inspections_cnt[-1] * inspections_cnt[-2])
print("END")

# # %%
# PART 2
import pathlib
import math


def parse(path):
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


path = pathlib.Path.cwd() / "input.txt"
data = parse(path)
lcm_list = []
monkeys = {}
for i, line in enumerate(data):
    if line.startswith("Monkey"):

        items = data[i + 1].replace(",", "").split()
        items = items[2:]

        monkeys[line[-2]] = {
            "items": [int(item) for item in items],
            "op": data[i + 2].split("=")[1],
            "test": int(data[i + 3].split()[-1]),
            "true": data[i + 4].split()[-1],
            "false": data[i + 5].split()[-1],
            "cnt": 0,
        }
        lcm_list.append(monkeys[line[-2]]["test"])

lcm = math.lcm(*lcm_list)

for _ in range(10000):
    for monkey in monkeys.values():
        for __ in range(len(monkey["items"])):
            monkey["cnt"] += 1
            old = monkey["items"].pop(0)
            test = eval(monkey["op"])
            test = test % lcm
            # print(test)
            if test % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(test)
                # print(f'Item with worry level {test} is thrown to monkey {monkey["true"]}. old:{old}; formula: {monkey["op"]} ')
            else:
                monkeys[monkey["false"]]["items"].append(test)
                # print(f'Item with worry level {test} is thrown to monkey {monkey["false"]}. old:{old}; formula: {monkey["op"]} ')

inspections_cnt = []
for key in monkeys.keys():
    print(key, monkeys[key]["cnt"])
    inspections_cnt.append(monkeys[key]["cnt"])

inspections_cnt.sort()
print("PART 2", inspections_cnt[-1] * inspections_cnt[-2])
print("END")

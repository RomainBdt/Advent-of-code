# %%
# PART 1
import pathlib
from collections import deque, defaultdict
import re

path = pathlib.Path.cwd() / "input.txt"
data = {x.split(": ")[0]: x.split(": ")[1] for x in open(path).read().splitlines()}


pat = "([a-z]{4})"
for name, yell in data.items():
    olds = re.findall(pat, yell)
    for old in olds:
        yell = yell.replace(old, f"data['{old}']")
    if len(olds) == 0:
        data[name] = int(yell)
    else:
        data[name] = yell


i = 0

while not isinstance(data["root"], int) and i < 100:
    i += 1
    j = 0
    for name, yell in data.items():
        if isinstance(yell, int):
            j += 1
        else:
            try:
                data[name] = int(eval(yell))
            except:
                continue
    print(i, j)

print(data["root"])

# %%
# PART 2
import pathlib
import re
from scipy.optimize import minimize

path = pathlib.Path.cwd() / "input.txt"
data = {x.split(": ")[0]: x.split(": ")[1] for x in open(path).read().splitlines()}


pat = "([a-z]{4})"
for name, yell in data.items():
    olds = re.findall(pat, yell)
    for old in olds:
        yell = yell.replace(old, f"data['{old}']")
    if len(olds) == 0:
        data[name] = int(yell)
    else:
        data[name] = f"({yell})"


data["humn"] = "xx"

for _ in range(20):
    for name, yell in data.items():
        if name == "root":
            continue
        try:
            data[name] = int(eval(yell))
        except:
            continue

strings = [key for key in data.keys() if isinstance(data[key], str)]
data_save = data.copy()


def f(i):
    data = data_save.copy()
    data["humn"] = i
    stop = 0
    while (
        not (isinstance(data["tcmj"], int) and isinstance(data["qggp"], int))
        and stop < 100
    ):
        j = 0
        stop += 1

        for name in strings:
            if name == "root":
                continue
            yell = data[name]
            try:
                data[name] = int(eval(yell))
            except:
                continue
    return data["tcmj"] - data["qggp"]


lb = 0
hb = 10000000000000000000000000000

# find the correct value
while True:
    mid = (lb + hb) // 2
    res = f(mid)

    if res == 0:
        print(mid)
        break
    elif res > 0:
        lb = mid
    else:
        hb = mid
# %%

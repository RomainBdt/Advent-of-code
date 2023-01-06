# %%
# PART 1
import pathlib
from collections import deque, defaultdict

path = pathlib.Path.cwd() / "input.txt"
data = [int(x) for x in open(path)]

n = len(data) - 1
offset = (abs(min(data)) // n + 1) * n

data = list(enumerate(data))
tmp = data.copy()

for x in data:
    _, num = x
    if num == 0:
        zero = x
        continue

    idx = tmp.index(x)

    new_idx = idx + num + offset
    new_idx %= n
    if new_idx == 0:
        new_idx = n

    tmp.remove(x)
    tmp.insert(new_idx, x)


idx_0 = tmp.index(zero)
tmp = tmp * (3000 // len(tmp) + 2)
ans = tmp[1000 + idx_0][1] + tmp[2000 + idx_0][1] + tmp[3000 + idx_0][1]
print(ans)

# %%
# PART 2
path = pathlib.Path.cwd() / "input.txt"
data = [int(x) * 811589153 for x in open(path)]

n = len(data) - 1
offset = (abs(min(data)) // n + 1) * n

data = list(enumerate(data))
tmp = data.copy()

for _ in range(10):
    for x in data:
        _, num = x
        if num == 0:
            zero = x
            continue

        idx = tmp.index(x)

        new_idx = idx + num + offset
        new_idx %= n
        if new_idx == 0:
            new_idx = n

        tmp.remove(x)
        tmp.insert(new_idx, x)


idx_0 = tmp.index(zero)
tmp = tmp * (3000 // len(tmp) + 2)
ans = tmp[1000 + idx_0][1] + tmp[2000 + idx_0][1] + tmp[3000 + idx_0][1]
print(ans)

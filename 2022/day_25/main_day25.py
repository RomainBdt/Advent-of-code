# %%
import pathlib
from collections import deque, defaultdict
import re

path = pathlib.Path.cwd() / "input.txt"
lines = [x for x in open(path).read().splitlines()]


def snafu_to_dec(s):
    ans = 0
    for i, ch in enumerate(reversed(s)):
        if ch == "-":
            ch = -1
        elif ch == "=":
            ch = -2
        ans += int(ch) * 5**i
    return ans


total = 0
for line in lines:
    total += snafu_to_dec(line)

num = 1
p = 1

while num < total:
    num += 2 * 5**p
    p += 1

snafu = ["2" for _ in range(p)]
for pow, x in enumerate(range(p)):
    for y in "210-=":
        s = snafu.copy()
        s[x] = y
        if snafu_to_dec("".join(s)) < total:
            break
        else:
            snafu = s

print("".join(snafu))
# %%

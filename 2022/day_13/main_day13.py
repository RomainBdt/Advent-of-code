# %%

import pathlib
import ast


def parse(path):
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


path = pathlib.Path.cwd() / "input.txt"
data = parse(path)


def check(left, right):
    try:
        left = int(left)
        try:
            right = int(right)
            if left < right:
                return True
            elif left > right:
                return False
            else:
                return None
        except:
            return check([left], right)
    except:
        try:
            right = int(right)
            return check(left, [right])
        except:
            i = 0
            ans = None
            while i < len(left):
                if i == len(right):
                    return False
                ans = check(left[i], right[i])
                if ans is not None:
                    return ans
                i += 1
            if len(left) == len(right):
                return None
            else:
                return True


cnt = 0

for i, line in enumerate(data):

    if i % 3 == 0:
        left = ast.literal_eval(data[i])
        right = ast.literal_eval(data[i + 1])
        ans = check(left, right)
        if ans:
            cnt += i // 3 + 1

print(f"Part 1 = {cnt}")
# %%
pos_div2 = 1
pos_div6 = 2

for i, line in enumerate(data):

    if i % 3 == 0:
        left = ast.literal_eval(data[i])
        if check(left, [[2]]):
            pos_div2 += 1
        if check(left, [[6]]):
            pos_div6 += 1

        left = ast.literal_eval(data[i + 1])
        if check(left, [[2]]):
            pos_div2 += 1
        if check(left, [[6]]):
            pos_div6 += 1

print(f"Part 2 = {pos_div2 * pos_div6}")

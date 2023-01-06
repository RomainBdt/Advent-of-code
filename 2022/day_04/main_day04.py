# %%
import pathlib


def parse(path):
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


path = pathlib.Path.cwd() / "input.txt"
data = parse(path)


def give_full_list(text="72-77"):
    start = int(text.split("-")[0])
    end = int(text.split("-")[1]) + 1
    output_list = [i for i in range(start, end)]
    return output_list


# %%
# part 1
ans = 0
for i in data:
    list_all = i.split(",")
    set_0 = set(give_full_list(list_all[0]))
    set_1 = set(give_full_list(list_all[1]))
    if set_0.issubset(set_1) or set_1.issubset(set_0):
        ans += 1
print(ans)

# %%
# part 2
ans = 0
for i in data:
    list_all = i.split(",")
    set_0 = set(give_full_list(list_all[0]))
    set_1 = set(give_full_list(list_all[1]))
    if len(set_0.intersection(set_1)) > 0:
        ans += 1
print(ans)

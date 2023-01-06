# %%

import pathlib


def parse(path):
    with open(path, mode="r", encoding="utf-8") as fid:
        puzzle_input = [line.strip() for line in fid]
    return puzzle_input


path = pathlib.Path.cwd() / "input.txt"
data = parse(path)
data = [line.split(" -> ") for line in data]


def get_all_points_between_two(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    lst = []
    if x1 == x2:
        for i in range(min([y1, y2]), max([y1, y2]) + 1):
            lst.append((x1, i))
    else:
        for i in range(min([x1, x2]), max([x1, x2]) + 1):
            lst.append((i, y1))
    return lst


grid = [[], []]
rocks = set()
for line in data:
    coor = [eval(z) for z in line]
    t1 = coor[0]
    for t2 in coor[1:]:
        rocks.update(set(get_all_points_between_two(t1, t2)))
        t1 = t2

bottom = 0
for _, y in rocks:
    bottom = max(bottom, y)

for y in range(10):
    row = []
    for x in range(494, 504):
        if tuple([x, y]) in rocks:
            row.append("#")
        else:
            row.append(".")
    print("".join(row))


sand = set()
busy = rocks.copy()
i = 0
while i < 20000:  # add sand
    i += 1
    x, y = 500, 0
    busy.update(sand)
    for _ in range(bottom):
        print(tuple([x, y]))
        if tuple([x, y + 1]) not in busy:
            print("move down")
            y += 1
        elif tuple([x - 1, y + 1]) not in busy:
            print("move left")
            x -= 1
            y += 1
        elif tuple([x + 1, y + 1]) not in busy:
            print("move right")
            x += 1
            y += 1
        else:
            print(f"sand stopped at {tuple([x, y])}")
            sand.update({(x, y)})
            break  # sand found a stable position
    else:
        print("sand reached the bottom")  # sand did not found a stable position
        break  # end of while
print(len(sand))


print("END Part 1")

# %%

busy = rocks.copy()
i = 0
stop = False

while not stop:  # add sand
    i += 1
    x, y = 500, 0
    for v in range(bottom + 2):
        # print(tuple([x, y]), v)
        if v > bottom:
            print(f"sand stopped at {tuple([x, y])} on the floor")
            busy.update({(x, y)})
            break
        elif tuple([x, y + 1]) not in busy:
            # print('move down')
            y += 1
        elif tuple([x - 1, y + 1]) not in busy:
            # print('move left')
            x -= 1
            y += 1
        elif tuple([x + 1, y + 1]) not in busy:
            # print('move right')
            x += 1
            y += 1
        else:
            print(f"sand stopped at {tuple([x, y])}")
            if (x, y) == (500, 0):
                stop = True
            busy.update({(x, y)})
            break  # sand found a stable position

    if i > 100000:
        break
print(len(busy) - len(rocks))


print("END Part 2")
# %%

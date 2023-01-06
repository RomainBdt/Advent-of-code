# %%
import pathlib

path = pathlib.Path.cwd() / "input.txt"

sensors = []
beacons = []

for line in open(path):

    x = [list(p.split("x="))[-1] for p in line.strip().split(",")]
    x1, x2 = list(map(int, x[:2]))

    y = [list(p.split("y="))[-1] for p in line.strip().split(":")]
    y1, y2 = list(map(int, y[:2]))

    sensors.append((x1, y1))
    beacons.append((x2, y2))

cov = set()
the_row = 2000000
# the_row = 10

for (x1, y1), (x2, y2) in zip(sensors, beacons):
    manh_dist = abs(x1 - x2) + abs(y1 - y2)
    if y1 - manh_dist <= the_row <= y1 + manh_dist:
        v_dist = abs(the_row - y1)
        for i in range(x1 - manh_dist + v_dist, x1 + manh_dist - v_dist + 1):
            cov.add((i, the_row))


print(len(cov.difference(sensors).difference(beacons)))
print("END PART 1")

# %%
# PART 2
import pathlib
from tqdm import trange

path = pathlib.Path.cwd() / "input.txt"

sensors = []
beacons = []

for line in open(path):

    x = [list(p.split("x="))[-1] for p in line.strip().split(",")]
    x1, x2 = list(map(int, x[:2]))

    y = [list(p.split("y="))[-1] for p in line.strip().split(":")]
    y1, y2 = list(map(int, y[:2]))

    sensors.append((x1, y1))
    beacons.append((x2, y2))

size = 4000000
stop = False

for y in trange(size):
    intervals = []
    for (x1, y1), (x2, y2) in zip(sensors, beacons):

        manh_dist = abs(x1 - x2) + abs(y1 - y2)
        ofst = manh_dist - abs(y1 - y)

        if ofst < 0:
            continue

        intervals.append((x1 - ofst, x1 + ofst))

    intervals.sort()

    mini = intervals[0][0]
    maxi = intervals[0][1]

    if mini > 0:
        print("mini is not small enough")

    for lo, hi in intervals:
        if lo <= maxi + 1:  # update segment
            maxi = max(maxi, hi)
        else:  # found missing point
            print("intervals disconnect at: ", maxi, lo)
            print("uncovered is :", y, maxi + 1)
            print("result is : ", (maxi + 1) * size + y)
            stop = True
            break
        if maxi > size:  # segment covers all points
            break
    if stop:
        break

# %%

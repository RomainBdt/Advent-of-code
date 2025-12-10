from pathlib import Path
from time import time
import pandas as pd
from tqdm import tqdm

start_time = time()
file_num = 2
filename = "test.txt" if file_num == 1 else "input.txt"
path = Path(__file__).resolve().parent / filename

with open(path, mode="r", encoding="utf-8") as fid:
    lines = [tuple(map(int, (line.strip().split(',')))) for line in fid]

areas = []

for i, (x1, y1) in enumerate(lines):
    for j, (x2, y2) in enumerate(lines):
        if i > j:
            areas.append((
                (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1),
                i,
                j
            ))
areas = sorted(areas, reverse=True)

print("Part 1:", areas[0][0])

df = pd.DataFrame(lines)
df.columns = ["x", "y"]

def validate_wall(s, l1, l2):
    """ Function that returns True if there is continuous wall in s from l1 to l2"""
    df = s.to_frame()
    df.columns = ["z"]
    df['group'] = (df.index.to_series().diff() != 1).cumsum()

    # if last group contains the max index, merge with the first group
    if df.index[-1] == len(lines) - 1 and df.index[0] == 0:
        last_group = df['group'].iloc[-1]
        df.loc[df['group'] == last_group, 'group'] = df['group'].iloc[0]

    for group_id in df['group'].unique():
        df_temp = df[df['group'] == group_id]
        if min(df_temp.z) <= min(l1, l2) and max(df_temp.z) >= max(l1, l2):
            return True
    else:
        return False

for area in tqdm(areas):
    x1, y1 = lines[area[1]]
    x2, y2 = lines[area[2]]
    check_SE, check_SW = False, False
    check_NE, check_NW = False, False

    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    # If there is a point inside the rectangle, skip
    if len(df[(min_x < df.x) & (df.x < max_x) & (min_y < df.y) & (df.y < max_y)]) > 0:
        continue

    southwest = df[(df.x <= min_x) & (df.y <= min_y)]
    southeast = df[(df.x >= max_x) & (df.y <= min_y)]
    northwest = df[(df.x <= min_x) & (df.y >= max_y)]
    northeast = df[(df.x >= max_x) & (df.y >= max_y)]

    if(
        len(southwest) > 0 and
        len(southeast) > 0 and
        len(northwest) > 0 and
        len(northeast) > 0
    ):
        southwall = df[df.y <= min_y]
        if not validate_wall(southwall.x, min_x, max_x):
            continue
        eastwall = df[df.x >= max_x]
        if not validate_wall(eastwall.y, min_y, max_y):
            continue
        northwall = df[df.y >= max_y]
        if not validate_wall(northwall.x, min_x, max_x):
            continue
        westwall = df[df.x <= min_x]
        if not validate_wall(westwall.y, min_y, max_y):
            continue
        break

print("Part 2:", area[0])
print(f"Time: {time() - start_time:.6f} seconds")
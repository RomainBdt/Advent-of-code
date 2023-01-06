# %%
# PART 1
import pathlib
from collections import deque, defaultdict

path = pathlib.Path.cwd() / "input.txt"
data = {}

for line in open(path):
    words = line.split()
    # print(words)
    data[words[1]] = {
        "rate": int(words[4].split("=")[1][:-1]),
        "valves": [i[:2] for i in words[9:]],
    }

pos_rate = set()
for v in data:
    if data[v]["rate"] > 0:
        pos_rate.add(v)


def get_path_length(start, end):
    dq = deque()  # time, current_valve
    vis = set(start)
    for valve in data[start]["valves"]:
        dq.append((1, valve))

    while dq:
        valve = dq.popleft()

        if valve[1] == end:
            break
        if valve[1] not in vis:
            vis.add(valve[1])
            for next_valve in data[valve[1]]["valves"]:
                dq.append((valve[0] + 1, next_valve))
    return valve[0]


main_path = {}
for start in list(pos_rate) + ["AA"]:
    for end in pos_rate:
        if start != end:
            if start in main_path.keys():
                main_path[start][end] = get_path_length(start, end)
            else:
                main_path[start] = {end: get_path_length(start, end)}

dq = deque()
dq.append({"time": 1, "valve": "AA", "rate": 0, "total": 0, "opened": []})
i = 0
res = []

MAX_TIME = 30
max_total_rate = 0

while dq and i < 100000000:
    i += 1
    d = dq.popleft()
    current_valve = d["valve"]

    if d["time"] > MAX_TIME:
        continue
    else:
        extrapolate_total_rate = d["total"] + d["rate"] * (MAX_TIME - d["time"])
        if extrapolate_total_rate > max_total_rate:
            best_d = d
        max_total_rate = max(max_total_rate, extrapolate_total_rate)

    for target_valve in pos_rate:
        # add valve and open it
        if (target_valve not in d["opened"]) and (current_valve != target_valve):
            path_length = main_path[current_valve][target_valve]
            dq.append(
                {
                    "time": d["time"]
                    + path_length
                    + 1,  # current time + travel + opening
                    "valve": target_valve,
                    "rate": d["rate"] + data[target_valve]["rate"],
                    "total": d["total"]
                    + d["rate"] * (path_length + 1)
                    + data[target_valve]["rate"],
                    "opened": d["opened"] + [target_valve],
                }
            )

print(max_total_rate)

# %%
%%time
# Part 2 New version
import pathlib
from collections import deque
from tqdm import trange

path = pathlib.Path.cwd() / "input.txt"
data = {}

for line in open(path):
    words = line.split()
    # print(words)
    data[words[1]] = {
        "rate": int(words[4].split("=")[1][:-1]),
        "valves": [i[:2] for i in words[9:]],
    }

pos_rate = set()
for v in data:
    if data[v]["rate"] > 0:
        pos_rate.add(v)


def get_path_length(start, end):
    dq = deque()  # time, current_valve
    vis = set(start)
    for valve in data[start]["valves"]:
        dq.append((1, valve))

    while dq:
        valve = dq.popleft()

        if valve[1] == end:
            break
        if valve[1] not in vis:
            vis.add(valve[1])
            for next_valve in data[valve[1]]["valves"]:
                dq.append((valve[0] + 1, next_valve))
    return valve[0]


main_path = {}
for start in list(pos_rate) + ["AA"]:
    for end in pos_rate:
        if start != end:
            if start in main_path.keys():
                main_path[start][end] = get_path_length(start, end)
            else:
                main_path[start] = {end: get_path_length(start, end)}

cache = {}  #time_valve_closed : max_rate

def f(closed):
    dq = deque()
    dq.append({"time": 1, "valve": "AA", "rate": 0, "total": 0, "closed": closed})

    max_total_rate = 0
    max_possible_rate = sum([data[i]['rate'] for i in closed])
    
    while dq:
        d = dq.popleft()
        current_valve = d["valve"]
        
        # key = str(d['time']) + '_' + current_valve + '_' + str(d['closed']) + '_' + str(pos_rate - d['closed'])
        # if key in cache:
        #     cache[key] = max(cache[key], d['total'])
        #     continue
        # else:
        #     cache[key] = d['total']

        extrapolate_total_rate = d["total"] + d["rate"] * (MAX_TIME - d["time"])
        max_total_rate = max(max_total_rate, extrapolate_total_rate)

        for target_valve in d["closed"]:
            # add valve and open it
            path_length = main_path[current_valve][target_valve]

            if ((d["time"] + path_length <= MAX_TIME)
                and ((d['total'] + (MAX_TIME - d['time']) * max_possible_rate) >= max_total_rate)): 
                dq.append(
                    {
                        "time": d["time"] + path_length + 1,  # current time + travel + opening valve
                        "valve": target_valve,
                        "rate": d["rate"] + data[target_valve]["rate"],
                        "total": d["total"] + d["rate"] * (path_length + 1) + data[target_valve]["rate"],
                        "closed": d["closed"] - set([target_valve]),
                    }        
                )

    return max_total_rate

closed = pos_rate
MAX_TIME = 26
best_score = 0


max_bin = int('1'*len(pos_rate), 2)
for i in trange((max_bin + 1) // 2):
    i = str(bin(i))[2:].zfill(len(pos_rate)) # transform i into binary number
    me = set([d for d, s in zip(pos_rate, i) if int(s)]) # use binary number as a string to filter pos_rate
    el = pos_rate - me
    score = f(me) + f(el)
    if score > best_score:
        best_score = score
        # print(f(me), f(el))
    
print(best_score)


# %%

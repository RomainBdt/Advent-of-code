# %%
import pathlib
import re
from collections import deque

path = pathlib.Path.cwd() / "input.txt"

costs = {}
for line in open(path):
    num = re.findall("\d+", line)
    costs[int(num[0])] = tuple(int(i) for i in num[1:])


def dfs(t, parts, robots):
    key = f"{t}_{parts}_{robots}"

    if key in seen:
        return 0
    else:
        seen.add(key)

    ore = parts[0]
    clay = parts[1]
    obs = parts[2]
    geode = parts[3]

    ore_robot = robots[0]
    clay_robot = robots[1]
    obs_robot = robots[2]
    geode_robot = robots[3]

    new_ore = min(ore + ore_robot, maxspend[0] * (TIME - t - 1))
    new_clay = min(clay + clay_robot, maxspend[1] * (TIME - t - 1))
    new_obs = min(obs + obs_robot, maxspend[2] * (TIME - t - 1))
    new_geode = geode + geode_robot

    if t == TIME:
        return geode

    # no robot build
    score = dfs(t + 1, (new_ore, new_clay, new_obs, new_geode), robots)

    if ore >= cost[0] and ore_robot < maxspend[0]:
        score = max(
            score,
            dfs(
                t + 1,
                (new_ore - cost[0], new_clay, new_obs, new_geode),
                (ore_robot + 1, clay_robot, obs_robot, geode_robot),
            ),
        )
    if ore >= cost[1] and clay_robot < maxspend[1]:
        score = max(
            score,
            dfs(
                t + 1,
                (new_ore - cost[1], new_clay, new_obs, new_geode),
                (ore_robot, clay_robot + 1, obs_robot, geode_robot),
            ),
        )
    if ore >= cost[2] and clay >= cost[3] and obs_robot < maxspend[2]:
        score = max(
            score,
            dfs(
                t + 1,
                (new_ore - cost[2], new_clay - cost[3], new_obs, new_geode),
                (ore_robot, clay_robot, obs_robot + 1, geode_robot),
            ),
        )

    if ore >= cost[4] and obs >= cost[5]:
        score = max(
            score,
            dfs(
                t + 1,
                (new_ore - cost[4], new_clay, new_obs - cost[5], new_geode),
                (ore_robot, clay_robot, obs_robot, geode_robot + 1),
            ),
        )
    return score


TIME = 24
PARTS_INIT = (0, 0, 0, 0)
ROBOTS_INIT = (1, 0, 0, 0)
scores = []

for i in range(len(costs)):
    cost = costs[i + 1]
    seen = set()
    maxspend = (max(cost[0], cost[1], cost[2], cost[4]), cost[3], cost[5])
    scores.append(dfs(0, PARTS_INIT, ROBOTS_INIT))
    print(i, scores[-1])

ans = 0
for i, score in enumerate(scores):
    ans += (i + 1) * score

print("PART 1:", ans)


# %%
TIME = 32
scores = []
total = 1

for i in range(3):
    cost = costs[i + 1]
    seen = set()
    maxspend = (max(cost[0], cost[1], cost[2], cost[4]), cost[3], cost[5])
    scores.append(dfs(0, PARTS_INIT, ROBOTS_INIT))
    print(i, scores[-1])
    total *= scores[-1]

print("PART 2:", total)

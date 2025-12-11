from pathlib import Path
from time import time
import pandas as pd
from tqdm import tqdm
import re
from functools import cache

start_time = time()
file_num = 2
filename = "test.txt" if file_num == 1 else "input.txt"
path = Path(__file__).resolve().parent / filename

with open(path, mode="r", encoding="utf-8") as fid:
    lines = [(line.strip().split()) for line in fid]

P = dict()
for line in lines:
    k = line[0][:-1]
    P[k] = line[1:]

# Count number of paths from 'you' to 'out'
def count_paths(current, target, P, visited):
    if current == target:
        return 1
    if current in visited:
        return 0
    visited.add(current)
    total_paths = 0
    for neighbor in P.get(current, []):
        total_paths += count_paths(neighbor, target, P, visited.copy())
    return total_paths

total_paths = count_paths('you', 'out', P, set())


print("Part 1:", total_paths)
print(f"Time: {time() - start_time:.6f} seconds")

from functools import lru_cache

# precompute nodes reachable from each node
def compute_reachable(P):
    reachable = {}
    for node in P:
        seen = set()
        stack = [node]
        while stack:
            n = stack.pop()
            if n in seen:
                continue
            seen.add(n)
            for nb in P.get(n, []):
                if nb not in seen:
                    stack.append(nb)
        reachable[node] = seen
    return reachable

reachable = compute_reachable(P)
from pprint import pprint
# pprint(reachable)
REQUIRED = frozenset({'dac', 'fft'})

# Count number of paths from 'svr' to 'out' using reduced visited keys
@lru_cache(maxsize=None)
def count_paths_cached(current: str, target: str, visited: frozenset):
    # 'visited' is a reduced frozenset containing only nodes relevant for 'current'
    if current == target:
        return 1 if REQUIRED.issubset(visited) else 0
    if current in visited:
        return 0
    # mark current visited (in the reduced representation)
    new_visited = set(visited)
    new_visited.add(current)
    total = 0
    for neighbor in P.get(current, []):
        # only keep nodes that matter for the neighbour (reachable from neighbour) or required nodes
        neighbor_relevant = reachable.get(neighbor, set()) | REQUIRED
        neighbor_key = frozenset(n for n in new_visited if n in neighbor_relevant)
        total += count_paths_cached(neighbor, target, neighbor_key)
    return total

total_paths = count_paths_cached('svr', 'out', frozenset())

print("Part 2:", total_paths)
print(f"Time: {time() - start_time:.6f} seconds")
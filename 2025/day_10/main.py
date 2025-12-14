from pathlib import Path
from time import time
import pandas as pd
from tqdm import tqdm
import re
from heapq import heapify, heappop, heappush

start_time = time()
file_num = 2
filename = "test.txt" if file_num == 1 else "input.txt"
path = Path(__file__).resolve().parent / filename

with open(path, mode="r", encoding="utf-8") as fid:
    lights = []
    actions = []
    jolts = []
    for line in fid:
        bracket_content = re.findall(r'\[([^\]]*)\]', line)[0].replace('.', '0').replace('#', '1')
        lights.append(list(map(int, bracket_content)))
        parenthesis_content = [list(map(int,x.split(','))) for x in re.findall(r'\(([^)]*)\)', line)]
        actions.append(parenthesis_content)
        curly_content = re.findall(r'\{([^}]*)\}', line)[0]
        jolts.append(list(map(int, curly_content.split(','))))

results = []
i = 0
for target, moves in zip(lights, actions):
    print(f"Processing light {i+1}/{len(lights)}")
    i += 1
    # normalize to tuples for hashing
    target_t = tuple(target)
    moves_t = [tuple(m) for m in moves]
    initial_state = tuple([0] * len(target))

    # heap entries: (count, next_move_index, state_tuple)
    h = [(0, idx, initial_state) for idx in range(len(moves_t))]
    heapify(h)

    # visited cache: best known cost for (state, next_move_index)
    visited = set()

    while h:
        if len(h) > 1E9:
            print("Too many states, aborting...")
            break
        count, move_idx, state = heappop(h)

        # skip if we've seen this (state, move) with a better or equal cost
        key = (state, move_idx)
        if key in visited:
            continue
        visited.add(key)

        # check for goal
        if state == target_t:
            results.append(count)
            break

        # apply the move to produce the next state
        new_state_list = list(state)
        for idx in moves_t[move_idx]:
            new_state_list[idx] = 1 - new_state_list[idx]
        new_state = tuple(new_state_list)

        # push successors (useless to repeat same move immediately)
        for next_idx in range(len(moves_t)):
            if next_idx == move_idx:
                continue
            heappush(h, (count + 1, next_idx, new_state))

print("Part 1:", sum(results))

import z3

results = []
for i, (target, moves) in enumerate(zip(jolts, actions), 1):
    print(f"Processing light {i}/{len(jolts)}")

    o = z3.Optimize()
    move_vars = [z3.Int(f'move_{j}') for j in range(len(moves))]
    
    # Each move can be applied 0 to max(target) times
    for mv in move_vars:
        o.add(mv >= 0, mv <= max(target))
    
    # Build constraints directly from the sparse representation
    final_state = []
    for k in range(len(target)):
        # Sum contributions from all moves that affect position k
        contributions = [move_vars[j] for j, move in enumerate(moves) if k in move]
        final_state.append(z3.Sum(contributions) if contributions else 0)
    
    # Set constraints to match target
    for k in range(len(target)):
        o.add(final_state[k] == target[k])
    
    o.minimize(z3.Sum(move_vars))
    
    if o.check() == z3.sat:
        model = o.model()
        total_moves = sum(model[mv].as_long() for mv in move_vars)
        results.append(total_moves)
        
print("Part 2:", sum(results))
print(f"Time: {time() - start_time:.6f} seconds")